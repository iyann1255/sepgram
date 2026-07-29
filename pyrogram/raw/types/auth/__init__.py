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
    "SentCode": "sent_code",
    "SentCodeSuccess": "sent_code_success",
    "SentCodePaymentRequired": "sent_code_payment_required",
    "Authorization": "authorization",
    "AuthorizationSignUpRequired": "authorization_sign_up_required",
    "ExportedAuthorization": "exported_authorization",
    "PasswordRecovery": "password_recovery",
    "CodeTypeSms": "code_type_sms",
    "CodeTypeCall": "code_type_call",
    "CodeTypeFlashCall": "code_type_flash_call",
    "CodeTypeMissedCall": "code_type_missed_call",
    "CodeTypeFragmentSms": "code_type_fragment_sms",
    "SentCodeTypeApp": "sent_code_type_app",
    "SentCodeTypeSms": "sent_code_type_sms",
    "SentCodeTypeCall": "sent_code_type_call",
    "SentCodeTypeFlashCall": "sent_code_type_flash_call",
    "SentCodeTypeMissedCall": "sent_code_type_missed_call",
    "SentCodeTypeEmailCode": "sent_code_type_email_code",
    "SentCodeTypeSetUpEmailRequired": "sent_code_type_set_up_email_required",
    "SentCodeTypeFragmentSms": "sent_code_type_fragment_sms",
    "SentCodeTypeFirebaseSms": "sent_code_type_firebase_sms",
    "SentCodeTypeSmsWord": "sent_code_type_sms_word",
    "SentCodeTypeSmsPhrase": "sent_code_type_sms_phrase",
    "LoginToken": "login_token",
    "LoginTokenMigrateTo": "login_token_migrate_to",
    "LoginTokenSuccess": "login_token_success",
    "LoggedOut": "logged_out",
    "PasskeyLoginOptions": "passkey_login_options",
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
    from .sent_code import SentCode
    from .sent_code_success import SentCodeSuccess
    from .sent_code_payment_required import SentCodePaymentRequired
    from .authorization import Authorization
    from .authorization_sign_up_required import AuthorizationSignUpRequired
    from .exported_authorization import ExportedAuthorization
    from .password_recovery import PasswordRecovery
    from .code_type_sms import CodeTypeSms
    from .code_type_call import CodeTypeCall
    from .code_type_flash_call import CodeTypeFlashCall
    from .code_type_missed_call import CodeTypeMissedCall
    from .code_type_fragment_sms import CodeTypeFragmentSms
    from .sent_code_type_app import SentCodeTypeApp
    from .sent_code_type_sms import SentCodeTypeSms
    from .sent_code_type_call import SentCodeTypeCall
    from .sent_code_type_flash_call import SentCodeTypeFlashCall
    from .sent_code_type_missed_call import SentCodeTypeMissedCall
    from .sent_code_type_email_code import SentCodeTypeEmailCode
    from .sent_code_type_set_up_email_required import SentCodeTypeSetUpEmailRequired
    from .sent_code_type_fragment_sms import SentCodeTypeFragmentSms
    from .sent_code_type_firebase_sms import SentCodeTypeFirebaseSms
    from .sent_code_type_sms_word import SentCodeTypeSmsWord
    from .sent_code_type_sms_phrase import SentCodeTypeSmsPhrase
    from .login_token import LoginToken
    from .login_token_migrate_to import LoginTokenMigrateTo
    from .login_token_success import LoginTokenSuccess
    from .logged_out import LoggedOut
    from .passkey_login_options import PasskeyLoginOptions
