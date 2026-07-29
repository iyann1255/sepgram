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
    "ChannelParticipants": "channel_participants",
    "ChannelParticipantsNotModified": "channel_participants_not_modified",
    "ChannelParticipant": "channel_participant",
    "AdminLogResults": "admin_log_results",
    "SendAsPeers": "send_as_peers",
    "SponsoredMessageReportResultChooseOption": "sponsored_message_report_result_choose_option",
    "SponsoredMessageReportResultAdsHidden": "sponsored_message_report_result_ads_hidden",
    "SponsoredMessageReportResultReported": "sponsored_message_report_result_reported",
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
    from .channel_participants import ChannelParticipants
    from .channel_participants_not_modified import ChannelParticipantsNotModified
    from .channel_participant import ChannelParticipant
    from .admin_log_results import AdminLogResults
    from .send_as_peers import SendAsPeers
    from .sponsored_message_report_result_choose_option import SponsoredMessageReportResultChooseOption
    from .sponsored_message_report_result_ads_hidden import SponsoredMessageReportResultAdsHidden
    from .sponsored_message_report_result_reported import SponsoredMessageReportResultReported
