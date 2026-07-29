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
    "Dialogs": "dialogs",
    "DialogsSlice": "dialogs_slice",
    "DialogsNotModified": "dialogs_not_modified",
    "Messages": "messages",
    "MessagesSlice": "messages_slice",
    "ChannelMessages": "channel_messages",
    "MessagesNotModified": "messages_not_modified",
    "Chats": "chats",
    "ChatsSlice": "chats_slice",
    "ChatFull": "chat_full",
    "AffectedHistory": "affected_history",
    "DhConfigNotModified": "dh_config_not_modified",
    "DhConfig": "dh_config",
    "SentEncryptedMessage": "sent_encrypted_message",
    "SentEncryptedFile": "sent_encrypted_file",
    "StickersNotModified": "stickers_not_modified",
    "Stickers": "stickers",
    "AllStickersNotModified": "all_stickers_not_modified",
    "AllStickers": "all_stickers",
    "AffectedMessages": "affected_messages",
    "StickerSet": "sticker_set",
    "StickerSetNotModified": "sticker_set_not_modified",
    "SavedGifsNotModified": "saved_gifs_not_modified",
    "SavedGifs": "saved_gifs",
    "BotResults": "bot_results",
    "BotCallbackAnswer": "bot_callback_answer",
    "MessageEditData": "message_edit_data",
    "PeerDialogs": "peer_dialogs",
    "FeaturedStickersNotModified": "featured_stickers_not_modified",
    "FeaturedStickers": "featured_stickers",
    "RecentStickersNotModified": "recent_stickers_not_modified",
    "RecentStickers": "recent_stickers",
    "ArchivedStickers": "archived_stickers",
    "StickerSetInstallResultSuccess": "sticker_set_install_result_success",
    "StickerSetInstallResultArchive": "sticker_set_install_result_archive",
    "HighScores": "high_scores",
    "FavedStickersNotModified": "faved_stickers_not_modified",
    "FavedStickers": "faved_stickers",
    "FoundStickerSetsNotModified": "found_sticker_sets_not_modified",
    "FoundStickerSets": "found_sticker_sets",
    "SearchCounter": "search_counter",
    "InactiveChats": "inactive_chats",
    "VotesList": "votes_list",
    "MessageViews": "message_views",
    "DiscussionMessage": "discussion_message",
    "HistoryImport": "history_import",
    "HistoryImportParsed": "history_import_parsed",
    "AffectedFoundMessages": "affected_found_messages",
    "ExportedChatInvites": "exported_chat_invites",
    "ExportedChatInvite": "exported_chat_invite",
    "ExportedChatInviteReplaced": "exported_chat_invite_replaced",
    "ChatInviteImporters": "chat_invite_importers",
    "ChatAdminsWithInvites": "chat_admins_with_invites",
    "CheckedHistoryImportPeer": "checked_history_import_peer",
    "SponsoredMessages": "sponsored_messages",
    "SponsoredMessagesEmpty": "sponsored_messages_empty",
    "SearchResultsCalendar": "search_results_calendar",
    "SearchResultsPositions": "search_results_positions",
    "PeerSettings": "peer_settings",
    "MessageReactionsList": "message_reactions_list",
    "AvailableReactionsNotModified": "available_reactions_not_modified",
    "AvailableReactions": "available_reactions",
    "TranscribedAudio": "transcribed_audio",
    "ReactionsNotModified": "reactions_not_modified",
    "Reactions": "reactions",
    "ForumTopics": "forum_topics",
    "EmojiGroupsNotModified": "emoji_groups_not_modified",
    "EmojiGroups": "emoji_groups",
    "TranslateResult": "translate_result",
    "BotApp": "bot_app",
    "WebPage": "web_page",
    "SavedDialogs": "saved_dialogs",
    "SavedDialogsSlice": "saved_dialogs_slice",
    "SavedDialogsNotModified": "saved_dialogs_not_modified",
    "SavedReactionTagsNotModified": "saved_reaction_tags_not_modified",
    "SavedReactionTags": "saved_reaction_tags",
    "QuickReplies": "quick_replies",
    "QuickRepliesNotModified": "quick_replies_not_modified",
    "DialogFilters": "dialog_filters",
    "MyStickers": "my_stickers",
    "InvitedUsers": "invited_users",
    "AvailableEffectsNotModified": "available_effects_not_modified",
    "AvailableEffects": "available_effects",
    "BotPreparedInlineMessage": "bot_prepared_inline_message",
    "PreparedInlineMessage": "prepared_inline_message",
    "FoundStickersNotModified": "found_stickers_not_modified",
    "FoundStickers": "found_stickers",
    "WebPagePreview": "web_page_preview",
    "EmojiGameOutcome": "emoji_game_outcome",
    "EmojiGameUnavailable": "emoji_game_unavailable",
    "EmojiGameDiceInfo": "emoji_game_dice_info",
    "ComposedMessageWithAI": "composed_message_with_ai",
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
    from .dialogs import Dialogs
    from .dialogs_slice import DialogsSlice
    from .dialogs_not_modified import DialogsNotModified
    from .messages import Messages
    from .messages_slice import MessagesSlice
    from .channel_messages import ChannelMessages
    from .messages_not_modified import MessagesNotModified
    from .chats import Chats
    from .chats_slice import ChatsSlice
    from .chat_full import ChatFull
    from .affected_history import AffectedHistory
    from .dh_config_not_modified import DhConfigNotModified
    from .dh_config import DhConfig
    from .sent_encrypted_message import SentEncryptedMessage
    from .sent_encrypted_file import SentEncryptedFile
    from .stickers_not_modified import StickersNotModified
    from .stickers import Stickers
    from .all_stickers_not_modified import AllStickersNotModified
    from .all_stickers import AllStickers
    from .affected_messages import AffectedMessages
    from .sticker_set import StickerSet
    from .sticker_set_not_modified import StickerSetNotModified
    from .saved_gifs_not_modified import SavedGifsNotModified
    from .saved_gifs import SavedGifs
    from .bot_results import BotResults
    from .bot_callback_answer import BotCallbackAnswer
    from .message_edit_data import MessageEditData
    from .peer_dialogs import PeerDialogs
    from .featured_stickers_not_modified import FeaturedStickersNotModified
    from .featured_stickers import FeaturedStickers
    from .recent_stickers_not_modified import RecentStickersNotModified
    from .recent_stickers import RecentStickers
    from .archived_stickers import ArchivedStickers
    from .sticker_set_install_result_success import StickerSetInstallResultSuccess
    from .sticker_set_install_result_archive import StickerSetInstallResultArchive
    from .high_scores import HighScores
    from .faved_stickers_not_modified import FavedStickersNotModified
    from .faved_stickers import FavedStickers
    from .found_sticker_sets_not_modified import FoundStickerSetsNotModified
    from .found_sticker_sets import FoundStickerSets
    from .search_counter import SearchCounter
    from .inactive_chats import InactiveChats
    from .votes_list import VotesList
    from .message_views import MessageViews
    from .discussion_message import DiscussionMessage
    from .history_import import HistoryImport
    from .history_import_parsed import HistoryImportParsed
    from .affected_found_messages import AffectedFoundMessages
    from .exported_chat_invites import ExportedChatInvites
    from .exported_chat_invite import ExportedChatInvite
    from .exported_chat_invite_replaced import ExportedChatInviteReplaced
    from .chat_invite_importers import ChatInviteImporters
    from .chat_admins_with_invites import ChatAdminsWithInvites
    from .checked_history_import_peer import CheckedHistoryImportPeer
    from .sponsored_messages import SponsoredMessages
    from .sponsored_messages_empty import SponsoredMessagesEmpty
    from .search_results_calendar import SearchResultsCalendar
    from .search_results_positions import SearchResultsPositions
    from .peer_settings import PeerSettings
    from .message_reactions_list import MessageReactionsList
    from .available_reactions_not_modified import AvailableReactionsNotModified
    from .available_reactions import AvailableReactions
    from .transcribed_audio import TranscribedAudio
    from .reactions_not_modified import ReactionsNotModified
    from .reactions import Reactions
    from .forum_topics import ForumTopics
    from .emoji_groups_not_modified import EmojiGroupsNotModified
    from .emoji_groups import EmojiGroups
    from .translate_result import TranslateResult
    from .bot_app import BotApp
    from .web_page import WebPage
    from .saved_dialogs import SavedDialogs
    from .saved_dialogs_slice import SavedDialogsSlice
    from .saved_dialogs_not_modified import SavedDialogsNotModified
    from .saved_reaction_tags_not_modified import SavedReactionTagsNotModified
    from .saved_reaction_tags import SavedReactionTags
    from .quick_replies import QuickReplies
    from .quick_replies_not_modified import QuickRepliesNotModified
    from .dialog_filters import DialogFilters
    from .my_stickers import MyStickers
    from .invited_users import InvitedUsers
    from .available_effects_not_modified import AvailableEffectsNotModified
    from .available_effects import AvailableEffects
    from .bot_prepared_inline_message import BotPreparedInlineMessage
    from .prepared_inline_message import PreparedInlineMessage
    from .found_stickers_not_modified import FoundStickersNotModified
    from .found_stickers import FoundStickers
    from .web_page_preview import WebPagePreview
    from .emoji_game_outcome import EmojiGameOutcome
    from .emoji_game_unavailable import EmojiGameUnavailable
    from .emoji_game_dice_info import EmojiGameDiceInfo
    from .composed_message_with_ai import ComposedMessageWithAI
