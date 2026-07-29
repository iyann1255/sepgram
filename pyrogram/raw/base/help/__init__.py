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
    "InviteText": "invite_text",
    "Support": "support",
    "TermsOfService": "terms_of_service",
    "RecentMeUrls": "recent_me_urls",
    "TermsOfServiceUpdate": "terms_of_service_update",
    "DeepLinkInfo": "deep_link_info",
    "PassportConfig": "passport_config",
    "SupportName": "support_name",
    "UserInfo": "user_info",
    "PromoData": "promo_data",
    "CountryCode": "country_code",
    "Country": "country",
    "CountriesList": "countries_list",
    "PremiumPromo": "premium_promo",
    "AppConfig": "app_config",
    "PeerColorSet": "peer_color_set",
    "PeerColorOption": "peer_color_option",
    "PeerColors": "peer_colors",
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
    from .invite_text import InviteText
    from .support import Support
    from .terms_of_service import TermsOfService
    from .recent_me_urls import RecentMeUrls
    from .terms_of_service_update import TermsOfServiceUpdate
    from .deep_link_info import DeepLinkInfo
    from .passport_config import PassportConfig
    from .support_name import SupportName
    from .user_info import UserInfo
    from .promo_data import PromoData
    from .country_code import CountryCode
    from .country import Country
    from .countries_list import CountriesList
    from .premium_promo import PremiumPromo
    from .app_config import AppConfig
    from .peer_color_set import PeerColorSet
    from .peer_color_option import PeerColorOption
    from .peer_colors import PeerColors
    from .timezones_list import TimezonesList
