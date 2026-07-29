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
    "SendCode": "send_code",
    "SignUp": "sign_up",
    "SignIn": "sign_in",
    "LogOut": "log_out",
    "ResetAuthorizations": "reset_authorizations",
    "ExportAuthorization": "export_authorization",
    "ImportAuthorization": "import_authorization",
    "BindTempAuthKey": "bind_temp_auth_key",
    "ImportBotAuthorization": "import_bot_authorization",
    "CheckPassword": "check_password",
    "RequestPasswordRecovery": "request_password_recovery",
    "RecoverPassword": "recover_password",
    "ResendCode": "resend_code",
    "CancelCode": "cancel_code",
    "DropTempAuthKeys": "drop_temp_auth_keys",
    "ExportLoginToken": "export_login_token",
    "ImportLoginToken": "import_login_token",
    "AcceptLoginToken": "accept_login_token",
    "CheckRecoveryPassword": "check_recovery_password",
    "ImportWebTokenAuthorization": "import_web_token_authorization",
    "RequestFirebaseSms": "request_firebase_sms",
    "ResetLoginEmail": "reset_login_email",
    "ReportMissingCode": "report_missing_code",
    "CheckPaidAuth": "check_paid_auth",
    "InitPasskeyLogin": "init_passkey_login",
    "FinishPasskeyLogin": "finish_passkey_login",
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
    from .send_code import SendCode
    from .sign_up import SignUp
    from .sign_in import SignIn
    from .log_out import LogOut
    from .reset_authorizations import ResetAuthorizations
    from .export_authorization import ExportAuthorization
    from .import_authorization import ImportAuthorization
    from .bind_temp_auth_key import BindTempAuthKey
    from .import_bot_authorization import ImportBotAuthorization
    from .check_password import CheckPassword
    from .request_password_recovery import RequestPasswordRecovery
    from .recover_password import RecoverPassword
    from .resend_code import ResendCode
    from .cancel_code import CancelCode
    from .drop_temp_auth_keys import DropTempAuthKeys
    from .export_login_token import ExportLoginToken
    from .import_login_token import ImportLoginToken
    from .accept_login_token import AcceptLoginToken
    from .check_recovery_password import CheckRecoveryPassword
    from .import_web_token_authorization import ImportWebTokenAuthorization
    from .request_firebase_sms import RequestFirebaseSms
    from .reset_login_email import ResetLoginEmail
    from .report_missing_code import ReportMissingCode
    from .check_paid_auth import CheckPaidAuth
    from .init_passkey_login import InitPasskeyLogin
    from .finish_passkey_login import FinishPasskeyLogin
