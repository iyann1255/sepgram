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
    "GetCallConfig": "get_call_config",
    "RequestCall": "request_call",
    "AcceptCall": "accept_call",
    "ConfirmCall": "confirm_call",
    "ReceivedCall": "received_call",
    "DiscardCall": "discard_call",
    "SetCallRating": "set_call_rating",
    "SaveCallDebug": "save_call_debug",
    "SendSignalingData": "send_signaling_data",
    "CreateGroupCall": "create_group_call",
    "JoinGroupCall": "join_group_call",
    "LeaveGroupCall": "leave_group_call",
    "InviteToGroupCall": "invite_to_group_call",
    "DiscardGroupCall": "discard_group_call",
    "ToggleGroupCallSettings": "toggle_group_call_settings",
    "GetGroupCall": "get_group_call",
    "GetGroupParticipants": "get_group_participants",
    "CheckGroupCall": "check_group_call",
    "ToggleGroupCallRecord": "toggle_group_call_record",
    "EditGroupCallParticipant": "edit_group_call_participant",
    "EditGroupCallTitle": "edit_group_call_title",
    "GetGroupCallJoinAs": "get_group_call_join_as",
    "ExportGroupCallInvite": "export_group_call_invite",
    "ToggleGroupCallStartSubscription": "toggle_group_call_start_subscription",
    "StartScheduledGroupCall": "start_scheduled_group_call",
    "SaveDefaultGroupCallJoinAs": "save_default_group_call_join_as",
    "JoinGroupCallPresentation": "join_group_call_presentation",
    "LeaveGroupCallPresentation": "leave_group_call_presentation",
    "GetGroupCallStreamChannels": "get_group_call_stream_channels",
    "GetGroupCallStreamRtmpUrl": "get_group_call_stream_rtmp_url",
    "SaveCallLog": "save_call_log",
    "CreateConferenceCall": "create_conference_call",
    "DeleteConferenceCallParticipants": "delete_conference_call_participants",
    "SendConferenceCallBroadcast": "send_conference_call_broadcast",
    "InviteConferenceCallParticipant": "invite_conference_call_participant",
    "DeclineConferenceCallInvite": "decline_conference_call_invite",
    "GetGroupCallChainBlocks": "get_group_call_chain_blocks",
    "SendGroupCallMessage": "send_group_call_message",
    "SendGroupCallEncryptedMessage": "send_group_call_encrypted_message",
    "DeleteGroupCallMessages": "delete_group_call_messages",
    "DeleteGroupCallParticipantMessages": "delete_group_call_participant_messages",
    "GetGroupCallStars": "get_group_call_stars",
    "SaveDefaultSendAs": "save_default_send_as",
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
    from .get_call_config import GetCallConfig
    from .request_call import RequestCall
    from .accept_call import AcceptCall
    from .confirm_call import ConfirmCall
    from .received_call import ReceivedCall
    from .discard_call import DiscardCall
    from .set_call_rating import SetCallRating
    from .save_call_debug import SaveCallDebug
    from .send_signaling_data import SendSignalingData
    from .create_group_call import CreateGroupCall
    from .join_group_call import JoinGroupCall
    from .leave_group_call import LeaveGroupCall
    from .invite_to_group_call import InviteToGroupCall
    from .discard_group_call import DiscardGroupCall
    from .toggle_group_call_settings import ToggleGroupCallSettings
    from .get_group_call import GetGroupCall
    from .get_group_participants import GetGroupParticipants
    from .check_group_call import CheckGroupCall
    from .toggle_group_call_record import ToggleGroupCallRecord
    from .edit_group_call_participant import EditGroupCallParticipant
    from .edit_group_call_title import EditGroupCallTitle
    from .get_group_call_join_as import GetGroupCallJoinAs
    from .export_group_call_invite import ExportGroupCallInvite
    from .toggle_group_call_start_subscription import ToggleGroupCallStartSubscription
    from .start_scheduled_group_call import StartScheduledGroupCall
    from .save_default_group_call_join_as import SaveDefaultGroupCallJoinAs
    from .join_group_call_presentation import JoinGroupCallPresentation
    from .leave_group_call_presentation import LeaveGroupCallPresentation
    from .get_group_call_stream_channels import GetGroupCallStreamChannels
    from .get_group_call_stream_rtmp_url import GetGroupCallStreamRtmpUrl
    from .save_call_log import SaveCallLog
    from .create_conference_call import CreateConferenceCall
    from .delete_conference_call_participants import DeleteConferenceCallParticipants
    from .send_conference_call_broadcast import SendConferenceCallBroadcast
    from .invite_conference_call_participant import InviteConferenceCallParticipant
    from .decline_conference_call_invite import DeclineConferenceCallInvite
    from .get_group_call_chain_blocks import GetGroupCallChainBlocks
    from .send_group_call_message import SendGroupCallMessage
    from .send_group_call_encrypted_message import SendGroupCallEncryptedMessage
    from .delete_group_call_messages import DeleteGroupCallMessages
    from .delete_group_call_participant_messages import DeleteGroupCallParticipantMessages
    from .get_group_call_stars import GetGroupCallStars
    from .save_default_send_as import SaveDefaultSendAs
