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
    "PrivacyRules": "privacy_rules",
    "Authorizations": "authorizations",
    "Password": "password",
    "PasswordSettings": "password_settings",
    "PasswordInputSettings": "password_input_settings",
    "TmpPassword": "tmp_password",
    "WebAuthorizations": "web_authorizations",
    "AuthorizationForm": "authorization_form",
    "SentEmailCode": "sent_email_code",
    "Takeout": "takeout",
    "WallPapers": "wall_papers",
    "AutoDownloadSettings": "auto_download_settings",
    "Themes": "themes",
    "ContentSettings": "content_settings",
    "ResetPasswordResult": "reset_password_result",
    "ChatThemes": "chat_themes",
    "SavedRingtones": "saved_ringtones",
    "SavedRingtone": "saved_ringtone",
    "EmojiStatuses": "emoji_statuses",
    "EmailVerified": "email_verified",
    "AutoSaveSettings": "auto_save_settings",
    "ConnectedBots": "connected_bots",
    "BusinessChatLinks": "business_chat_links",
    "ResolvedBusinessChatLinks": "resolved_business_chat_links",
    "PaidMessagesRevenue": "paid_messages_revenue",
    "SavedMusicIds": "saved_music_ids",
    "Passkeys": "passkeys",
    "PasskeyRegistrationOptions": "passkey_registration_options",
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
    from .privacy_rules import PrivacyRules
    from .authorizations import Authorizations
    from .password import Password
    from .password_settings import PasswordSettings
    from .password_input_settings import PasswordInputSettings
    from .tmp_password import TmpPassword
    from .web_authorizations import WebAuthorizations
    from .authorization_form import AuthorizationForm
    from .sent_email_code import SentEmailCode
    from .takeout import Takeout
    from .wall_papers import WallPapers
    from .auto_download_settings import AutoDownloadSettings
    from .themes import Themes
    from .content_settings import ContentSettings
    from .reset_password_result import ResetPasswordResult
    from .chat_themes import ChatThemes
    from .saved_ringtones import SavedRingtones
    from .saved_ringtone import SavedRingtone
    from .emoji_statuses import EmojiStatuses
    from .email_verified import EmailVerified
    from .auto_save_settings import AutoSaveSettings
    from .connected_bots import ConnectedBots
    from .business_chat_links import BusinessChatLinks
    from .resolved_business_chat_links import ResolvedBusinessChatLinks
    from .paid_messages_revenue import PaidMessagesRevenue
    from .saved_music_ids import SavedMusicIds
    from .passkeys import Passkeys
    from .passkey_registration_options import PasskeyRegistrationOptions
