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
    "GetBroadcastStats": "get_broadcast_stats",
    "LoadAsyncGraph": "load_async_graph",
    "GetMegagroupStats": "get_megagroup_stats",
    "GetMessagePublicForwards": "get_message_public_forwards",
    "GetMessageStats": "get_message_stats",
    "GetStoryStats": "get_story_stats",
    "GetStoryPublicForwards": "get_story_public_forwards",
    "GetPollStats": "get_poll_stats",
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
    from .get_broadcast_stats import GetBroadcastStats
    from .load_async_graph import LoadAsyncGraph
    from .get_megagroup_stats import GetMegagroupStats
    from .get_message_public_forwards import GetMessagePublicForwards
    from .get_message_stats import GetMessageStats
    from .get_story_stats import GetStoryStats
    from .get_story_public_forwards import GetStoryPublicForwards
    from .get_poll_stats import GetPollStats
