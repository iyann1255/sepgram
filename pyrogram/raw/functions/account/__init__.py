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
    "RegisterDevice": "register_device",
    "UnregisterDevice": "unregister_device",
    "UpdateNotifySettings": "update_notify_settings",
    "GetNotifySettings": "get_notify_settings",
    "ResetNotifySettings": "reset_notify_settings",
    "UpdateProfile": "update_profile",
    "UpdateStatus": "update_status",
    "GetWallPapers": "get_wall_papers",
    "ReportPeer": "report_peer",
    "CheckUsername": "check_username",
    "UpdateUsername": "update_username",
    "GetPrivacy": "get_privacy",
    "SetPrivacy": "set_privacy",
    "DeleteAccount": "delete_account",
    "GetAccountTTL": "get_account_ttl",
    "SetAccountTTL": "set_account_ttl",
    "SendChangePhoneCode": "send_change_phone_code",
    "ChangePhone": "change_phone",
    "UpdateDeviceLocked": "update_device_locked",
    "GetAuthorizations": "get_authorizations",
    "ResetAuthorization": "reset_authorization",
    "GetPassword": "get_password",
    "GetPasswordSettings": "get_password_settings",
    "UpdatePasswordSettings": "update_password_settings",
    "SendConfirmPhoneCode": "send_confirm_phone_code",
    "ConfirmPhone": "confirm_phone",
    "GetTmpPassword": "get_tmp_password",
    "GetWebAuthorizations": "get_web_authorizations",
    "ResetWebAuthorization": "reset_web_authorization",
    "ResetWebAuthorizations": "reset_web_authorizations",
    "GetAllSecureValues": "get_all_secure_values",
    "GetSecureValue": "get_secure_value",
    "SaveSecureValue": "save_secure_value",
    "DeleteSecureValue": "delete_secure_value",
    "GetAuthorizationForm": "get_authorization_form",
    "AcceptAuthorization": "accept_authorization",
    "SendVerifyPhoneCode": "send_verify_phone_code",
    "VerifyPhone": "verify_phone",
    "SendVerifyEmailCode": "send_verify_email_code",
    "VerifyEmail": "verify_email",
    "InitTakeoutSession": "init_takeout_session",
    "FinishTakeoutSession": "finish_takeout_session",
    "ConfirmPasswordEmail": "confirm_password_email",
    "ResendPasswordEmail": "resend_password_email",
    "CancelPasswordEmail": "cancel_password_email",
    "GetContactSignUpNotification": "get_contact_sign_up_notification",
    "SetContactSignUpNotification": "set_contact_sign_up_notification",
    "GetNotifyExceptions": "get_notify_exceptions",
    "GetWallPaper": "get_wall_paper",
    "UploadWallPaper": "upload_wall_paper",
    "SaveWallPaper": "save_wall_paper",
    "InstallWallPaper": "install_wall_paper",
    "ResetWallPapers": "reset_wall_papers",
    "GetAutoDownloadSettings": "get_auto_download_settings",
    "SaveAutoDownloadSettings": "save_auto_download_settings",
    "UploadTheme": "upload_theme",
    "CreateTheme": "create_theme",
    "UpdateTheme": "update_theme",
    "SaveTheme": "save_theme",
    "InstallTheme": "install_theme",
    "GetTheme": "get_theme",
    "GetThemes": "get_themes",
    "SetContentSettings": "set_content_settings",
    "GetContentSettings": "get_content_settings",
    "GetMultiWallPapers": "get_multi_wall_papers",
    "GetGlobalPrivacySettings": "get_global_privacy_settings",
    "SetGlobalPrivacySettings": "set_global_privacy_settings",
    "ReportProfilePhoto": "report_profile_photo",
    "ResetPassword": "reset_password",
    "DeclinePasswordReset": "decline_password_reset",
    "GetChatThemes": "get_chat_themes",
    "SetAuthorizationTTL": "set_authorization_ttl",
    "ChangeAuthorizationSettings": "change_authorization_settings",
    "GetSavedRingtones": "get_saved_ringtones",
    "SaveRingtone": "save_ringtone",
    "UploadRingtone": "upload_ringtone",
    "UpdateEmojiStatus": "update_emoji_status",
    "GetDefaultEmojiStatuses": "get_default_emoji_statuses",
    "GetRecentEmojiStatuses": "get_recent_emoji_statuses",
    "ClearRecentEmojiStatuses": "clear_recent_emoji_statuses",
    "ReorderUsernames": "reorder_usernames",
    "ToggleUsername": "toggle_username",
    "GetDefaultProfilePhotoEmojis": "get_default_profile_photo_emojis",
    "GetDefaultGroupPhotoEmojis": "get_default_group_photo_emojis",
    "GetAutoSaveSettings": "get_auto_save_settings",
    "SaveAutoSaveSettings": "save_auto_save_settings",
    "DeleteAutoSaveExceptions": "delete_auto_save_exceptions",
    "InvalidateSignInCodes": "invalidate_sign_in_codes",
    "UpdateColor": "update_color",
    "GetDefaultBackgroundEmojis": "get_default_background_emojis",
    "GetChannelDefaultEmojiStatuses": "get_channel_default_emoji_statuses",
    "GetChannelRestrictedStatusEmojis": "get_channel_restricted_status_emojis",
    "UpdateBusinessWorkHours": "update_business_work_hours",
    "UpdateBusinessLocation": "update_business_location",
    "UpdateBusinessGreetingMessage": "update_business_greeting_message",
    "UpdateBusinessAwayMessage": "update_business_away_message",
    "UpdateConnectedBot": "update_connected_bot",
    "GetConnectedBots": "get_connected_bots",
    "GetBotBusinessConnection": "get_bot_business_connection",
    "UpdateBusinessIntro": "update_business_intro",
    "ToggleConnectedBotPaused": "toggle_connected_bot_paused",
    "DisablePeerConnectedBot": "disable_peer_connected_bot",
    "UpdateBirthday": "update_birthday",
    "CreateBusinessChatLink": "create_business_chat_link",
    "EditBusinessChatLink": "edit_business_chat_link",
    "DeleteBusinessChatLink": "delete_business_chat_link",
    "GetBusinessChatLinks": "get_business_chat_links",
    "ResolveBusinessChatLink": "resolve_business_chat_link",
    "UpdatePersonalChannel": "update_personal_channel",
    "ToggleSponsoredMessages": "toggle_sponsored_messages",
    "GetReactionsNotifySettings": "get_reactions_notify_settings",
    "SetReactionsNotifySettings": "set_reactions_notify_settings",
    "GetCollectibleEmojiStatuses": "get_collectible_emoji_statuses",
    "GetPaidMessagesRevenue": "get_paid_messages_revenue",
    "ToggleNoPaidMessagesException": "toggle_no_paid_messages_exception",
    "SetMainProfileTab": "set_main_profile_tab",
    "SaveMusic": "save_music",
    "GetSavedMusicIds": "get_saved_music_ids",
    "GetUniqueGiftChatThemes": "get_unique_gift_chat_themes",
    "InitPasskeyRegistration": "init_passkey_registration",
    "RegisterPasskey": "register_passkey",
    "GetPasskeys": "get_passkeys",
    "DeletePasskey": "delete_passkey",
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
    from .register_device import RegisterDevice
    from .unregister_device import UnregisterDevice
    from .update_notify_settings import UpdateNotifySettings
    from .get_notify_settings import GetNotifySettings
    from .reset_notify_settings import ResetNotifySettings
    from .update_profile import UpdateProfile
    from .update_status import UpdateStatus
    from .get_wall_papers import GetWallPapers
    from .report_peer import ReportPeer
    from .check_username import CheckUsername
    from .update_username import UpdateUsername
    from .get_privacy import GetPrivacy
    from .set_privacy import SetPrivacy
    from .delete_account import DeleteAccount
    from .get_account_ttl import GetAccountTTL
    from .set_account_ttl import SetAccountTTL
    from .send_change_phone_code import SendChangePhoneCode
    from .change_phone import ChangePhone
    from .update_device_locked import UpdateDeviceLocked
    from .get_authorizations import GetAuthorizations
    from .reset_authorization import ResetAuthorization
    from .get_password import GetPassword
    from .get_password_settings import GetPasswordSettings
    from .update_password_settings import UpdatePasswordSettings
    from .send_confirm_phone_code import SendConfirmPhoneCode
    from .confirm_phone import ConfirmPhone
    from .get_tmp_password import GetTmpPassword
    from .get_web_authorizations import GetWebAuthorizations
    from .reset_web_authorization import ResetWebAuthorization
    from .reset_web_authorizations import ResetWebAuthorizations
    from .get_all_secure_values import GetAllSecureValues
    from .get_secure_value import GetSecureValue
    from .save_secure_value import SaveSecureValue
    from .delete_secure_value import DeleteSecureValue
    from .get_authorization_form import GetAuthorizationForm
    from .accept_authorization import AcceptAuthorization
    from .send_verify_phone_code import SendVerifyPhoneCode
    from .verify_phone import VerifyPhone
    from .send_verify_email_code import SendVerifyEmailCode
    from .verify_email import VerifyEmail
    from .init_takeout_session import InitTakeoutSession
    from .finish_takeout_session import FinishTakeoutSession
    from .confirm_password_email import ConfirmPasswordEmail
    from .resend_password_email import ResendPasswordEmail
    from .cancel_password_email import CancelPasswordEmail
    from .get_contact_sign_up_notification import GetContactSignUpNotification
    from .set_contact_sign_up_notification import SetContactSignUpNotification
    from .get_notify_exceptions import GetNotifyExceptions
    from .get_wall_paper import GetWallPaper
    from .upload_wall_paper import UploadWallPaper
    from .save_wall_paper import SaveWallPaper
    from .install_wall_paper import InstallWallPaper
    from .reset_wall_papers import ResetWallPapers
    from .get_auto_download_settings import GetAutoDownloadSettings
    from .save_auto_download_settings import SaveAutoDownloadSettings
    from .upload_theme import UploadTheme
    from .create_theme import CreateTheme
    from .update_theme import UpdateTheme
    from .save_theme import SaveTheme
    from .install_theme import InstallTheme
    from .get_theme import GetTheme
    from .get_themes import GetThemes
    from .set_content_settings import SetContentSettings
    from .get_content_settings import GetContentSettings
    from .get_multi_wall_papers import GetMultiWallPapers
    from .get_global_privacy_settings import GetGlobalPrivacySettings
    from .set_global_privacy_settings import SetGlobalPrivacySettings
    from .report_profile_photo import ReportProfilePhoto
    from .reset_password import ResetPassword
    from .decline_password_reset import DeclinePasswordReset
    from .get_chat_themes import GetChatThemes
    from .set_authorization_ttl import SetAuthorizationTTL
    from .change_authorization_settings import ChangeAuthorizationSettings
    from .get_saved_ringtones import GetSavedRingtones
    from .save_ringtone import SaveRingtone
    from .upload_ringtone import UploadRingtone
    from .update_emoji_status import UpdateEmojiStatus
    from .get_default_emoji_statuses import GetDefaultEmojiStatuses
    from .get_recent_emoji_statuses import GetRecentEmojiStatuses
    from .clear_recent_emoji_statuses import ClearRecentEmojiStatuses
    from .reorder_usernames import ReorderUsernames
    from .toggle_username import ToggleUsername
    from .get_default_profile_photo_emojis import GetDefaultProfilePhotoEmojis
    from .get_default_group_photo_emojis import GetDefaultGroupPhotoEmojis
    from .get_auto_save_settings import GetAutoSaveSettings
    from .save_auto_save_settings import SaveAutoSaveSettings
    from .delete_auto_save_exceptions import DeleteAutoSaveExceptions
    from .invalidate_sign_in_codes import InvalidateSignInCodes
    from .update_color import UpdateColor
    from .get_default_background_emojis import GetDefaultBackgroundEmojis
    from .get_channel_default_emoji_statuses import GetChannelDefaultEmojiStatuses
    from .get_channel_restricted_status_emojis import GetChannelRestrictedStatusEmojis
    from .update_business_work_hours import UpdateBusinessWorkHours
    from .update_business_location import UpdateBusinessLocation
    from .update_business_greeting_message import UpdateBusinessGreetingMessage
    from .update_business_away_message import UpdateBusinessAwayMessage
    from .update_connected_bot import UpdateConnectedBot
    from .get_connected_bots import GetConnectedBots
    from .get_bot_business_connection import GetBotBusinessConnection
    from .update_business_intro import UpdateBusinessIntro
    from .toggle_connected_bot_paused import ToggleConnectedBotPaused
    from .disable_peer_connected_bot import DisablePeerConnectedBot
    from .update_birthday import UpdateBirthday
    from .create_business_chat_link import CreateBusinessChatLink
    from .edit_business_chat_link import EditBusinessChatLink
    from .delete_business_chat_link import DeleteBusinessChatLink
    from .get_business_chat_links import GetBusinessChatLinks
    from .resolve_business_chat_link import ResolveBusinessChatLink
    from .update_personal_channel import UpdatePersonalChannel
    from .toggle_sponsored_messages import ToggleSponsoredMessages
    from .get_reactions_notify_settings import GetReactionsNotifySettings
    from .set_reactions_notify_settings import SetReactionsNotifySettings
    from .get_collectible_emoji_statuses import GetCollectibleEmojiStatuses
    from .get_paid_messages_revenue import GetPaidMessagesRevenue
    from .toggle_no_paid_messages_exception import ToggleNoPaidMessagesException
    from .set_main_profile_tab import SetMainProfileTab
    from .save_music import SaveMusic
    from .get_saved_music_ids import GetSavedMusicIds
    from .get_unique_gift_chat_themes import GetUniqueGiftChatThemes
    from .init_passkey_registration import InitPasskeyRegistration
    from .register_passkey import RegisterPasskey
    from .get_passkeys import GetPasskeys
    from .delete_passkey import DeletePasskey
