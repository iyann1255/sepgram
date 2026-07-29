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
    "GetMessages": "get_messages",
    "GetDialogs": "get_dialogs",
    "GetHistory": "get_history",
    "Search": "search",
    "ReadHistory": "read_history",
    "DeleteHistory": "delete_history",
    "DeleteMessages": "delete_messages",
    "ReceivedMessages": "received_messages",
    "SetTyping": "set_typing",
    "SendMessage": "send_message",
    "SendMedia": "send_media",
    "ForwardMessages": "forward_messages",
    "ReportSpam": "report_spam",
    "GetPeerSettings": "get_peer_settings",
    "Report": "report",
    "GetChats": "get_chats",
    "GetFullChat": "get_full_chat",
    "EditChatTitle": "edit_chat_title",
    "EditChatPhoto": "edit_chat_photo",
    "AddChatUser": "add_chat_user",
    "DeleteChatUser": "delete_chat_user",
    "CreateChat": "create_chat",
    "GetDhConfig": "get_dh_config",
    "RequestEncryption": "request_encryption",
    "AcceptEncryption": "accept_encryption",
    "DiscardEncryption": "discard_encryption",
    "SetEncryptedTyping": "set_encrypted_typing",
    "ReadEncryptedHistory": "read_encrypted_history",
    "SendEncrypted": "send_encrypted",
    "SendEncryptedFile": "send_encrypted_file",
    "SendEncryptedService": "send_encrypted_service",
    "ReceivedQueue": "received_queue",
    "ReportEncryptedSpam": "report_encrypted_spam",
    "ReadMessageContents": "read_message_contents",
    "GetStickers": "get_stickers",
    "GetAllStickers": "get_all_stickers",
    "GetWebPagePreview": "get_web_page_preview",
    "ExportChatInvite": "export_chat_invite",
    "CheckChatInvite": "check_chat_invite",
    "ImportChatInvite": "import_chat_invite",
    "GetStickerSet": "get_sticker_set",
    "InstallStickerSet": "install_sticker_set",
    "UninstallStickerSet": "uninstall_sticker_set",
    "StartBot": "start_bot",
    "GetMessagesViews": "get_messages_views",
    "EditChatAdmin": "edit_chat_admin",
    "MigrateChat": "migrate_chat",
    "SearchGlobal": "search_global",
    "ReorderStickerSets": "reorder_sticker_sets",
    "GetDocumentByHash": "get_document_by_hash",
    "GetSavedGifs": "get_saved_gifs",
    "SaveGif": "save_gif",
    "GetInlineBotResults": "get_inline_bot_results",
    "SetInlineBotResults": "set_inline_bot_results",
    "SendInlineBotResult": "send_inline_bot_result",
    "GetMessageEditData": "get_message_edit_data",
    "EditMessage": "edit_message",
    "EditInlineBotMessage": "edit_inline_bot_message",
    "GetBotCallbackAnswer": "get_bot_callback_answer",
    "SetBotCallbackAnswer": "set_bot_callback_answer",
    "GetPeerDialogs": "get_peer_dialogs",
    "SaveDraft": "save_draft",
    "GetAllDrafts": "get_all_drafts",
    "GetFeaturedStickers": "get_featured_stickers",
    "ReadFeaturedStickers": "read_featured_stickers",
    "GetRecentStickers": "get_recent_stickers",
    "SaveRecentSticker": "save_recent_sticker",
    "ClearRecentStickers": "clear_recent_stickers",
    "GetArchivedStickers": "get_archived_stickers",
    "GetMaskStickers": "get_mask_stickers",
    "GetAttachedStickers": "get_attached_stickers",
    "SetGameScore": "set_game_score",
    "SetInlineGameScore": "set_inline_game_score",
    "GetGameHighScores": "get_game_high_scores",
    "GetInlineGameHighScores": "get_inline_game_high_scores",
    "GetCommonChats": "get_common_chats",
    "GetWebPage": "get_web_page",
    "ToggleDialogPin": "toggle_dialog_pin",
    "ReorderPinnedDialogs": "reorder_pinned_dialogs",
    "GetPinnedDialogs": "get_pinned_dialogs",
    "SetBotShippingResults": "set_bot_shipping_results",
    "SetBotPrecheckoutResults": "set_bot_precheckout_results",
    "UploadMedia": "upload_media",
    "SendScreenshotNotification": "send_screenshot_notification",
    "GetFavedStickers": "get_faved_stickers",
    "FaveSticker": "fave_sticker",
    "GetUnreadMentions": "get_unread_mentions",
    "ReadMentions": "read_mentions",
    "GetRecentLocations": "get_recent_locations",
    "SendMultiMedia": "send_multi_media",
    "UploadEncryptedFile": "upload_encrypted_file",
    "SearchStickerSets": "search_sticker_sets",
    "GetSplitRanges": "get_split_ranges",
    "MarkDialogUnread": "mark_dialog_unread",
    "GetDialogUnreadMarks": "get_dialog_unread_marks",
    "ClearAllDrafts": "clear_all_drafts",
    "UpdatePinnedMessage": "update_pinned_message",
    "SendVote": "send_vote",
    "GetPollResults": "get_poll_results",
    "GetOnlines": "get_onlines",
    "EditChatAbout": "edit_chat_about",
    "EditChatDefaultBannedRights": "edit_chat_default_banned_rights",
    "GetEmojiKeywords": "get_emoji_keywords",
    "GetEmojiKeywordsDifference": "get_emoji_keywords_difference",
    "GetEmojiKeywordsLanguages": "get_emoji_keywords_languages",
    "GetEmojiURL": "get_emoji_url",
    "GetSearchCounters": "get_search_counters",
    "RequestUrlAuth": "request_url_auth",
    "AcceptUrlAuth": "accept_url_auth",
    "HidePeerSettingsBar": "hide_peer_settings_bar",
    "GetScheduledHistory": "get_scheduled_history",
    "GetScheduledMessages": "get_scheduled_messages",
    "SendScheduledMessages": "send_scheduled_messages",
    "DeleteScheduledMessages": "delete_scheduled_messages",
    "GetPollVotes": "get_poll_votes",
    "ToggleStickerSets": "toggle_sticker_sets",
    "GetDialogFilters": "get_dialog_filters",
    "GetSuggestedDialogFilters": "get_suggested_dialog_filters",
    "UpdateDialogFilter": "update_dialog_filter",
    "UpdateDialogFiltersOrder": "update_dialog_filters_order",
    "GetOldFeaturedStickers": "get_old_featured_stickers",
    "GetReplies": "get_replies",
    "GetDiscussionMessage": "get_discussion_message",
    "ReadDiscussion": "read_discussion",
    "UnpinAllMessages": "unpin_all_messages",
    "DeleteChat": "delete_chat",
    "DeletePhoneCallHistory": "delete_phone_call_history",
    "CheckHistoryImport": "check_history_import",
    "InitHistoryImport": "init_history_import",
    "UploadImportedMedia": "upload_imported_media",
    "StartHistoryImport": "start_history_import",
    "GetExportedChatInvites": "get_exported_chat_invites",
    "GetExportedChatInvite": "get_exported_chat_invite",
    "EditExportedChatInvite": "edit_exported_chat_invite",
    "DeleteRevokedExportedChatInvites": "delete_revoked_exported_chat_invites",
    "DeleteExportedChatInvite": "delete_exported_chat_invite",
    "GetAdminsWithInvites": "get_admins_with_invites",
    "GetChatInviteImporters": "get_chat_invite_importers",
    "SetHistoryTTL": "set_history_ttl",
    "CheckHistoryImportPeer": "check_history_import_peer",
    "SetChatTheme": "set_chat_theme",
    "GetMessageReadParticipants": "get_message_read_participants",
    "GetSearchResultsCalendar": "get_search_results_calendar",
    "GetSearchResultsPositions": "get_search_results_positions",
    "HideChatJoinRequest": "hide_chat_join_request",
    "HideAllChatJoinRequests": "hide_all_chat_join_requests",
    "ToggleNoForwards": "toggle_no_forwards",
    "SaveDefaultSendAs": "save_default_send_as",
    "SendReaction": "send_reaction",
    "GetMessagesReactions": "get_messages_reactions",
    "GetMessageReactionsList": "get_message_reactions_list",
    "SetChatAvailableReactions": "set_chat_available_reactions",
    "GetAvailableReactions": "get_available_reactions",
    "SetDefaultReaction": "set_default_reaction",
    "TranslateText": "translate_text",
    "GetUnreadReactions": "get_unread_reactions",
    "ReadReactions": "read_reactions",
    "SearchSentMedia": "search_sent_media",
    "GetAttachMenuBots": "get_attach_menu_bots",
    "GetAttachMenuBot": "get_attach_menu_bot",
    "ToggleBotInAttachMenu": "toggle_bot_in_attach_menu",
    "RequestWebView": "request_web_view",
    "ProlongWebView": "prolong_web_view",
    "RequestSimpleWebView": "request_simple_web_view",
    "SendWebViewResultMessage": "send_web_view_result_message",
    "SendWebViewData": "send_web_view_data",
    "TranscribeAudio": "transcribe_audio",
    "RateTranscribedAudio": "rate_transcribed_audio",
    "GetCustomEmojiDocuments": "get_custom_emoji_documents",
    "GetEmojiStickers": "get_emoji_stickers",
    "GetFeaturedEmojiStickers": "get_featured_emoji_stickers",
    "ReportReaction": "report_reaction",
    "GetTopReactions": "get_top_reactions",
    "GetRecentReactions": "get_recent_reactions",
    "ClearRecentReactions": "clear_recent_reactions",
    "GetExtendedMedia": "get_extended_media",
    "SetDefaultHistoryTTL": "set_default_history_ttl",
    "GetDefaultHistoryTTL": "get_default_history_ttl",
    "SendBotRequestedPeer": "send_bot_requested_peer",
    "GetEmojiGroups": "get_emoji_groups",
    "GetEmojiStatusGroups": "get_emoji_status_groups",
    "GetEmojiProfilePhotoGroups": "get_emoji_profile_photo_groups",
    "SearchCustomEmoji": "search_custom_emoji",
    "TogglePeerTranslations": "toggle_peer_translations",
    "GetBotApp": "get_bot_app",
    "RequestAppWebView": "request_app_web_view",
    "SetChatWallPaper": "set_chat_wall_paper",
    "SearchEmojiStickerSets": "search_emoji_sticker_sets",
    "GetSavedDialogs": "get_saved_dialogs",
    "GetSavedHistory": "get_saved_history",
    "DeleteSavedHistory": "delete_saved_history",
    "GetPinnedSavedDialogs": "get_pinned_saved_dialogs",
    "ToggleSavedDialogPin": "toggle_saved_dialog_pin",
    "ReorderPinnedSavedDialogs": "reorder_pinned_saved_dialogs",
    "GetSavedReactionTags": "get_saved_reaction_tags",
    "UpdateSavedReactionTag": "update_saved_reaction_tag",
    "GetDefaultTagReactions": "get_default_tag_reactions",
    "GetOutboxReadDate": "get_outbox_read_date",
    "GetQuickReplies": "get_quick_replies",
    "ReorderQuickReplies": "reorder_quick_replies",
    "CheckQuickReplyShortcut": "check_quick_reply_shortcut",
    "EditQuickReplyShortcut": "edit_quick_reply_shortcut",
    "DeleteQuickReplyShortcut": "delete_quick_reply_shortcut",
    "GetQuickReplyMessages": "get_quick_reply_messages",
    "SendQuickReplyMessages": "send_quick_reply_messages",
    "DeleteQuickReplyMessages": "delete_quick_reply_messages",
    "ToggleDialogFilterTags": "toggle_dialog_filter_tags",
    "GetMyStickers": "get_my_stickers",
    "GetEmojiStickerGroups": "get_emoji_sticker_groups",
    "GetAvailableEffects": "get_available_effects",
    "EditFactCheck": "edit_fact_check",
    "DeleteFactCheck": "delete_fact_check",
    "GetFactCheck": "get_fact_check",
    "RequestMainWebView": "request_main_web_view",
    "SendPaidReaction": "send_paid_reaction",
    "TogglePaidReactionPrivacy": "toggle_paid_reaction_privacy",
    "GetPaidReactionPrivacy": "get_paid_reaction_privacy",
    "ViewSponsoredMessage": "view_sponsored_message",
    "ClickSponsoredMessage": "click_sponsored_message",
    "ReportSponsoredMessage": "report_sponsored_message",
    "GetSponsoredMessages": "get_sponsored_messages",
    "SavePreparedInlineMessage": "save_prepared_inline_message",
    "GetPreparedInlineMessage": "get_prepared_inline_message",
    "SearchStickers": "search_stickers",
    "ReportMessagesDelivery": "report_messages_delivery",
    "GetSavedDialogsByID": "get_saved_dialogs_by_id",
    "ReadSavedHistory": "read_saved_history",
    "ToggleTodoCompleted": "toggle_todo_completed",
    "AppendTodoList": "append_todo_list",
    "ToggleSuggestedPostApproval": "toggle_suggested_post_approval",
    "GetForumTopics": "get_forum_topics",
    "GetForumTopicsByID": "get_forum_topics_by_id",
    "EditForumTopic": "edit_forum_topic",
    "UpdatePinnedForumTopic": "update_pinned_forum_topic",
    "ReorderPinnedForumTopics": "reorder_pinned_forum_topics",
    "CreateForumTopic": "create_forum_topic",
    "DeleteTopicHistory": "delete_topic_history",
    "GetEmojiGameInfo": "get_emoji_game_info",
    "SummarizeText": "summarize_text",
    "EditChatCreator": "edit_chat_creator",
    "GetFutureChatCreatorAfterLeave": "get_future_chat_creator_after_leave",
    "EditChatParticipantRank": "edit_chat_participant_rank",
    "DeclineUrlAuth": "decline_url_auth",
    "CheckUrlAuthMatchCode": "check_url_auth_match_code",
    "ComposeMessageWithAI": "compose_message_with_ai",
    "ReportReadMetrics": "report_read_metrics",
    "ReportMusicListen": "report_music_listen",
    "AddPollAnswer": "add_poll_answer",
    "DeletePollAnswer": "delete_poll_answer",
    "GetUnreadPollVotes": "get_unread_poll_votes",
    "ReadPollVotes": "read_poll_votes",
    "SetBotGuestChatResult": "set_bot_guest_chat_result",
    "DeleteParticipantReactions": "delete_participant_reactions",
    "DeleteParticipantReaction": "delete_participant_reaction",
    "GetPersonalChannelHistory": "get_personal_channel_history",
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
    from .get_messages import GetMessages
    from .get_dialogs import GetDialogs
    from .get_history import GetHistory
    from .search import Search
    from .read_history import ReadHistory
    from .delete_history import DeleteHistory
    from .delete_messages import DeleteMessages
    from .received_messages import ReceivedMessages
    from .set_typing import SetTyping
    from .send_message import SendMessage
    from .send_media import SendMedia
    from .forward_messages import ForwardMessages
    from .report_spam import ReportSpam
    from .get_peer_settings import GetPeerSettings
    from .report import Report
    from .get_chats import GetChats
    from .get_full_chat import GetFullChat
    from .edit_chat_title import EditChatTitle
    from .edit_chat_photo import EditChatPhoto
    from .add_chat_user import AddChatUser
    from .delete_chat_user import DeleteChatUser
    from .create_chat import CreateChat
    from .get_dh_config import GetDhConfig
    from .request_encryption import RequestEncryption
    from .accept_encryption import AcceptEncryption
    from .discard_encryption import DiscardEncryption
    from .set_encrypted_typing import SetEncryptedTyping
    from .read_encrypted_history import ReadEncryptedHistory
    from .send_encrypted import SendEncrypted
    from .send_encrypted_file import SendEncryptedFile
    from .send_encrypted_service import SendEncryptedService
    from .received_queue import ReceivedQueue
    from .report_encrypted_spam import ReportEncryptedSpam
    from .read_message_contents import ReadMessageContents
    from .get_stickers import GetStickers
    from .get_all_stickers import GetAllStickers
    from .get_web_page_preview import GetWebPagePreview
    from .export_chat_invite import ExportChatInvite
    from .check_chat_invite import CheckChatInvite
    from .import_chat_invite import ImportChatInvite
    from .get_sticker_set import GetStickerSet
    from .install_sticker_set import InstallStickerSet
    from .uninstall_sticker_set import UninstallStickerSet
    from .start_bot import StartBot
    from .get_messages_views import GetMessagesViews
    from .edit_chat_admin import EditChatAdmin
    from .migrate_chat import MigrateChat
    from .search_global import SearchGlobal
    from .reorder_sticker_sets import ReorderStickerSets
    from .get_document_by_hash import GetDocumentByHash
    from .get_saved_gifs import GetSavedGifs
    from .save_gif import SaveGif
    from .get_inline_bot_results import GetInlineBotResults
    from .set_inline_bot_results import SetInlineBotResults
    from .send_inline_bot_result import SendInlineBotResult
    from .get_message_edit_data import GetMessageEditData
    from .edit_message import EditMessage
    from .edit_inline_bot_message import EditInlineBotMessage
    from .get_bot_callback_answer import GetBotCallbackAnswer
    from .set_bot_callback_answer import SetBotCallbackAnswer
    from .get_peer_dialogs import GetPeerDialogs
    from .save_draft import SaveDraft
    from .get_all_drafts import GetAllDrafts
    from .get_featured_stickers import GetFeaturedStickers
    from .read_featured_stickers import ReadFeaturedStickers
    from .get_recent_stickers import GetRecentStickers
    from .save_recent_sticker import SaveRecentSticker
    from .clear_recent_stickers import ClearRecentStickers
    from .get_archived_stickers import GetArchivedStickers
    from .get_mask_stickers import GetMaskStickers
    from .get_attached_stickers import GetAttachedStickers
    from .set_game_score import SetGameScore
    from .set_inline_game_score import SetInlineGameScore
    from .get_game_high_scores import GetGameHighScores
    from .get_inline_game_high_scores import GetInlineGameHighScores
    from .get_common_chats import GetCommonChats
    from .get_web_page import GetWebPage
    from .toggle_dialog_pin import ToggleDialogPin
    from .reorder_pinned_dialogs import ReorderPinnedDialogs
    from .get_pinned_dialogs import GetPinnedDialogs
    from .set_bot_shipping_results import SetBotShippingResults
    from .set_bot_precheckout_results import SetBotPrecheckoutResults
    from .upload_media import UploadMedia
    from .send_screenshot_notification import SendScreenshotNotification
    from .get_faved_stickers import GetFavedStickers
    from .fave_sticker import FaveSticker
    from .get_unread_mentions import GetUnreadMentions
    from .read_mentions import ReadMentions
    from .get_recent_locations import GetRecentLocations
    from .send_multi_media import SendMultiMedia
    from .upload_encrypted_file import UploadEncryptedFile
    from .search_sticker_sets import SearchStickerSets
    from .get_split_ranges import GetSplitRanges
    from .mark_dialog_unread import MarkDialogUnread
    from .get_dialog_unread_marks import GetDialogUnreadMarks
    from .clear_all_drafts import ClearAllDrafts
    from .update_pinned_message import UpdatePinnedMessage
    from .send_vote import SendVote
    from .get_poll_results import GetPollResults
    from .get_onlines import GetOnlines
    from .edit_chat_about import EditChatAbout
    from .edit_chat_default_banned_rights import EditChatDefaultBannedRights
    from .get_emoji_keywords import GetEmojiKeywords
    from .get_emoji_keywords_difference import GetEmojiKeywordsDifference
    from .get_emoji_keywords_languages import GetEmojiKeywordsLanguages
    from .get_emoji_url import GetEmojiURL
    from .get_search_counters import GetSearchCounters
    from .request_url_auth import RequestUrlAuth
    from .accept_url_auth import AcceptUrlAuth
    from .hide_peer_settings_bar import HidePeerSettingsBar
    from .get_scheduled_history import GetScheduledHistory
    from .get_scheduled_messages import GetScheduledMessages
    from .send_scheduled_messages import SendScheduledMessages
    from .delete_scheduled_messages import DeleteScheduledMessages
    from .get_poll_votes import GetPollVotes
    from .toggle_sticker_sets import ToggleStickerSets
    from .get_dialog_filters import GetDialogFilters
    from .get_suggested_dialog_filters import GetSuggestedDialogFilters
    from .update_dialog_filter import UpdateDialogFilter
    from .update_dialog_filters_order import UpdateDialogFiltersOrder
    from .get_old_featured_stickers import GetOldFeaturedStickers
    from .get_replies import GetReplies
    from .get_discussion_message import GetDiscussionMessage
    from .read_discussion import ReadDiscussion
    from .unpin_all_messages import UnpinAllMessages
    from .delete_chat import DeleteChat
    from .delete_phone_call_history import DeletePhoneCallHistory
    from .check_history_import import CheckHistoryImport
    from .init_history_import import InitHistoryImport
    from .upload_imported_media import UploadImportedMedia
    from .start_history_import import StartHistoryImport
    from .get_exported_chat_invites import GetExportedChatInvites
    from .get_exported_chat_invite import GetExportedChatInvite
    from .edit_exported_chat_invite import EditExportedChatInvite
    from .delete_revoked_exported_chat_invites import DeleteRevokedExportedChatInvites
    from .delete_exported_chat_invite import DeleteExportedChatInvite
    from .get_admins_with_invites import GetAdminsWithInvites
    from .get_chat_invite_importers import GetChatInviteImporters
    from .set_history_ttl import SetHistoryTTL
    from .check_history_import_peer import CheckHistoryImportPeer
    from .set_chat_theme import SetChatTheme
    from .get_message_read_participants import GetMessageReadParticipants
    from .get_search_results_calendar import GetSearchResultsCalendar
    from .get_search_results_positions import GetSearchResultsPositions
    from .hide_chat_join_request import HideChatJoinRequest
    from .hide_all_chat_join_requests import HideAllChatJoinRequests
    from .toggle_no_forwards import ToggleNoForwards
    from .save_default_send_as import SaveDefaultSendAs
    from .send_reaction import SendReaction
    from .get_messages_reactions import GetMessagesReactions
    from .get_message_reactions_list import GetMessageReactionsList
    from .set_chat_available_reactions import SetChatAvailableReactions
    from .get_available_reactions import GetAvailableReactions
    from .set_default_reaction import SetDefaultReaction
    from .translate_text import TranslateText
    from .get_unread_reactions import GetUnreadReactions
    from .read_reactions import ReadReactions
    from .search_sent_media import SearchSentMedia
    from .get_attach_menu_bots import GetAttachMenuBots
    from .get_attach_menu_bot import GetAttachMenuBot
    from .toggle_bot_in_attach_menu import ToggleBotInAttachMenu
    from .request_web_view import RequestWebView
    from .prolong_web_view import ProlongWebView
    from .request_simple_web_view import RequestSimpleWebView
    from .send_web_view_result_message import SendWebViewResultMessage
    from .send_web_view_data import SendWebViewData
    from .transcribe_audio import TranscribeAudio
    from .rate_transcribed_audio import RateTranscribedAudio
    from .get_custom_emoji_documents import GetCustomEmojiDocuments
    from .get_emoji_stickers import GetEmojiStickers
    from .get_featured_emoji_stickers import GetFeaturedEmojiStickers
    from .report_reaction import ReportReaction
    from .get_top_reactions import GetTopReactions
    from .get_recent_reactions import GetRecentReactions
    from .clear_recent_reactions import ClearRecentReactions
    from .get_extended_media import GetExtendedMedia
    from .set_default_history_ttl import SetDefaultHistoryTTL
    from .get_default_history_ttl import GetDefaultHistoryTTL
    from .send_bot_requested_peer import SendBotRequestedPeer
    from .get_emoji_groups import GetEmojiGroups
    from .get_emoji_status_groups import GetEmojiStatusGroups
    from .get_emoji_profile_photo_groups import GetEmojiProfilePhotoGroups
    from .search_custom_emoji import SearchCustomEmoji
    from .toggle_peer_translations import TogglePeerTranslations
    from .get_bot_app import GetBotApp
    from .request_app_web_view import RequestAppWebView
    from .set_chat_wall_paper import SetChatWallPaper
    from .search_emoji_sticker_sets import SearchEmojiStickerSets
    from .get_saved_dialogs import GetSavedDialogs
    from .get_saved_history import GetSavedHistory
    from .delete_saved_history import DeleteSavedHistory
    from .get_pinned_saved_dialogs import GetPinnedSavedDialogs
    from .toggle_saved_dialog_pin import ToggleSavedDialogPin
    from .reorder_pinned_saved_dialogs import ReorderPinnedSavedDialogs
    from .get_saved_reaction_tags import GetSavedReactionTags
    from .update_saved_reaction_tag import UpdateSavedReactionTag
    from .get_default_tag_reactions import GetDefaultTagReactions
    from .get_outbox_read_date import GetOutboxReadDate
    from .get_quick_replies import GetQuickReplies
    from .reorder_quick_replies import ReorderQuickReplies
    from .check_quick_reply_shortcut import CheckQuickReplyShortcut
    from .edit_quick_reply_shortcut import EditQuickReplyShortcut
    from .delete_quick_reply_shortcut import DeleteQuickReplyShortcut
    from .get_quick_reply_messages import GetQuickReplyMessages
    from .send_quick_reply_messages import SendQuickReplyMessages
    from .delete_quick_reply_messages import DeleteQuickReplyMessages
    from .toggle_dialog_filter_tags import ToggleDialogFilterTags
    from .get_my_stickers import GetMyStickers
    from .get_emoji_sticker_groups import GetEmojiStickerGroups
    from .get_available_effects import GetAvailableEffects
    from .edit_fact_check import EditFactCheck
    from .delete_fact_check import DeleteFactCheck
    from .get_fact_check import GetFactCheck
    from .request_main_web_view import RequestMainWebView
    from .send_paid_reaction import SendPaidReaction
    from .toggle_paid_reaction_privacy import TogglePaidReactionPrivacy
    from .get_paid_reaction_privacy import GetPaidReactionPrivacy
    from .view_sponsored_message import ViewSponsoredMessage
    from .click_sponsored_message import ClickSponsoredMessage
    from .report_sponsored_message import ReportSponsoredMessage
    from .get_sponsored_messages import GetSponsoredMessages
    from .save_prepared_inline_message import SavePreparedInlineMessage
    from .get_prepared_inline_message import GetPreparedInlineMessage
    from .search_stickers import SearchStickers
    from .report_messages_delivery import ReportMessagesDelivery
    from .get_saved_dialogs_by_id import GetSavedDialogsByID
    from .read_saved_history import ReadSavedHistory
    from .toggle_todo_completed import ToggleTodoCompleted
    from .append_todo_list import AppendTodoList
    from .toggle_suggested_post_approval import ToggleSuggestedPostApproval
    from .get_forum_topics import GetForumTopics
    from .get_forum_topics_by_id import GetForumTopicsByID
    from .edit_forum_topic import EditForumTopic
    from .update_pinned_forum_topic import UpdatePinnedForumTopic
    from .reorder_pinned_forum_topics import ReorderPinnedForumTopics
    from .create_forum_topic import CreateForumTopic
    from .delete_topic_history import DeleteTopicHistory
    from .get_emoji_game_info import GetEmojiGameInfo
    from .summarize_text import SummarizeText
    from .edit_chat_creator import EditChatCreator
    from .get_future_chat_creator_after_leave import GetFutureChatCreatorAfterLeave
    from .edit_chat_participant_rank import EditChatParticipantRank
    from .decline_url_auth import DeclineUrlAuth
    from .check_url_auth_match_code import CheckUrlAuthMatchCode
    from .compose_message_with_ai import ComposeMessageWithAI
    from .report_read_metrics import ReportReadMetrics
    from .report_music_listen import ReportMusicListen
    from .add_poll_answer import AddPollAnswer
    from .delete_poll_answer import DeletePollAnswer
    from .get_unread_poll_votes import GetUnreadPollVotes
    from .read_poll_votes import ReadPollVotes
    from .set_bot_guest_chat_result import SetBotGuestChatResult
    from .delete_participant_reactions import DeleteParticipantReactions
    from .delete_participant_reaction import DeleteParticipantReaction
    from .get_personal_channel_history import GetPersonalChannelHistory
