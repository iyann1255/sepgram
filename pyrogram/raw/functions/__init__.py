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
    "ReqPq": "req_pq",
    "ReqPqMulti": "req_pq_multi",
    "ReqDHParams": "req_dh_params",
    "SetClientDHParams": "set_client_dh_params",
    "DestroyAuthKey": "destroy_auth_key",
    "RpcDropAnswer": "rpc_drop_answer",
    "GetFutureSalts": "get_future_salts",
    "Ping": "ping",
    "PingDelayDisconnect": "ping_delay_disconnect",
    "DestroySession": "destroy_session",
    "InvokeAfterMsg": "invoke_after_msg",
    "InvokeAfterMsgs": "invoke_after_msgs",
    "InitConnection": "init_connection",
    "InvokeWithLayer": "invoke_with_layer",
    "InvokeWithoutUpdates": "invoke_without_updates",
    "InvokeWithMessagesRange": "invoke_with_messages_range",
    "InvokeWithTakeout": "invoke_with_takeout",
    "InvokeWithBusinessConnection": "invoke_with_business_connection",
    "InvokeWithGooglePlayIntegrity": "invoke_with_google_play_integrity",
    "InvokeWithApnsSecret": "invoke_with_apns_secret",
    "InvokeWithReCaptcha": "invoke_with_re_captcha",
}

_SUBMODULES = frozenset((
    "contest",
    "auth",
    "account",
    "users",
    "contacts",
    "messages",
    "updates",
    "photos",
    "upload",
    "help",
    "channels",
    "bots",
    "payments",
    "stickers",
    "phone",
    "langpack",
    "folders",
    "stats",
    "chatlists",
    "stories",
    "premium",
    "smsjobs",
    "fragment",
    "aicompose",
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
    from .req_pq import ReqPq
    from .req_pq_multi import ReqPqMulti
    from .req_dh_params import ReqDHParams
    from .set_client_dh_params import SetClientDHParams
    from .destroy_auth_key import DestroyAuthKey
    from .rpc_drop_answer import RpcDropAnswer
    from .get_future_salts import GetFutureSalts
    from .ping import Ping
    from .ping_delay_disconnect import PingDelayDisconnect
    from .destroy_session import DestroySession
    from .invoke_after_msg import InvokeAfterMsg
    from .invoke_after_msgs import InvokeAfterMsgs
    from .init_connection import InitConnection
    from .invoke_with_layer import InvokeWithLayer
    from .invoke_without_updates import InvokeWithoutUpdates
    from .invoke_with_messages_range import InvokeWithMessagesRange
    from .invoke_with_takeout import InvokeWithTakeout
    from .invoke_with_business_connection import InvokeWithBusinessConnection
    from .invoke_with_google_play_integrity import InvokeWithGooglePlayIntegrity
    from .invoke_with_apns_secret import InvokeWithApnsSecret
    from .invoke_with_re_captcha import InvokeWithReCaptcha
    from . import contest
    from . import auth
    from . import account
    from . import users
    from . import contacts
    from . import messages
    from . import updates
    from . import photos
    from . import upload
    from . import help
    from . import channels
    from . import bots
    from . import payments
    from . import stickers
    from . import phone
    from . import langpack
    from . import folders
    from . import stats
    from . import chatlists
    from . import stories
    from . import premium
    from . import smsjobs
    from . import fragment
    from . import aicompose
