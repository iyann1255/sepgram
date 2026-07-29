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
    "GetConfig": "get_config",
    "GetNearestDc": "get_nearest_dc",
    "GetAppUpdate": "get_app_update",
    "GetInviteText": "get_invite_text",
    "GetSupport": "get_support",
    "SetBotUpdatesStatus": "set_bot_updates_status",
    "GetCdnConfig": "get_cdn_config",
    "GetRecentMeUrls": "get_recent_me_urls",
    "GetTermsOfServiceUpdate": "get_terms_of_service_update",
    "AcceptTermsOfService": "accept_terms_of_service",
    "GetDeepLinkInfo": "get_deep_link_info",
    "GetAppConfig": "get_app_config",
    "SaveAppLog": "save_app_log",
    "GetPassportConfig": "get_passport_config",
    "GetSupportName": "get_support_name",
    "GetUserInfo": "get_user_info",
    "EditUserInfo": "edit_user_info",
    "GetPromoData": "get_promo_data",
    "HidePromoData": "hide_promo_data",
    "DismissSuggestion": "dismiss_suggestion",
    "GetCountriesList": "get_countries_list",
    "GetPremiumPromo": "get_premium_promo",
    "GetPeerColors": "get_peer_colors",
    "GetPeerProfileColors": "get_peer_profile_colors",
    "GetTimezonesList": "get_timezones_list",
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
    from .get_config import GetConfig
    from .get_nearest_dc import GetNearestDc
    from .get_app_update import GetAppUpdate
    from .get_invite_text import GetInviteText
    from .get_support import GetSupport
    from .set_bot_updates_status import SetBotUpdatesStatus
    from .get_cdn_config import GetCdnConfig
    from .get_recent_me_urls import GetRecentMeUrls
    from .get_terms_of_service_update import GetTermsOfServiceUpdate
    from .accept_terms_of_service import AcceptTermsOfService
    from .get_deep_link_info import GetDeepLinkInfo
    from .get_app_config import GetAppConfig
    from .save_app_log import SaveAppLog
    from .get_passport_config import GetPassportConfig
    from .get_support_name import GetSupportName
    from .get_user_info import GetUserInfo
    from .edit_user_info import EditUserInfo
    from .get_promo_data import GetPromoData
    from .hide_promo_data import HidePromoData
    from .dismiss_suggestion import DismissSuggestion
    from .get_countries_list import GetCountriesList
    from .get_premium_promo import GetPremiumPromo
    from .get_peer_colors import GetPeerColors
    from .get_peer_profile_colors import GetPeerProfileColors
    from .get_timezones_list import GetTimezonesList
