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
from typing import Any, Dict, ItemsView, List, Tuple


class LazyObjects(dict):
    """Constructor id -> TL class mapping that imports each class on first use.

    Resolving all TL classes up front (the historical behaviour) forced an import of
    every single generated raw module at ``import pyrogram`` time. That was the single
    largest chunk of startup latency and resident memory, for classes most apps never
    touch. Here a value starts out as its dotted import path and is swapped in place for
    the real class the first time its constructor id is looked up, so deserialization is
    a plain dict hit from then on.
    """

    __slots__ = ()

    def __getitem__(self, key: int) -> Any:
        value = dict.__getitem__(self, key)

        if type(value) is str:
            path, name = value.rsplit(".", 1)
            value = getattr(import_module(path), name)
            dict.__setitem__(self, key, value)

        return value

    def get(self, key: int, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def values(self) -> List[Any]:  # type: ignore[override]
        return [self[k] for k in dict.keys(self)]

    def items(self) -> ItemsView[int, Any]:  # type: ignore[override]
        return dict(self.resolve_all()).items()

    def copy(self) -> Dict[int, Any]:  # type: ignore[override]
        return dict(self.resolve_all())

    def resolve_all(self) -> "LazyObjects":
        """Eagerly import every TL class. Only useful for tooling and tests."""
        for k in list(dict.keys(self)):
            self[k]

        return self

    def __iter__(self):
        return dict.__iter__(self)

    def __reduce__(self) -> Tuple[Any, ...]:
        return dict, (dict(self.resolve_all()),)
