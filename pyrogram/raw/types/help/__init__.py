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
    "ConfigSimple": "config_simple",
    "AppUpdate": "app_update",
    "NoAppUpdate": "no_app_update",
    "InviteText": "invite_text",
    "Support": "support",
    "TermsOfService": "terms_of_service",
    "RecentMeUrls": "recent_me_urls",
    "TermsOfServiceUpdateEmpty": "terms_of_service_update_empty",
    "TermsOfServiceUpdate": "terms_of_service_update",
    "DeepLinkInfoEmpty": "deep_link_info_empty",
    "DeepLinkInfo": "deep_link_info",
    "PassportConfigNotModified": "passport_config_not_modified",
    "PassportConfig": "passport_config",
    "SupportName": "support_name",
    "UserInfoEmpty": "user_info_empty",
    "UserInfo": "user_info",
    "PromoDataEmpty": "promo_data_empty",
    "PromoData": "promo_data",
    "CountryCode": "country_code",
    "Country": "country",
    "CountriesListNotModified": "countries_list_not_modified",
    "CountriesList": "countries_list",
    "PremiumPromo": "premium_promo",
    "AppConfigNotModified": "app_config_not_modified",
    "AppConfig": "app_config",
    "PeerColorSet": "peer_color_set",
    "PeerColorProfileSet": "peer_color_profile_set",
    "PeerColorOption": "peer_color_option",
    "PeerColorsNotModified": "peer_colors_not_modified",
    "PeerColors": "peer_colors",
    "TimezonesListNotModified": "timezones_list_not_modified",
    "TimezonesList": "timezones_list",
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
    from .config_simple import ConfigSimple
    from .app_update import AppUpdate
    from .no_app_update import NoAppUpdate
    from .invite_text import InviteText
    from .support import Support
    from .terms_of_service import TermsOfService
    from .recent_me_urls import RecentMeUrls
    from .terms_of_service_update_empty import TermsOfServiceUpdateEmpty
    from .terms_of_service_update import TermsOfServiceUpdate
    from .deep_link_info_empty import DeepLinkInfoEmpty
    from .deep_link_info import DeepLinkInfo
    from .passport_config_not_modified import PassportConfigNotModified
    from .passport_config import PassportConfig
    from .support_name import SupportName
    from .user_info_empty import UserInfoEmpty
    from .user_info import UserInfo
    from .promo_data_empty import PromoDataEmpty
    from .promo_data import PromoData
    from .country_code import CountryCode
    from .country import Country
    from .countries_list_not_modified import CountriesListNotModified
    from .countries_list import CountriesList
    from .premium_promo import PremiumPromo
    from .app_config_not_modified import AppConfigNotModified
    from .app_config import AppConfig
    from .peer_color_set import PeerColorSet
    from .peer_color_profile_set import PeerColorProfileSet
    from .peer_color_option import PeerColorOption
    from .peer_colors_not_modified import PeerColorsNotModified
    from .peer_colors import PeerColors
    from .timezones_list_not_modified import TimezonesListNotModified
    from .timezones_list import TimezonesList
