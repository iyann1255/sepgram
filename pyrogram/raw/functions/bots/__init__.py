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
    "SendCustomRequest": "send_custom_request",
    "AnswerWebhookJSONQuery": "answer_webhook_json_query",
    "SetBotCommands": "set_bot_commands",
    "ResetBotCommands": "reset_bot_commands",
    "GetBotCommands": "get_bot_commands",
    "SetBotMenuButton": "set_bot_menu_button",
    "GetBotMenuButton": "get_bot_menu_button",
    "SetBotBroadcastDefaultAdminRights": "set_bot_broadcast_default_admin_rights",
    "SetBotGroupDefaultAdminRights": "set_bot_group_default_admin_rights",
    "SetBotInfo": "set_bot_info",
    "GetBotInfo": "get_bot_info",
    "ReorderUsernames": "reorder_usernames",
    "ToggleUsername": "toggle_username",
    "CanSendMessage": "can_send_message",
    "AllowSendMessage": "allow_send_message",
    "InvokeWebViewCustomMethod": "invoke_web_view_custom_method",
    "GetPopularAppBots": "get_popular_app_bots",
    "AddPreviewMedia": "add_preview_media",
    "EditPreviewMedia": "edit_preview_media",
    "DeletePreviewMedia": "delete_preview_media",
    "ReorderPreviewMedias": "reorder_preview_medias",
    "GetPreviewInfo": "get_preview_info",
    "GetPreviewMedias": "get_preview_medias",
    "UpdateUserEmojiStatus": "update_user_emoji_status",
    "ToggleUserEmojiStatusPermission": "toggle_user_emoji_status_permission",
    "CheckDownloadFileParams": "check_download_file_params",
    "GetAdminedBots": "get_admined_bots",
    "UpdateStarRefProgram": "update_star_ref_program",
    "SetCustomVerification": "set_custom_verification",
    "GetBotRecommendations": "get_bot_recommendations",
    "CheckUsername": "check_username",
    "CreateBot": "create_bot",
    "ExportBotToken": "export_bot_token",
    "RequestWebViewButton": "request_web_view_button",
    "GetRequestedWebViewButton": "get_requested_web_view_button",
    "GetAccessSettings": "get_access_settings",
    "EditAccessSettings": "edit_access_settings",
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
    from .send_custom_request import SendCustomRequest
    from .answer_webhook_json_query import AnswerWebhookJSONQuery
    from .set_bot_commands import SetBotCommands
    from .reset_bot_commands import ResetBotCommands
    from .get_bot_commands import GetBotCommands
    from .set_bot_menu_button import SetBotMenuButton
    from .get_bot_menu_button import GetBotMenuButton
    from .set_bot_broadcast_default_admin_rights import SetBotBroadcastDefaultAdminRights
    from .set_bot_group_default_admin_rights import SetBotGroupDefaultAdminRights
    from .set_bot_info import SetBotInfo
    from .get_bot_info import GetBotInfo
    from .reorder_usernames import ReorderUsernames
    from .toggle_username import ToggleUsername
    from .can_send_message import CanSendMessage
    from .allow_send_message import AllowSendMessage
    from .invoke_web_view_custom_method import InvokeWebViewCustomMethod
    from .get_popular_app_bots import GetPopularAppBots
    from .add_preview_media import AddPreviewMedia
    from .edit_preview_media import EditPreviewMedia
    from .delete_preview_media import DeletePreviewMedia
    from .reorder_preview_medias import ReorderPreviewMedias
    from .get_preview_info import GetPreviewInfo
    from .get_preview_medias import GetPreviewMedias
    from .update_user_emoji_status import UpdateUserEmojiStatus
    from .toggle_user_emoji_status_permission import ToggleUserEmojiStatusPermission
    from .check_download_file_params import CheckDownloadFileParams
    from .get_admined_bots import GetAdminedBots
    from .update_star_ref_program import UpdateStarRefProgram
    from .set_custom_verification import SetCustomVerification
    from .get_bot_recommendations import GetBotRecommendations
    from .check_username import CheckUsername
    from .create_bot import CreateBot
    from .export_bot_token import ExportBotToken
    from .request_web_view_button import RequestWebViewButton
    from .get_requested_web_view_button import GetRequestedWebViewButton
    from .get_access_settings import GetAccessSettings
    from .edit_access_settings import EditAccessSettings
