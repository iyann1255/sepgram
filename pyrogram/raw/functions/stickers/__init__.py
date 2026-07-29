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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from importlib import import_module
from typing import TYPE_CHECKING

_OBJECTS = {
    "CreateStickerSet": "create_sticker_set",
    "RemoveStickerFromSet": "remove_sticker_from_set",
    "ChangeStickerPosition": "change_sticker_position",
    "AddStickerToSet": "add_sticker_to_set",
    "SetStickerSetThumb": "set_sticker_set_thumb",
    "CheckShortName": "check_short_name",
    "SuggestShortName": "suggest_short_name",
    "ChangeSticker": "change_sticker",
    "RenameStickerSet": "rename_sticker_set",
    "DeleteStickerSet": "delete_sticker_set",
    "ReplaceSticker": "replace_sticker",
}

_SUBMODULES = frozenset((
))

__all__ = [*_OBJECTS, *_SUBMODULES]


def __getattr__(name: str):
    module = _OBJECTS.get(name)

    if module is not None:
        value = getattr(import_module("." + module, __name__), name)
    elif name in _SUBMODULES:
        value = import_module("." + name, __name__)
    else:
        raise AttributeError(
            f"module {__name__!r} has no attribute {name!r}"
        )

    globals()[name] = value  # cache: subsequent lookups skip __getattr__
    return value


def __dir__():
    return sorted(__all__)


if TYPE_CHECKING:
    from .create_sticker_set import CreateStickerSet
    from .remove_sticker_from_set import RemoveStickerFromSet
    from .change_sticker_position import ChangeStickerPosition
    from .add_sticker_to_set import AddStickerToSet
    from .set_sticker_set_thumb import SetStickerSetThumb
    from .check_short_name import CheckShortName
    from .suggest_short_name import SuggestShortName
    from .change_sticker import ChangeSticker
    from .rename_sticker_set import RenameStickerSet
    from .delete_sticker_set import DeleteStickerSet
    from .replace_sticker import ReplaceSticker
