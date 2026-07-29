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
    "Messages": "messages",
    "Chats": "chats",
    "ChatFull": "chat_full",
    "AffectedHistory": "affected_history",
    "DhConfig": "dh_config",
    "SentEncryptedMessage": "sent_encrypted_message",
    "Stickers": "stickers",
    "AllStickers": "all_stickers",
    "AffectedMessages": "affected_messages",
    "StickerSet": "sticker_set",
    "SavedGifs": "saved_gifs",
    "BotResults": "bot_results",
    "BotCallbackAnswer": "bot_callback_answer",
    "MessageEditData": "message_edit_data",
    "PeerDialogs": "peer_dialogs",
    "FeaturedStickers": "featured_stickers",
    "RecentStickers": "recent_stickers",
    "ArchivedStickers": "archived_stickers",
    "StickerSetInstallResult": "sticker_set_install_result",
    "HighScores": "high_scores",
    "FavedStickers": "faved_stickers",
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
    "ChatInviteImporters": "chat_invite_importers",
    "ChatAdminsWithInvites": "chat_admins_with_invites",
    "CheckedHistoryImportPeer": "checked_history_import_peer",
    "SponsoredMessages": "sponsored_messages",
    "SearchResultsCalendar": "search_results_calendar",
    "SearchResultsPositions": "search_results_positions",
    "PeerSettings": "peer_settings",
    "MessageReactionsList": "message_reactions_list",
    "AvailableReactions": "available_reactions",
    "TranscribedAudio": "transcribed_audio",
    "Reactions": "reactions",
    "ForumTopics": "forum_topics",
    "EmojiGroups": "emoji_groups",
    "TranslatedText": "translated_text",
    "BotApp": "bot_app",
    "WebPage": "web_page",
    "SavedDialogs": "saved_dialogs",
    "SavedReactionTags": "saved_reaction_tags",
    "QuickReplies": "quick_replies",
    "DialogFilters": "dialog_filters",
    "MyStickers": "my_stickers",
    "InvitedUsers": "invited_users",
    "AvailableEffects": "available_effects",
    "BotPreparedInlineMessage": "bot_prepared_inline_message",
    "PreparedInlineMessage": "prepared_inline_message",
    "FoundStickers": "found_stickers",
    "WebPagePreview": "web_page_preview",
    "EmojiGameOutcome": "emoji_game_outcome",
    "EmojiGameInfo": "emoji_game_info",
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
    from .messages import Messages
    from .chats import Chats
    from .chat_full import ChatFull
    from .affected_history import AffectedHistory
    from .dh_config import DhConfig
    from .sent_encrypted_message import SentEncryptedMessage
    from .stickers import Stickers
    from .all_stickers import AllStickers
    from .affected_messages import AffectedMessages
    from .sticker_set import StickerSet
    from .saved_gifs import SavedGifs
    from .bot_results import BotResults
    from .bot_callback_answer import BotCallbackAnswer
    from .message_edit_data import MessageEditData
    from .peer_dialogs import PeerDialogs
    from .featured_stickers import FeaturedStickers
    from .recent_stickers import RecentStickers
    from .archived_stickers import ArchivedStickers
    from .sticker_set_install_result import StickerSetInstallResult
    from .high_scores import HighScores
    from .faved_stickers import FavedStickers
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
    from .chat_invite_importers import ChatInviteImporters
    from .chat_admins_with_invites import ChatAdminsWithInvites
    from .checked_history_import_peer import CheckedHistoryImportPeer
    from .sponsored_messages import SponsoredMessages
    from .search_results_calendar import SearchResultsCalendar
    from .search_results_positions import SearchResultsPositions
    from .peer_settings import PeerSettings
    from .message_reactions_list import MessageReactionsList
    from .available_reactions import AvailableReactions
    from .transcribed_audio import TranscribedAudio
    from .reactions import Reactions
    from .forum_topics import ForumTopics
    from .emoji_groups import EmojiGroups
    from .translated_text import TranslatedText
    from .bot_app import BotApp
    from .web_page import WebPage
    from .saved_dialogs import SavedDialogs
    from .saved_reaction_tags import SavedReactionTags
    from .quick_replies import QuickReplies
    from .dialog_filters import DialogFilters
    from .my_stickers import MyStickers
    from .invited_users import InvitedUsers
    from .available_effects import AvailableEffects
    from .bot_prepared_inline_message import BotPreparedInlineMessage
    from .prepared_inline_message import PreparedInlineMessage
    from .found_stickers import FoundStickers
    from .web_page_preview import WebPagePreview
    from .emoji_game_outcome import EmojiGameOutcome
    from .emoji_game_info import EmojiGameInfo
    from .composed_message_with_ai import ComposedMessageWithAI
