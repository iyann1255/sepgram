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
    "GetContactIDs": "get_contact_i_ds",
    "GetStatuses": "get_statuses",
    "GetContacts": "get_contacts",
    "ImportContacts": "import_contacts",
    "DeleteContacts": "delete_contacts",
    "DeleteByPhones": "delete_by_phones",
    "Block": "block",
    "Unblock": "unblock",
    "GetBlocked": "get_blocked",
    "Search": "search",
    "ResolveUsername": "resolve_username",
    "GetTopPeers": "get_top_peers",
    "ResetTopPeerRating": "reset_top_peer_rating",
    "ResetSaved": "reset_saved",
    "GetSaved": "get_saved",
    "ToggleTopPeers": "toggle_top_peers",
    "AddContact": "add_contact",
    "AcceptContact": "accept_contact",
    "GetLocated": "get_located",
    "BlockFromReplies": "block_from_replies",
    "ResolvePhone": "resolve_phone",
    "ExportContactToken": "export_contact_token",
    "ImportContactToken": "import_contact_token",
    "EditCloseFriends": "edit_close_friends",
    "SetBlocked": "set_blocked",
    "GetBirthdays": "get_birthdays",
    "GetSponsoredPeers": "get_sponsored_peers",
    "UpdateContactNote": "update_contact_note",
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
    from .get_contact_i_ds import GetContactIDs
    from .get_statuses import GetStatuses
    from .get_contacts import GetContacts
    from .import_contacts import ImportContacts
    from .delete_contacts import DeleteContacts
    from .delete_by_phones import DeleteByPhones
    from .block import Block
    from .unblock import Unblock
    from .get_blocked import GetBlocked
    from .search import Search
    from .resolve_username import ResolveUsername
    from .get_top_peers import GetTopPeers
    from .reset_top_peer_rating import ResetTopPeerRating
    from .reset_saved import ResetSaved
    from .get_saved import GetSaved
    from .toggle_top_peers import ToggleTopPeers
    from .add_contact import AddContact
    from .accept_contact import AcceptContact
    from .get_located import GetLocated
    from .block_from_replies import BlockFromReplies
    from .resolve_phone import ResolvePhone
    from .export_contact_token import ExportContactToken
    from .import_contact_token import ImportContactToken
    from .edit_close_friends import EditCloseFriends
    from .set_blocked import SetBlocked
    from .get_birthdays import GetBirthdays
    from .get_sponsored_peers import GetSponsoredPeers
    from .update_contact_note import UpdateContactNote
