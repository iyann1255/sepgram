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
    "ResPQ": "res_pq",
    "PQInnerData": "pq_inner_data",
    "BindAuthKeyInner": "bind_auth_key_inner",
    "ServerDHParams": "server_dh_params",
    "ServerDHInnerData": "server_dh_inner_data",
    "ClientDHInnerData": "client_dh_inner_data",
    "SetClientDHParamsAnswer": "set_client_dh_params_answer",
    "DestroyAuthKeyRes": "destroy_auth_key_res",
    "MsgsAck": "msgs_ack",
    "BadMsgNotification": "bad_msg_notification",
    "MsgsStateReq": "msgs_state_req",
    "MsgsStateInfo": "msgs_state_info",
    "MsgsAllInfo": "msgs_all_info",
    "MsgDetailedInfo": "msg_detailed_info",
    "MsgResendReq": "msg_resend_req",
    "RpcResult": "rpc_result",
    "RpcError": "rpc_error",
    "RpcDropAnswer": "rpc_drop_answer",
    "Pong": "pong",
    "DestroySessionRes": "destroy_session_res",
    "NewSession": "new_session",
    "HttpWait": "http_wait",
    "IpPort": "ip_port",
    "AccessPointRule": "access_point_rule",
    "InputPeer": "input_peer",
    "InputUser": "input_user",
    "InputContact": "input_contact",
    "InputFile": "input_file",
    "InputMedia": "input_media",
    "InputChatPhoto": "input_chat_photo",
    "InputGeoPoint": "input_geo_point",
    "InputPhoto": "input_photo",
    "InputFileLocation": "input_file_location",
    "Peer": "peer",
    "User": "user",
    "UserProfilePhoto": "user_profile_photo",
    "UserStatus": "user_status",
    "Chat": "chat",
    "ChatFull": "chat_full",
    "ChatParticipant": "chat_participant",
    "ChatParticipants": "chat_participants",
    "ChatPhoto": "chat_photo",
    "Message": "message",
    "MessageMedia": "message_media",
    "MessageAction": "message_action",
    "Dialog": "dialog",
    "Photo": "photo",
    "PhotoSize": "photo_size",
    "GeoPoint": "geo_point",
    "InputNotifyPeer": "input_notify_peer",
    "InputPeerNotifySettings": "input_peer_notify_settings",
    "PeerNotifySettings": "peer_notify_settings",
    "PeerSettings": "peer_settings",
    "WallPaper": "wall_paper",
    "ReportReason": "report_reason",
    "UserFull": "user_full",
    "Contact": "contact",
    "ImportedContact": "imported_contact",
    "ContactStatus": "contact_status",
    "MessagesFilter": "messages_filter",
    "Update": "update",
    "Updates": "updates_t",
    "DcOption": "dc_option",
    "Config": "config",
    "NearestDc": "nearest_dc",
    "EncryptedChat": "encrypted_chat",
    "InputEncryptedChat": "input_encrypted_chat",
    "EncryptedFile": "encrypted_file",
    "InputEncryptedFile": "input_encrypted_file",
    "EncryptedMessage": "encrypted_message",
    "InputDocument": "input_document",
    "Document": "document",
    "NotifyPeer": "notify_peer",
    "SendMessageAction": "send_message_action",
    "InputPrivacyKey": "input_privacy_key",
    "PrivacyKey": "privacy_key",
    "InputPrivacyRule": "input_privacy_rule",
    "PrivacyRule": "privacy_rule",
    "AccountDaysTTL": "account_days_ttl",
    "DocumentAttribute": "document_attribute",
    "StickerPack": "sticker_pack",
    "WebPage": "web_page",
    "Authorization": "authorization",
    "ReceivedNotifyMessage": "received_notify_message",
    "ExportedChatInvite": "exported_chat_invite",
    "ChatInvite": "chat_invite",
    "InputStickerSet": "input_sticker_set",
    "StickerSet": "sticker_set",
    "BotCommand": "bot_command",
    "BotInfo": "bot_info",
    "KeyboardButton": "keyboard_button",
    "KeyboardButtonRow": "keyboard_button_row",
    "ReplyMarkup": "reply_markup",
    "MessageEntity": "message_entity",
    "InputChannel": "input_channel",
    "MessageRange": "message_range",
    "ChannelMessagesFilter": "channel_messages_filter",
    "ChannelParticipant": "channel_participant",
    "ChannelParticipantsFilter": "channel_participants_filter",
    "InputBotInlineMessage": "input_bot_inline_message",
    "InputBotInlineResult": "input_bot_inline_result",
    "BotInlineMessage": "bot_inline_message",
    "BotInlineResult": "bot_inline_result",
    "ExportedMessageLink": "exported_message_link",
    "MessageFwdHeader": "message_fwd_header",
    "InputBotInlineMessageID": "input_bot_inline_message_id",
    "InlineBotSwitchPM": "inline_bot_switch_pm",
    "TopPeer": "top_peer",
    "TopPeerCategory": "top_peer_category",
    "TopPeerCategoryPeers": "top_peer_category_peers",
    "DraftMessage": "draft_message",
    "StickerSetCovered": "sticker_set_covered",
    "MaskCoords": "mask_coords",
    "InputStickeredMedia": "input_stickered_media",
    "Game": "game",
    "InputGame": "input_game",
    "HighScore": "high_score",
    "RichText": "rich_text",
    "PageBlock": "page_block",
    "PhoneCallDiscardReason": "phone_call_discard_reason",
    "DataJSON": "data_json",
    "LabeledPrice": "labeled_price",
    "Invoice": "invoice",
    "PaymentCharge": "payment_charge",
    "PostAddress": "post_address",
    "PaymentRequestedInfo": "payment_requested_info",
    "PaymentSavedCredentials": "payment_saved_credentials",
    "WebDocument": "web_document",
    "InputWebDocument": "input_web_document",
    "InputWebFileLocation": "input_web_file_location",
    "InputPaymentCredentials": "input_payment_credentials",
    "ShippingOption": "shipping_option",
    "InputStickerSetItem": "input_sticker_set_item",
    "InputPhoneCall": "input_phone_call",
    "PhoneCall": "phone_call",
    "PhoneConnection": "phone_connection",
    "PhoneCallProtocol": "phone_call_protocol",
    "CdnPublicKey": "cdn_public_key",
    "CdnConfig": "cdn_config",
    "LangPackString": "lang_pack_string",
    "LangPackDifference": "lang_pack_difference",
    "LangPackLanguage": "lang_pack_language",
    "ChannelAdminLogEventAction": "channel_admin_log_event_action",
    "ChannelAdminLogEvent": "channel_admin_log_event",
    "ChannelAdminLogEventsFilter": "channel_admin_log_events_filter",
    "PopularContact": "popular_contact",
    "RecentMeUrl": "recent_me_url",
    "InputSingleMedia": "input_single_media",
    "WebAuthorization": "web_authorization",
    "InputMessage": "input_message",
    "InputDialogPeer": "input_dialog_peer",
    "DialogPeer": "dialog_peer",
    "FileHash": "file_hash",
    "InputClientProxy": "input_client_proxy",
    "InputSecureFile": "input_secure_file",
    "SecureFile": "secure_file",
    "SecureData": "secure_data",
    "SecurePlainData": "secure_plain_data",
    "SecureValueType": "secure_value_type",
    "SecureValue": "secure_value",
    "InputSecureValue": "input_secure_value",
    "SecureValueHash": "secure_value_hash",
    "SecureValueError": "secure_value_error",
    "SecureCredentialsEncrypted": "secure_credentials_encrypted",
    "SavedContact": "saved_contact",
    "PasswordKdfAlgo": "password_kdf_algo",
    "SecurePasswordKdfAlgo": "secure_password_kdf_algo",
    "SecureSecretSettings": "secure_secret_settings",
    "InputCheckPasswordSRP": "input_check_password_srp",
    "SecureRequiredType": "secure_required_type",
    "InputAppEvent": "input_app_event",
    "JSONObjectValue": "json_object_value",
    "JSONValue": "json_value",
    "PageTableCell": "page_table_cell",
    "PageTableRow": "page_table_row",
    "PageCaption": "page_caption",
    "PageListItem": "page_list_item",
    "PageListOrderedItem": "page_list_ordered_item",
    "PageRelatedArticle": "page_related_article",
    "Page": "page",
    "PollAnswer": "poll_answer",
    "Poll": "poll",
    "PollAnswerVoters": "poll_answer_voters",
    "PollResults": "poll_results",
    "ChatOnlines": "chat_onlines",
    "StatsURL": "stats_url",
    "ChatAdminRights": "chat_admin_rights",
    "ChatBannedRights": "chat_banned_rights",
    "InputWallPaper": "input_wall_paper",
    "CodeSettings": "code_settings",
    "WallPaperSettings": "wall_paper_settings",
    "AutoDownloadSettings": "auto_download_settings",
    "EmojiKeyword": "emoji_keyword",
    "EmojiKeywordsDifference": "emoji_keywords_difference",
    "EmojiURL": "emoji_url",
    "EmojiLanguage": "emoji_language",
    "Folder": "folder",
    "InputFolderPeer": "input_folder_peer",
    "FolderPeer": "folder_peer",
    "UrlAuthResult": "url_auth_result",
    "ChannelLocation": "channel_location",
    "PeerLocated": "peer_located",
    "RestrictionReason": "restriction_reason",
    "InputTheme": "input_theme",
    "Theme": "theme",
    "BaseTheme": "base_theme",
    "InputThemeSettings": "input_theme_settings",
    "ThemeSettings": "theme_settings",
    "WebPageAttribute": "web_page_attribute",
    "BankCardOpenUrl": "bank_card_open_url",
    "DialogFilter": "dialog_filter",
    "DialogFilterSuggested": "dialog_filter_suggested",
    "StatsDateRangeDays": "stats_date_range_days",
    "StatsAbsValueAndPrev": "stats_abs_value_and_prev",
    "StatsPercentValue": "stats_percent_value",
    "StatsGraph": "stats_graph",
    "VideoSize": "video_size",
    "StatsGroupTopPoster": "stats_group_top_poster",
    "StatsGroupTopAdmin": "stats_group_top_admin",
    "StatsGroupTopInviter": "stats_group_top_inviter",
    "GlobalPrivacySettings": "global_privacy_settings",
    "MessageViews": "message_views",
    "MessageReplyHeader": "message_reply_header",
    "MessageReplies": "message_replies",
    "PeerBlocked": "peer_blocked",
    "GroupCall": "group_call",
    "InputGroupCall": "input_group_call",
    "GroupCallParticipant": "group_call_participant",
    "InlineQueryPeerType": "inline_query_peer_type",
    "ChatInviteImporter": "chat_invite_importer",
    "ChatAdminWithInvites": "chat_admin_with_invites",
    "GroupCallParticipantVideoSourceGroup": "group_call_participant_video_source_group",
    "GroupCallParticipantVideo": "group_call_participant_video",
    "BotCommandScope": "bot_command_scope",
    "ChatTheme": "chat_theme",
    "SponsoredMessage": "sponsored_message",
    "SearchResultsCalendarPeriod": "search_results_calendar_period",
    "SearchResultsPosition": "search_results_position",
    "ReactionCount": "reaction_count",
    "MessageReactions": "message_reactions",
    "AvailableReaction": "available_reaction",
    "MessagePeerReaction": "message_peer_reaction",
    "GroupCallStreamChannel": "group_call_stream_channel",
    "AttachMenuBotIconColor": "attach_menu_bot_icon_color",
    "AttachMenuBotIcon": "attach_menu_bot_icon",
    "AttachMenuBot": "attach_menu_bot",
    "AttachMenuBots": "attach_menu_bots",
    "AttachMenuBotsBot": "attach_menu_bots_bot",
    "WebViewResult": "web_view_result",
    "WebViewMessageSent": "web_view_message_sent",
    "BotMenuButton": "bot_menu_button",
    "NotificationSound": "notification_sound",
    "AttachMenuPeerType": "attach_menu_peer_type",
    "InputInvoice": "input_invoice",
    "InputStorePaymentPurpose": "input_store_payment_purpose",
    "PaymentFormMethod": "payment_form_method",
    "EmojiStatus": "emoji_status",
    "Reaction": "reaction",
    "ChatReactions": "chat_reactions",
    "EmailVerifyPurpose": "email_verify_purpose",
    "EmailVerification": "email_verification",
    "PremiumSubscriptionOption": "premium_subscription_option",
    "SendAsPeer": "send_as_peer",
    "MessageExtendedMedia": "message_extended_media",
    "StickerKeyword": "sticker_keyword",
    "Username": "username",
    "ForumTopic": "forum_topic",
    "DefaultHistoryTTL": "default_history_ttl",
    "ExportedContactToken": "exported_contact_token",
    "RequestPeerType": "request_peer_type",
    "EmojiList": "emoji_list",
    "EmojiGroup": "emoji_group",
    "TextWithEntities": "text_with_entities",
    "AutoSaveSettings": "auto_save_settings",
    "AutoSaveException": "auto_save_exception",
    "InputBotApp": "input_bot_app",
    "BotApp": "bot_app",
    "InlineBotWebView": "inline_bot_web_view",
    "ReadParticipantDate": "read_participant_date",
    "InputChatlist": "input_chatlist",
    "ExportedChatlistInvite": "exported_chatlist_invite",
    "MessagePeerVote": "message_peer_vote",
    "StoryViews": "story_views",
    "StoryItem": "story_item",
    "StoryView": "story_view",
    "InputReplyTo": "input_reply_to",
    "ExportedStoryLink": "exported_story_link",
    "StoriesStealthMode": "stories_stealth_mode",
    "MediaAreaCoordinates": "media_area_coordinates",
    "MediaArea": "media_area",
    "PeerStories": "peer_stories",
    "PremiumGiftCodeOption": "premium_gift_code_option",
    "PrepaidGiveaway": "prepaid_giveaway",
    "Boost": "boost",
    "MyBoost": "my_boost",
    "StoryFwdHeader": "story_fwd_header",
    "PostInteractionCounters": "post_interaction_counters",
    "PublicForward": "public_forward",
    "PeerColor": "peer_color",
    "StoryReaction": "story_reaction",
    "SavedDialog": "saved_dialog",
    "SavedReactionTag": "saved_reaction_tag",
    "OutboxReadDate": "outbox_read_date",
    "SmsJob": "sms_job",
    "BusinessWeeklyOpen": "business_weekly_open",
    "BusinessWorkHours": "business_work_hours",
    "BusinessLocation": "business_location",
    "InputBusinessRecipients": "input_business_recipients",
    "BusinessRecipients": "business_recipients",
    "BusinessAwayMessageSchedule": "business_away_message_schedule",
    "InputBusinessGreetingMessage": "input_business_greeting_message",
    "BusinessGreetingMessage": "business_greeting_message",
    "InputBusinessAwayMessage": "input_business_away_message",
    "BusinessAwayMessage": "business_away_message",
    "Timezone": "timezone",
    "QuickReply": "quick_reply",
    "InputQuickReplyShortcut": "input_quick_reply_shortcut",
    "ConnectedBot": "connected_bot",
    "Birthday": "birthday",
    "BotBusinessConnection": "bot_business_connection",
    "InputBusinessIntro": "input_business_intro",
    "BusinessIntro": "business_intro",
    "InputCollectible": "input_collectible",
    "InputBusinessBotRecipients": "input_business_bot_recipients",
    "BusinessBotRecipients": "business_bot_recipients",
    "ContactBirthday": "contact_birthday",
    "MissingInvitee": "missing_invitee",
    "InputBusinessChatLink": "input_business_chat_link",
    "BusinessChatLink": "business_chat_link",
    "RequestedPeer": "requested_peer",
    "SponsoredMessageReportOption": "sponsored_message_report_option",
    "ReactionNotificationsFrom": "reaction_notifications_from",
    "ReactionsNotifySettings": "reactions_notify_settings",
    "AvailableEffect": "available_effect",
    "FactCheck": "fact_check",
    "StarsTransactionPeer": "stars_transaction_peer",
    "StarsTopupOption": "stars_topup_option",
    "StarsTransaction": "stars_transaction",
    "FoundStory": "found_story",
    "GeoPointAddress": "geo_point_address",
    "StarsRevenueStatus": "stars_revenue_status",
    "InputStarsTransaction": "input_stars_transaction",
    "StarsGiftOption": "stars_gift_option",
    "BotPreviewMedia": "bot_preview_media",
    "StarsSubscriptionPricing": "stars_subscription_pricing",
    "StarsSubscription": "stars_subscription",
    "MessageReactor": "message_reactor",
    "StarsGiveawayOption": "stars_giveaway_option",
    "StarsGiveawayWinnersOption": "stars_giveaway_winners_option",
    "StarGift": "star_gift",
    "MessageReportOption": "message_report_option",
    "ReportResult": "report_result",
    "BotAppSettings": "bot_app_settings",
    "StarRefProgram": "star_ref_program",
    "ConnectedBotStarRef": "connected_bot_star_ref",
    "StarsAmount": "stars_amount",
    "BotVerifierSettings": "bot_verifier_settings",
    "BotVerification": "bot_verification",
    "StarGiftAttribute": "star_gift_attribute",
    "SavedStarGift": "saved_star_gift",
    "InputSavedStarGift": "input_saved_star_gift",
    "PaidReactionPrivacy": "paid_reaction_privacy",
    "RequirementToContact": "requirement_to_contact",
    "BusinessBotRights": "business_bot_rights",
    "DisallowedGiftsSettings": "disallowed_gifts_settings",
    "SponsoredPeer": "sponsored_peer",
    "StarGiftAttributeId": "star_gift_attribute_id",
    "StarGiftAttributeCounter": "star_gift_attribute_counter",
    "PendingSuggestion": "pending_suggestion",
    "TodoItem": "todo_item",
    "TodoList": "todo_list",
    "TodoCompletion": "todo_completion",
    "SuggestedPost": "suggested_post",
    "StarsRating": "stars_rating",
    "StarGiftCollection": "star_gift_collection",
    "StoryAlbum": "story_album",
    "SearchPostsFlood": "search_posts_flood",
    "ProfileTab": "profile_tab",
    "InputChatTheme": "input_chat_theme",
    "StarGiftUpgradePrice": "star_gift_upgrade_price",
    "GroupCallMessage": "group_call_message",
    "GroupCallDonor": "group_call_donor",
    "RecentStory": "recent_story",
    "AuctionBidLevel": "auction_bid_level",
    "StarGiftAuctionState": "star_gift_auction_state",
    "StarGiftAuctionUserState": "star_gift_auction_user_state",
    "StarGiftAuctionAcquiredGift": "star_gift_auction_acquired_gift",
    "StarGiftActiveAuctionState": "star_gift_active_auction_state",
    "InputStarGiftAuction": "input_star_gift_auction",
    "Passkey": "passkey",
    "InputPasskeyResponse": "input_passkey_response",
    "InputPasskeyCredential": "input_passkey_credential",
    "StarGiftBackground": "star_gift_background",
    "StarGiftAuctionRound": "star_gift_auction_round",
    "StarGiftAttributeRarity": "star_gift_attribute_rarity",
    "KeyboardButtonStyle": "keyboard_button_style",
    "InputMessageReadMetric": "input_message_read_metric",
    "InputAiComposeTone": "input_ai_compose_tone",
    "AiComposeTone": "ai_compose_tone",
    "AiComposeToneExample": "ai_compose_tone_example",
}

_SUBMODULES = frozenset((
    "help",
    "storage",
    "auth",
    "contacts",
    "messages",
    "updates",
    "photos",
    "upload",
    "account",
    "channels",
    "payments",
    "phone",
    "stats",
    "stickers",
    "users",
    "chatlists",
    "bots",
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
    from .res_pq import ResPQ
    from .pq_inner_data import PQInnerData
    from .bind_auth_key_inner import BindAuthKeyInner
    from .server_dh_params import ServerDHParams
    from .server_dh_inner_data import ServerDHInnerData
    from .client_dh_inner_data import ClientDHInnerData
    from .set_client_dh_params_answer import SetClientDHParamsAnswer
    from .destroy_auth_key_res import DestroyAuthKeyRes
    from .msgs_ack import MsgsAck
    from .bad_msg_notification import BadMsgNotification
    from .msgs_state_req import MsgsStateReq
    from .msgs_state_info import MsgsStateInfo
    from .msgs_all_info import MsgsAllInfo
    from .msg_detailed_info import MsgDetailedInfo
    from .msg_resend_req import MsgResendReq
    from .rpc_result import RpcResult
    from .rpc_error import RpcError
    from .rpc_drop_answer import RpcDropAnswer
    from .pong import Pong
    from .destroy_session_res import DestroySessionRes
    from .new_session import NewSession
    from .http_wait import HttpWait
    from .ip_port import IpPort
    from .access_point_rule import AccessPointRule
    from .input_peer import InputPeer
    from .input_user import InputUser
    from .input_contact import InputContact
    from .input_file import InputFile
    from .input_media import InputMedia
    from .input_chat_photo import InputChatPhoto
    from .input_geo_point import InputGeoPoint
    from .input_photo import InputPhoto
    from .input_file_location import InputFileLocation
    from .peer import Peer
    from .user import User
    from .user_profile_photo import UserProfilePhoto
    from .user_status import UserStatus
    from .chat import Chat
    from .chat_full import ChatFull
    from .chat_participant import ChatParticipant
    from .chat_participants import ChatParticipants
    from .chat_photo import ChatPhoto
    from .message import Message
    from .message_media import MessageMedia
    from .message_action import MessageAction
    from .dialog import Dialog
    from .photo import Photo
    from .photo_size import PhotoSize
    from .geo_point import GeoPoint
    from .input_notify_peer import InputNotifyPeer
    from .input_peer_notify_settings import InputPeerNotifySettings
    from .peer_notify_settings import PeerNotifySettings
    from .peer_settings import PeerSettings
    from .wall_paper import WallPaper
    from .report_reason import ReportReason
    from .user_full import UserFull
    from .contact import Contact
    from .imported_contact import ImportedContact
    from .contact_status import ContactStatus
    from .messages_filter import MessagesFilter
    from .update import Update
    from .updates_t import Updates
    from .dc_option import DcOption
    from .config import Config
    from .nearest_dc import NearestDc
    from .encrypted_chat import EncryptedChat
    from .input_encrypted_chat import InputEncryptedChat
    from .encrypted_file import EncryptedFile
    from .input_encrypted_file import InputEncryptedFile
    from .encrypted_message import EncryptedMessage
    from .input_document import InputDocument
    from .document import Document
    from .notify_peer import NotifyPeer
    from .send_message_action import SendMessageAction
    from .input_privacy_key import InputPrivacyKey
    from .privacy_key import PrivacyKey
    from .input_privacy_rule import InputPrivacyRule
    from .privacy_rule import PrivacyRule
    from .account_days_ttl import AccountDaysTTL
    from .document_attribute import DocumentAttribute
    from .sticker_pack import StickerPack
    from .web_page import WebPage
    from .authorization import Authorization
    from .received_notify_message import ReceivedNotifyMessage
    from .exported_chat_invite import ExportedChatInvite
    from .chat_invite import ChatInvite
    from .input_sticker_set import InputStickerSet
    from .sticker_set import StickerSet
    from .bot_command import BotCommand
    from .bot_info import BotInfo
    from .keyboard_button import KeyboardButton
    from .keyboard_button_row import KeyboardButtonRow
    from .reply_markup import ReplyMarkup
    from .message_entity import MessageEntity
    from .input_channel import InputChannel
    from .message_range import MessageRange
    from .channel_messages_filter import ChannelMessagesFilter
    from .channel_participant import ChannelParticipant
    from .channel_participants_filter import ChannelParticipantsFilter
    from .input_bot_inline_message import InputBotInlineMessage
    from .input_bot_inline_result import InputBotInlineResult
    from .bot_inline_message import BotInlineMessage
    from .bot_inline_result import BotInlineResult
    from .exported_message_link import ExportedMessageLink
    from .message_fwd_header import MessageFwdHeader
    from .input_bot_inline_message_id import InputBotInlineMessageID
    from .inline_bot_switch_pm import InlineBotSwitchPM
    from .top_peer import TopPeer
    from .top_peer_category import TopPeerCategory
    from .top_peer_category_peers import TopPeerCategoryPeers
    from .draft_message import DraftMessage
    from .sticker_set_covered import StickerSetCovered
    from .mask_coords import MaskCoords
    from .input_stickered_media import InputStickeredMedia
    from .game import Game
    from .input_game import InputGame
    from .high_score import HighScore
    from .rich_text import RichText
    from .page_block import PageBlock
    from .phone_call_discard_reason import PhoneCallDiscardReason
    from .data_json import DataJSON
    from .labeled_price import LabeledPrice
    from .invoice import Invoice
    from .payment_charge import PaymentCharge
    from .post_address import PostAddress
    from .payment_requested_info import PaymentRequestedInfo
    from .payment_saved_credentials import PaymentSavedCredentials
    from .web_document import WebDocument
    from .input_web_document import InputWebDocument
    from .input_web_file_location import InputWebFileLocation
    from .input_payment_credentials import InputPaymentCredentials
    from .shipping_option import ShippingOption
    from .input_sticker_set_item import InputStickerSetItem
    from .input_phone_call import InputPhoneCall
    from .phone_call import PhoneCall
    from .phone_connection import PhoneConnection
    from .phone_call_protocol import PhoneCallProtocol
    from .cdn_public_key import CdnPublicKey
    from .cdn_config import CdnConfig
    from .lang_pack_string import LangPackString
    from .lang_pack_difference import LangPackDifference
    from .lang_pack_language import LangPackLanguage
    from .channel_admin_log_event_action import ChannelAdminLogEventAction
    from .channel_admin_log_event import ChannelAdminLogEvent
    from .channel_admin_log_events_filter import ChannelAdminLogEventsFilter
    from .popular_contact import PopularContact
    from .recent_me_url import RecentMeUrl
    from .input_single_media import InputSingleMedia
    from .web_authorization import WebAuthorization
    from .input_message import InputMessage
    from .input_dialog_peer import InputDialogPeer
    from .dialog_peer import DialogPeer
    from .file_hash import FileHash
    from .input_client_proxy import InputClientProxy
    from .input_secure_file import InputSecureFile
    from .secure_file import SecureFile
    from .secure_data import SecureData
    from .secure_plain_data import SecurePlainData
    from .secure_value_type import SecureValueType
    from .secure_value import SecureValue
    from .input_secure_value import InputSecureValue
    from .secure_value_hash import SecureValueHash
    from .secure_value_error import SecureValueError
    from .secure_credentials_encrypted import SecureCredentialsEncrypted
    from .saved_contact import SavedContact
    from .password_kdf_algo import PasswordKdfAlgo
    from .secure_password_kdf_algo import SecurePasswordKdfAlgo
    from .secure_secret_settings import SecureSecretSettings
    from .input_check_password_srp import InputCheckPasswordSRP
    from .secure_required_type import SecureRequiredType
    from .input_app_event import InputAppEvent
    from .json_object_value import JSONObjectValue
    from .json_value import JSONValue
    from .page_table_cell import PageTableCell
    from .page_table_row import PageTableRow
    from .page_caption import PageCaption
    from .page_list_item import PageListItem
    from .page_list_ordered_item import PageListOrderedItem
    from .page_related_article import PageRelatedArticle
    from .page import Page
    from .poll_answer import PollAnswer
    from .poll import Poll
    from .poll_answer_voters import PollAnswerVoters
    from .poll_results import PollResults
    from .chat_onlines import ChatOnlines
    from .stats_url import StatsURL
    from .chat_admin_rights import ChatAdminRights
    from .chat_banned_rights import ChatBannedRights
    from .input_wall_paper import InputWallPaper
    from .code_settings import CodeSettings
    from .wall_paper_settings import WallPaperSettings
    from .auto_download_settings import AutoDownloadSettings
    from .emoji_keyword import EmojiKeyword
    from .emoji_keywords_difference import EmojiKeywordsDifference
    from .emoji_url import EmojiURL
    from .emoji_language import EmojiLanguage
    from .folder import Folder
    from .input_folder_peer import InputFolderPeer
    from .folder_peer import FolderPeer
    from .url_auth_result import UrlAuthResult
    from .channel_location import ChannelLocation
    from .peer_located import PeerLocated
    from .restriction_reason import RestrictionReason
    from .input_theme import InputTheme
    from .theme import Theme
    from .base_theme import BaseTheme
    from .input_theme_settings import InputThemeSettings
    from .theme_settings import ThemeSettings
    from .web_page_attribute import WebPageAttribute
    from .bank_card_open_url import BankCardOpenUrl
    from .dialog_filter import DialogFilter
    from .dialog_filter_suggested import DialogFilterSuggested
    from .stats_date_range_days import StatsDateRangeDays
    from .stats_abs_value_and_prev import StatsAbsValueAndPrev
    from .stats_percent_value import StatsPercentValue
    from .stats_graph import StatsGraph
    from .video_size import VideoSize
    from .stats_group_top_poster import StatsGroupTopPoster
    from .stats_group_top_admin import StatsGroupTopAdmin
    from .stats_group_top_inviter import StatsGroupTopInviter
    from .global_privacy_settings import GlobalPrivacySettings
    from .message_views import MessageViews
    from .message_reply_header import MessageReplyHeader
    from .message_replies import MessageReplies
    from .peer_blocked import PeerBlocked
    from .group_call import GroupCall
    from .input_group_call import InputGroupCall
    from .group_call_participant import GroupCallParticipant
    from .inline_query_peer_type import InlineQueryPeerType
    from .chat_invite_importer import ChatInviteImporter
    from .chat_admin_with_invites import ChatAdminWithInvites
    from .group_call_participant_video_source_group import GroupCallParticipantVideoSourceGroup
    from .group_call_participant_video import GroupCallParticipantVideo
    from .bot_command_scope import BotCommandScope
    from .chat_theme import ChatTheme
    from .sponsored_message import SponsoredMessage
    from .search_results_calendar_period import SearchResultsCalendarPeriod
    from .search_results_position import SearchResultsPosition
    from .reaction_count import ReactionCount
    from .message_reactions import MessageReactions
    from .available_reaction import AvailableReaction
    from .message_peer_reaction import MessagePeerReaction
    from .group_call_stream_channel import GroupCallStreamChannel
    from .attach_menu_bot_icon_color import AttachMenuBotIconColor
    from .attach_menu_bot_icon import AttachMenuBotIcon
    from .attach_menu_bot import AttachMenuBot
    from .attach_menu_bots import AttachMenuBots
    from .attach_menu_bots_bot import AttachMenuBotsBot
    from .web_view_result import WebViewResult
    from .web_view_message_sent import WebViewMessageSent
    from .bot_menu_button import BotMenuButton
    from .notification_sound import NotificationSound
    from .attach_menu_peer_type import AttachMenuPeerType
    from .input_invoice import InputInvoice
    from .input_store_payment_purpose import InputStorePaymentPurpose
    from .payment_form_method import PaymentFormMethod
    from .emoji_status import EmojiStatus
    from .reaction import Reaction
    from .chat_reactions import ChatReactions
    from .email_verify_purpose import EmailVerifyPurpose
    from .email_verification import EmailVerification
    from .premium_subscription_option import PremiumSubscriptionOption
    from .send_as_peer import SendAsPeer
    from .message_extended_media import MessageExtendedMedia
    from .sticker_keyword import StickerKeyword
    from .username import Username
    from .forum_topic import ForumTopic
    from .default_history_ttl import DefaultHistoryTTL
    from .exported_contact_token import ExportedContactToken
    from .request_peer_type import RequestPeerType
    from .emoji_list import EmojiList
    from .emoji_group import EmojiGroup
    from .text_with_entities import TextWithEntities
    from .auto_save_settings import AutoSaveSettings
    from .auto_save_exception import AutoSaveException
    from .input_bot_app import InputBotApp
    from .bot_app import BotApp
    from .inline_bot_web_view import InlineBotWebView
    from .read_participant_date import ReadParticipantDate
    from .input_chatlist import InputChatlist
    from .exported_chatlist_invite import ExportedChatlistInvite
    from .message_peer_vote import MessagePeerVote
    from .story_views import StoryViews
    from .story_item import StoryItem
    from .story_view import StoryView
    from .input_reply_to import InputReplyTo
    from .exported_story_link import ExportedStoryLink
    from .stories_stealth_mode import StoriesStealthMode
    from .media_area_coordinates import MediaAreaCoordinates
    from .media_area import MediaArea
    from .peer_stories import PeerStories
    from .premium_gift_code_option import PremiumGiftCodeOption
    from .prepaid_giveaway import PrepaidGiveaway
    from .boost import Boost
    from .my_boost import MyBoost
    from .story_fwd_header import StoryFwdHeader
    from .post_interaction_counters import PostInteractionCounters
    from .public_forward import PublicForward
    from .peer_color import PeerColor
    from .story_reaction import StoryReaction
    from .saved_dialog import SavedDialog
    from .saved_reaction_tag import SavedReactionTag
    from .outbox_read_date import OutboxReadDate
    from .sms_job import SmsJob
    from .business_weekly_open import BusinessWeeklyOpen
    from .business_work_hours import BusinessWorkHours
    from .business_location import BusinessLocation
    from .input_business_recipients import InputBusinessRecipients
    from .business_recipients import BusinessRecipients
    from .business_away_message_schedule import BusinessAwayMessageSchedule
    from .input_business_greeting_message import InputBusinessGreetingMessage
    from .business_greeting_message import BusinessGreetingMessage
    from .input_business_away_message import InputBusinessAwayMessage
    from .business_away_message import BusinessAwayMessage
    from .timezone import Timezone
    from .quick_reply import QuickReply
    from .input_quick_reply_shortcut import InputQuickReplyShortcut
    from .connected_bot import ConnectedBot
    from .birthday import Birthday
    from .bot_business_connection import BotBusinessConnection
    from .input_business_intro import InputBusinessIntro
    from .business_intro import BusinessIntro
    from .input_collectible import InputCollectible
    from .input_business_bot_recipients import InputBusinessBotRecipients
    from .business_bot_recipients import BusinessBotRecipients
    from .contact_birthday import ContactBirthday
    from .missing_invitee import MissingInvitee
    from .input_business_chat_link import InputBusinessChatLink
    from .business_chat_link import BusinessChatLink
    from .requested_peer import RequestedPeer
    from .sponsored_message_report_option import SponsoredMessageReportOption
    from .reaction_notifications_from import ReactionNotificationsFrom
    from .reactions_notify_settings import ReactionsNotifySettings
    from .available_effect import AvailableEffect
    from .fact_check import FactCheck
    from .stars_transaction_peer import StarsTransactionPeer
    from .stars_topup_option import StarsTopupOption
    from .stars_transaction import StarsTransaction
    from .found_story import FoundStory
    from .geo_point_address import GeoPointAddress
    from .stars_revenue_status import StarsRevenueStatus
    from .input_stars_transaction import InputStarsTransaction
    from .stars_gift_option import StarsGiftOption
    from .bot_preview_media import BotPreviewMedia
    from .stars_subscription_pricing import StarsSubscriptionPricing
    from .stars_subscription import StarsSubscription
    from .message_reactor import MessageReactor
    from .stars_giveaway_option import StarsGiveawayOption
    from .stars_giveaway_winners_option import StarsGiveawayWinnersOption
    from .star_gift import StarGift
    from .message_report_option import MessageReportOption
    from .report_result import ReportResult
    from .bot_app_settings import BotAppSettings
    from .star_ref_program import StarRefProgram
    from .connected_bot_star_ref import ConnectedBotStarRef
    from .stars_amount import StarsAmount
    from .bot_verifier_settings import BotVerifierSettings
    from .bot_verification import BotVerification
    from .star_gift_attribute import StarGiftAttribute
    from .saved_star_gift import SavedStarGift
    from .input_saved_star_gift import InputSavedStarGift
    from .paid_reaction_privacy import PaidReactionPrivacy
    from .requirement_to_contact import RequirementToContact
    from .business_bot_rights import BusinessBotRights
    from .disallowed_gifts_settings import DisallowedGiftsSettings
    from .sponsored_peer import SponsoredPeer
    from .star_gift_attribute_id import StarGiftAttributeId
    from .star_gift_attribute_counter import StarGiftAttributeCounter
    from .pending_suggestion import PendingSuggestion
    from .todo_item import TodoItem
    from .todo_list import TodoList
    from .todo_completion import TodoCompletion
    from .suggested_post import SuggestedPost
    from .stars_rating import StarsRating
    from .star_gift_collection import StarGiftCollection
    from .story_album import StoryAlbum
    from .search_posts_flood import SearchPostsFlood
    from .profile_tab import ProfileTab
    from .input_chat_theme import InputChatTheme
    from .star_gift_upgrade_price import StarGiftUpgradePrice
    from .group_call_message import GroupCallMessage
    from .group_call_donor import GroupCallDonor
    from .recent_story import RecentStory
    from .auction_bid_level import AuctionBidLevel
    from .star_gift_auction_state import StarGiftAuctionState
    from .star_gift_auction_user_state import StarGiftAuctionUserState
    from .star_gift_auction_acquired_gift import StarGiftAuctionAcquiredGift
    from .star_gift_active_auction_state import StarGiftActiveAuctionState
    from .input_star_gift_auction import InputStarGiftAuction
    from .passkey import Passkey
    from .input_passkey_response import InputPasskeyResponse
    from .input_passkey_credential import InputPasskeyCredential
    from .star_gift_background import StarGiftBackground
    from .star_gift_auction_round import StarGiftAuctionRound
    from .star_gift_attribute_rarity import StarGiftAttributeRarity
    from .keyboard_button_style import KeyboardButtonStyle
    from .input_message_read_metric import InputMessageReadMetric
    from .input_ai_compose_tone import InputAiComposeTone
    from .ai_compose_tone import AiComposeTone
    from .ai_compose_tone_example import AiComposeToneExample
    from . import help
    from . import storage
    from . import auth
    from . import contacts
    from . import messages
    from . import updates
    from . import photos
    from . import upload
    from . import account
    from . import channels
    from . import payments
    from . import phone
    from . import stats
    from . import stickers
    from . import users
    from . import chatlists
    from . import bots
    from . import stories
    from . import premium
    from . import smsjobs
    from . import fragment
    from . import aicompose
