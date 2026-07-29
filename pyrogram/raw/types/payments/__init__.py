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
    "PaymentForm": "payment_form",
    "PaymentFormStars": "payment_form_stars",
    "PaymentFormStarGift": "payment_form_star_gift",
    "ValidatedRequestedInfo": "validated_requested_info",
    "PaymentResult": "payment_result",
    "PaymentVerificationNeeded": "payment_verification_needed",
    "PaymentReceipt": "payment_receipt",
    "PaymentReceiptStars": "payment_receipt_stars",
    "SavedInfo": "saved_info",
    "BankCardData": "bank_card_data",
    "ExportedInvoice": "exported_invoice",
    "CheckedGiftCode": "checked_gift_code",
    "GiveawayInfo": "giveaway_info",
    "GiveawayInfoResults": "giveaway_info_results",
    "StarsStatus": "stars_status",
    "StarsRevenueStats": "stars_revenue_stats",
    "StarsRevenueWithdrawalUrl": "stars_revenue_withdrawal_url",
    "StarsRevenueAdsAccountUrl": "stars_revenue_ads_account_url",
    "StarGiftsNotModified": "star_gifts_not_modified",
    "StarGifts": "star_gifts",
    "ConnectedStarRefBots": "connected_star_ref_bots",
    "SuggestedStarRefBots": "suggested_star_ref_bots",
    "StarGiftUpgradePreview": "star_gift_upgrade_preview",
    "UniqueStarGift": "unique_star_gift",
    "SavedStarGifts": "saved_star_gifts",
    "StarGiftWithdrawalUrl": "star_gift_withdrawal_url",
    "ResaleStarGifts": "resale_star_gifts",
    "StarGiftCollectionsNotModified": "star_gift_collections_not_modified",
    "StarGiftCollections": "star_gift_collections",
    "UniqueStarGiftValueInfo": "unique_star_gift_value_info",
    "CheckCanSendGiftResultOk": "check_can_send_gift_result_ok",
    "CheckCanSendGiftResultFail": "check_can_send_gift_result_fail",
    "StarGiftAuctionState": "star_gift_auction_state",
    "StarGiftAuctionAcquiredGifts": "star_gift_auction_acquired_gifts",
    "StarGiftActiveAuctionsNotModified": "star_gift_active_auctions_not_modified",
    "StarGiftActiveAuctions": "star_gift_active_auctions",
    "StarGiftUpgradeAttributes": "star_gift_upgrade_attributes",
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
    from .payment_form import PaymentForm
    from .payment_form_stars import PaymentFormStars
    from .payment_form_star_gift import PaymentFormStarGift
    from .validated_requested_info import ValidatedRequestedInfo
    from .payment_result import PaymentResult
    from .payment_verification_needed import PaymentVerificationNeeded
    from .payment_receipt import PaymentReceipt
    from .payment_receipt_stars import PaymentReceiptStars
    from .saved_info import SavedInfo
    from .bank_card_data import BankCardData
    from .exported_invoice import ExportedInvoice
    from .checked_gift_code import CheckedGiftCode
    from .giveaway_info import GiveawayInfo
    from .giveaway_info_results import GiveawayInfoResults
    from .stars_status import StarsStatus
    from .stars_revenue_stats import StarsRevenueStats
    from .stars_revenue_withdrawal_url import StarsRevenueWithdrawalUrl
    from .stars_revenue_ads_account_url import StarsRevenueAdsAccountUrl
    from .star_gifts_not_modified import StarGiftsNotModified
    from .star_gifts import StarGifts
    from .connected_star_ref_bots import ConnectedStarRefBots
    from .suggested_star_ref_bots import SuggestedStarRefBots
    from .star_gift_upgrade_preview import StarGiftUpgradePreview
    from .unique_star_gift import UniqueStarGift
    from .saved_star_gifts import SavedStarGifts
    from .star_gift_withdrawal_url import StarGiftWithdrawalUrl
    from .resale_star_gifts import ResaleStarGifts
    from .star_gift_collections_not_modified import StarGiftCollectionsNotModified
    from .star_gift_collections import StarGiftCollections
    from .unique_star_gift_value_info import UniqueStarGiftValueInfo
    from .check_can_send_gift_result_ok import CheckCanSendGiftResultOk
    from .check_can_send_gift_result_fail import CheckCanSendGiftResultFail
    from .star_gift_auction_state import StarGiftAuctionState
    from .star_gift_auction_acquired_gifts import StarGiftAuctionAcquiredGifts
    from .star_gift_active_auctions_not_modified import StarGiftActiveAuctionsNotModified
    from .star_gift_active_auctions import StarGiftActiveAuctions
    from .star_gift_upgrade_attributes import StarGiftUpgradeAttributes
