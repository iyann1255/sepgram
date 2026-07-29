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
    "ExportChatlistInvite": "export_chatlist_invite",
    "DeleteExportedInvite": "delete_exported_invite",
    "EditExportedInvite": "edit_exported_invite",
    "GetExportedInvites": "get_exported_invites",
    "CheckChatlistInvite": "check_chatlist_invite",
    "JoinChatlistInvite": "join_chatlist_invite",
    "GetChatlistUpdates": "get_chatlist_updates",
    "JoinChatlistUpdates": "join_chatlist_updates",
    "HideChatlistUpdates": "hide_chatlist_updates",
    "GetLeaveChatlistSuggestions": "get_leave_chatlist_suggestions",
    "LeaveChatlist": "leave_chatlist",
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
    from .export_chatlist_invite import ExportChatlistInvite
    from .delete_exported_invite import DeleteExportedInvite
    from .edit_exported_invite import EditExportedInvite
    from .get_exported_invites import GetExportedInvites
    from .check_chatlist_invite import CheckChatlistInvite
    from .join_chatlist_invite import JoinChatlistInvite
    from .get_chatlist_updates import GetChatlistUpdates
    from .join_chatlist_updates import JoinChatlistUpdates
    from .hide_chatlist_updates import HideChatlistUpdates
    from .get_leave_chatlist_suggestions import GetLeaveChatlistSuggestions
    from .leave_chatlist import LeaveChatlist
