#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from importlib import import_module
from typing import Any, Dict, Iterator, List, Tuple


class LazyObjects(dict):
    """Constructor id -> TL class mapping that imports each class on first use.

    Resolving every TL class up front forced an import of all generated raw modules at
    ``import pyrogram`` time: the largest single chunk of startup latency and resident
    memory, for classes most applications never touch.

    The mapping deliberately starts **empty** and resolves through ``__missing__``.
    ``dict.__missing__`` is only consulted for keys that are absent, so once a
    constructor id has been resolved and cached it is found by CPython's C-level dict
    lookup with no Python-level call in the way. That matters because ``TLObject.read``
    hits this mapping for every object and every nested object of every incoming
    update, so a Python ``__getitem__`` override here would tax the hottest path in the
    library.
    """

    __slots__ = ("_paths",)

    def __init__(self, paths: Dict[int, str]):
        super().__init__()
        self._paths = paths

    def __missing__(self, key: int) -> Any:
        path = self._paths[key]  # raises KeyError for genuinely unknown constructors
        module, name = path.rsplit(".", 1)
        value = getattr(import_module(module), name)
        dict.__setitem__(self, key, value)
        return value

    # The container must still behave like the full mapping it represents, even though
    # only the touched subset is materialised.
    def __len__(self) -> int:
        return len(self._paths)

    def __iter__(self) -> Iterator[int]:
        return iter(self._paths)

    def __contains__(self, key: object) -> bool:
        return key in self._paths

    def keys(self):  # type: ignore[override]
        return self._paths.keys()

    def get(self, key: int, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def values(self) -> List[Any]:  # type: ignore[override]
        return [self[k] for k in self._paths]

    def items(self) -> List[Tuple[int, Any]]:  # type: ignore[override]
        return [(k, self[k]) for k in self._paths]

    def copy(self) -> Dict[int, Any]:  # type: ignore[override]
        return dict(self.items())

    def resolve_all(self) -> "LazyObjects":
        """Eagerly import every TL class. Only useful for tooling and tests."""
        for key in self._paths:
            self[key]

        return self

    def __reduce__(self) -> Tuple[Any, ...]:
        return dict, (self.copy(),)
