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
    "PQInnerDataDc": "pq_inner_data_dc",
    "PQInnerDataTemp": "pq_inner_data_temp",
    "PQInnerDataTempDc": "pq_inner_data_temp_dc",
    "BindAuthKeyInner": "bind_auth_key_inner",
    "ServerDHParamsFail": "server_dh_params_fail",
    "ServerDHParamsOk": "server_dh_params_ok",
    "ServerDHInnerData": "server_dh_inner_data",
    "ClientDHInnerData": "client_dh_inner_data",
    "DhGenOk": "dh_gen_ok",
    "DhGenRetry": "dh_gen_retry",
    "DhGenFail": "dh_gen_fail",
    "DestroyAuthKeyOk": "destroy_auth_key_ok",
    "DestroyAuthKeyNone": "destroy_auth_key_none",
    "DestroyAuthKeyFail": "destroy_auth_key_fail",
    "MsgsAck": "msgs_ack",
    "BadMsgNotification": "bad_msg_notification",
    "BadServerSalt": "bad_server_salt",
    "MsgsStateReq": "msgs_state_req",
    "MsgsStateInfo": "msgs_state_info",
    "MsgsAllInfo": "msgs_all_info",
    "MsgDetailedInfo": "msg_detailed_info",
    "MsgNewDetailedInfo": "msg_new_detailed_info",
    "MsgResendReq": "msg_resend_req",
    "MsgResendAnsReq": "msg_resend_ans_req",
    "RpcResult": "rpc_result",
    "RpcError": "rpc_error",
    "RpcAnswerUnknown": "rpc_answer_unknown",
    "RpcAnswerDroppedRunning": "rpc_answer_dropped_running",
    "RpcAnswerDropped": "rpc_answer_dropped",
    "Pong": "pong",
    "DestroySessionOk": "destroy_session_ok",
    "DestroySessionNone": "destroy_session_none",
    "NewSessionCreated": "new_session_created",
    "HttpWait": "http_wait",
    "IpPort": "ip_port",
    "IpPortSecret": "ip_port_secret",
    "AccessPointRule": "access_point_rule",
    "InputPeerEmpty": "input_peer_empty",
    "InputPeerSelf": "input_peer_self",
    "InputPeerChat": "input_peer_chat",
    "InputPeerUser": "input_peer_user",
    "InputPeerChannel": "input_peer_channel",
    "InputPeerUserFromMessage": "input_peer_user_from_message",
    "InputPeerChannelFromMessage": "input_peer_channel_from_message",
    "InputUserEmpty": "input_user_empty",
    "InputUserSelf": "input_user_self",
    "InputUser": "input_user",
    "InputUserFromMessage": "input_user_from_message",
    "InputPhoneContact": "input_phone_contact",
    "InputFile": "input_file",
    "InputFileBig": "input_file_big",
    "InputFileStoryDocument": "input_file_story_document",
    "InputMediaEmpty": "input_media_empty",
    "InputMediaUploadedPhoto": "input_media_uploaded_photo",
    "InputMediaPhoto": "input_media_photo",
    "InputMediaGeoPoint": "input_media_geo_point",
    "InputMediaContact": "input_media_contact",
    "InputMediaUploadedDocument": "input_media_uploaded_document",
    "InputMediaDocument": "input_media_document",
    "InputMediaVenue": "input_media_venue",
    "InputMediaPhotoExternal": "input_media_photo_external",
    "InputMediaDocumentExternal": "input_media_document_external",
    "InputMediaGame": "input_media_game",
    "InputMediaInvoice": "input_media_invoice",
    "InputMediaGeoLive": "input_media_geo_live",
    "InputMediaPoll": "input_media_poll",
    "InputMediaDice": "input_media_dice",
    "InputMediaStory": "input_media_story",
    "InputMediaWebPage": "input_media_web_page",
    "InputMediaPaidMedia": "input_media_paid_media",
    "InputMediaTodo": "input_media_todo",
    "InputMediaStakeDice": "input_media_stake_dice",
    "InputChatPhotoEmpty": "input_chat_photo_empty",
    "InputChatUploadedPhoto": "input_chat_uploaded_photo",
    "InputChatPhoto": "input_chat_photo",
    "InputGeoPointEmpty": "input_geo_point_empty",
    "InputGeoPoint": "input_geo_point",
    "InputPhotoEmpty": "input_photo_empty",
    "InputPhoto": "input_photo",
    "InputFileLocation": "input_file_location",
    "InputEncryptedFileLocation": "input_encrypted_file_location",
    "InputDocumentFileLocation": "input_document_file_location",
    "InputSecureFileLocation": "input_secure_file_location",
    "InputTakeoutFileLocation": "input_takeout_file_location",
    "InputPhotoFileLocation": "input_photo_file_location",
    "InputPhotoLegacyFileLocation": "input_photo_legacy_file_location",
    "InputPeerPhotoFileLocation": "input_peer_photo_file_location",
    "InputStickerSetThumb": "input_sticker_set_thumb",
    "InputGroupCallStream": "input_group_call_stream",
    "PeerUser": "peer_user",
    "PeerChat": "peer_chat",
    "PeerChannel": "peer_channel",
    "UserEmpty": "user_empty",
    "User": "user",
    "UserProfilePhotoEmpty": "user_profile_photo_empty",
    "UserProfilePhoto": "user_profile_photo",
    "UserStatusEmpty": "user_status_empty",
    "UserStatusOnline": "user_status_online",
    "UserStatusOffline": "user_status_offline",
    "UserStatusRecently": "user_status_recently",
    "UserStatusLastWeek": "user_status_last_week",
    "UserStatusLastMonth": "user_status_last_month",
    "ChatEmpty": "chat_empty",
    "Chat": "chat",
    "ChatForbidden": "chat_forbidden",
    "Channel": "channel",
    "ChannelForbidden": "channel_forbidden",
    "ChatFull": "chat_full",
    "ChannelFull": "channel_full",
    "ChatParticipant": "chat_participant",
    "ChatParticipantCreator": "chat_participant_creator",
    "ChatParticipantAdmin": "chat_participant_admin",
    "ChatParticipantsForbidden": "chat_participants_forbidden",
    "ChatParticipants": "chat_participants",
    "ChatPhotoEmpty": "chat_photo_empty",
    "ChatPhoto": "chat_photo",
    "MessageEmpty": "message_empty",
    "Message": "message",
    "MessageService": "message_service",
    "MessageMediaEmpty": "message_media_empty",
    "MessageMediaPhoto": "message_media_photo",
    "MessageMediaGeo": "message_media_geo",
    "MessageMediaContact": "message_media_contact",
    "MessageMediaUnsupported": "message_media_unsupported",
    "MessageMediaDocument": "message_media_document",
    "MessageMediaWebPage": "message_media_web_page",
    "MessageMediaVenue": "message_media_venue",
    "MessageMediaGame": "message_media_game",
    "MessageMediaInvoice": "message_media_invoice",
    "MessageMediaGeoLive": "message_media_geo_live",
    "MessageMediaPoll": "message_media_poll",
    "MessageMediaDice": "message_media_dice",
    "MessageMediaStory": "message_media_story",
    "MessageMediaGiveaway": "message_media_giveaway",
    "MessageMediaGiveawayResults": "message_media_giveaway_results",
    "MessageMediaPaidMedia": "message_media_paid_media",
    "MessageMediaToDo": "message_media_to_do",
    "MessageMediaVideoStream": "message_media_video_stream",
    "MessageActionEmpty": "message_action_empty",
    "MessageActionChatCreate": "message_action_chat_create",
    "MessageActionChatEditTitle": "message_action_chat_edit_title",
    "MessageActionChatEditPhoto": "message_action_chat_edit_photo",
    "MessageActionChatDeletePhoto": "message_action_chat_delete_photo",
    "MessageActionChatAddUser": "message_action_chat_add_user",
    "MessageActionChatDeleteUser": "message_action_chat_delete_user",
    "MessageActionChatJoinedByLink": "message_action_chat_joined_by_link",
    "MessageActionChannelCreate": "message_action_channel_create",
    "MessageActionChatMigrateTo": "message_action_chat_migrate_to",
    "MessageActionChannelMigrateFrom": "message_action_channel_migrate_from",
    "MessageActionPinMessage": "message_action_pin_message",
    "MessageActionHistoryClear": "message_action_history_clear",
    "MessageActionGameScore": "message_action_game_score",
    "MessageActionPaymentSentMe": "message_action_payment_sent_me",
    "MessageActionPaymentSent": "message_action_payment_sent",
    "MessageActionPhoneCall": "message_action_phone_call",
    "MessageActionScreenshotTaken": "message_action_screenshot_taken",
    "MessageActionCustomAction": "message_action_custom_action",
    "MessageActionBotAllowed": "message_action_bot_allowed",
    "MessageActionSecureValuesSentMe": "message_action_secure_values_sent_me",
    "MessageActionSecureValuesSent": "message_action_secure_values_sent",
    "MessageActionContactSignUp": "message_action_contact_sign_up",
    "MessageActionGeoProximityReached": "message_action_geo_proximity_reached",
    "MessageActionGroupCall": "message_action_group_call",
    "MessageActionInviteToGroupCall": "message_action_invite_to_group_call",
    "MessageActionSetMessagesTTL": "message_action_set_messages_ttl",
    "MessageActionGroupCallScheduled": "message_action_group_call_scheduled",
    "MessageActionSetChatTheme": "message_action_set_chat_theme",
    "MessageActionChatJoinedByRequest": "message_action_chat_joined_by_request",
    "MessageActionWebViewDataSentMe": "message_action_web_view_data_sent_me",
    "MessageActionWebViewDataSent": "message_action_web_view_data_sent",
    "MessageActionGiftPremium": "message_action_gift_premium",
    "MessageActionTopicCreate": "message_action_topic_create",
    "MessageActionTopicEdit": "message_action_topic_edit",
    "MessageActionSuggestProfilePhoto": "message_action_suggest_profile_photo",
    "MessageActionRequestedPeer": "message_action_requested_peer",
    "MessageActionSetChatWallPaper": "message_action_set_chat_wall_paper",
    "MessageActionGiftCode": "message_action_gift_code",
    "MessageActionGiveawayLaunch": "message_action_giveaway_launch",
    "MessageActionGiveawayResults": "message_action_giveaway_results",
    "MessageActionBoostApply": "message_action_boost_apply",
    "MessageActionRequestedPeerSentMe": "message_action_requested_peer_sent_me",
    "MessageActionPaymentRefunded": "message_action_payment_refunded",
    "MessageActionGiftStars": "message_action_gift_stars",
    "MessageActionPrizeStars": "message_action_prize_stars",
    "MessageActionStarGift": "message_action_star_gift",
    "MessageActionStarGiftUnique": "message_action_star_gift_unique",
    "MessageActionPaidMessagesRefunded": "message_action_paid_messages_refunded",
    "MessageActionPaidMessagesPrice": "message_action_paid_messages_price",
    "MessageActionConferenceCall": "message_action_conference_call",
    "MessageActionTodoCompletions": "message_action_todo_completions",
    "MessageActionTodoAppendTasks": "message_action_todo_append_tasks",
    "MessageActionSuggestedPostApproval": "message_action_suggested_post_approval",
    "MessageActionSuggestedPostSuccess": "message_action_suggested_post_success",
    "MessageActionSuggestedPostRefund": "message_action_suggested_post_refund",
    "MessageActionGiftTon": "message_action_gift_ton",
    "MessageActionSuggestBirthday": "message_action_suggest_birthday",
    "MessageActionStarGiftPurchaseOffer": "message_action_star_gift_purchase_offer",
    "MessageActionStarGiftPurchaseOfferDeclined": "message_action_star_gift_purchase_offer_declined",
    "MessageActionNewCreatorPending": "message_action_new_creator_pending",
    "MessageActionChangeCreator": "message_action_change_creator",
    "MessageActionNoForwardsToggle": "message_action_no_forwards_toggle",
    "MessageActionNoForwardsRequest": "message_action_no_forwards_request",
    "MessageActionPollAppendAnswer": "message_action_poll_append_answer",
    "MessageActionPollDeleteAnswer": "message_action_poll_delete_answer",
    "MessageActionManagedBotCreated": "message_action_managed_bot_created",
    "Dialog": "dialog",
    "DialogFolder": "dialog_folder",
    "PhotoEmpty": "photo_empty",
    "Photo": "photo",
    "PhotoSizeEmpty": "photo_size_empty",
    "PhotoSize": "photo_size",
    "PhotoCachedSize": "photo_cached_size",
    "PhotoStrippedSize": "photo_stripped_size",
    "PhotoSizeProgressive": "photo_size_progressive",
    "PhotoPathSize": "photo_path_size",
    "GeoPointEmpty": "geo_point_empty",
    "GeoPoint": "geo_point",
    "InputNotifyPeer": "input_notify_peer",
    "InputNotifyUsers": "input_notify_users",
    "InputNotifyChats": "input_notify_chats",
    "InputNotifyBroadcasts": "input_notify_broadcasts",
    "InputNotifyForumTopic": "input_notify_forum_topic",
    "InputPeerNotifySettings": "input_peer_notify_settings",
    "PeerNotifySettings": "peer_notify_settings",
    "PeerSettings": "peer_settings",
    "WallPaper": "wall_paper",
    "WallPaperNoFile": "wall_paper_no_file",
    "InputReportReasonSpam": "input_report_reason_spam",
    "InputReportReasonViolence": "input_report_reason_violence",
    "InputReportReasonPornography": "input_report_reason_pornography",
    "InputReportReasonChildAbuse": "input_report_reason_child_abuse",
    "InputReportReasonOther": "input_report_reason_other",
    "InputReportReasonCopyright": "input_report_reason_copyright",
    "InputReportReasonGeoIrrelevant": "input_report_reason_geo_irrelevant",
    "InputReportReasonFake": "input_report_reason_fake",
    "InputReportReasonIllegalDrugs": "input_report_reason_illegal_drugs",
    "InputReportReasonPersonalDetails": "input_report_reason_personal_details",
    "UserFull": "user_full",
    "Contact": "contact",
    "ImportedContact": "imported_contact",
    "ContactStatus": "contact_status",
    "InputMessagesFilterEmpty": "input_messages_filter_empty",
    "InputMessagesFilterPhotos": "input_messages_filter_photos",
    "InputMessagesFilterVideo": "input_messages_filter_video",
    "InputMessagesFilterPhotoVideo": "input_messages_filter_photo_video",
    "InputMessagesFilterDocument": "input_messages_filter_document",
    "InputMessagesFilterUrl": "input_messages_filter_url",
    "InputMessagesFilterGif": "input_messages_filter_gif",
    "InputMessagesFilterVoice": "input_messages_filter_voice",
    "InputMessagesFilterMusic": "input_messages_filter_music",
    "InputMessagesFilterChatPhotos": "input_messages_filter_chat_photos",
    "InputMessagesFilterPhoneCalls": "input_messages_filter_phone_calls",
    "InputMessagesFilterRoundVoice": "input_messages_filter_round_voice",
    "InputMessagesFilterRoundVideo": "input_messages_filter_round_video",
    "InputMessagesFilterMyMentions": "input_messages_filter_my_mentions",
    "InputMessagesFilterGeo": "input_messages_filter_geo",
    "InputMessagesFilterContacts": "input_messages_filter_contacts",
    "InputMessagesFilterPinned": "input_messages_filter_pinned",
    "InputMessagesFilterPoll": "input_messages_filter_poll",
    "UpdateNewMessage": "update_new_message",
    "UpdateMessageID": "update_message_id",
    "UpdateDeleteMessages": "update_delete_messages",
    "UpdateUserTyping": "update_user_typing",
    "UpdateChatUserTyping": "update_chat_user_typing",
    "UpdateChatParticipants": "update_chat_participants",
    "UpdateUserStatus": "update_user_status",
    "UpdateUserName": "update_user_name",
    "UpdateNewAuthorization": "update_new_authorization",
    "UpdateNewEncryptedMessage": "update_new_encrypted_message",
    "UpdateEncryptedChatTyping": "update_encrypted_chat_typing",
    "UpdateEncryption": "update_encryption",
    "UpdateEncryptedMessagesRead": "update_encrypted_messages_read",
    "UpdateChatParticipantAdd": "update_chat_participant_add",
    "UpdateChatParticipantDelete": "update_chat_participant_delete",
    "UpdateDcOptions": "update_dc_options",
    "UpdateNotifySettings": "update_notify_settings",
    "UpdateServiceNotification": "update_service_notification",
    "UpdatePrivacy": "update_privacy",
    "UpdateUserPhone": "update_user_phone",
    "UpdateReadHistoryInbox": "update_read_history_inbox",
    "UpdateReadHistoryOutbox": "update_read_history_outbox",
    "UpdateWebPage": "update_web_page",
    "UpdateReadMessagesContents": "update_read_messages_contents",
    "UpdateChannelTooLong": "update_channel_too_long",
    "UpdateChannel": "update_channel",
    "UpdateNewChannelMessage": "update_new_channel_message",
    "UpdateReadChannelInbox": "update_read_channel_inbox",
    "UpdateDeleteChannelMessages": "update_delete_channel_messages",
    "UpdateChannelMessageViews": "update_channel_message_views",
    "UpdateChatParticipantAdmin": "update_chat_participant_admin",
    "UpdateNewStickerSet": "update_new_sticker_set",
    "UpdateStickerSetsOrder": "update_sticker_sets_order",
    "UpdateStickerSets": "update_sticker_sets",
    "UpdateSavedGifs": "update_saved_gifs",
    "UpdateBotInlineQuery": "update_bot_inline_query",
    "UpdateBotInlineSend": "update_bot_inline_send",
    "UpdateEditChannelMessage": "update_edit_channel_message",
    "UpdateBotCallbackQuery": "update_bot_callback_query",
    "UpdateEditMessage": "update_edit_message",
    "UpdateInlineBotCallbackQuery": "update_inline_bot_callback_query",
    "UpdateReadChannelOutbox": "update_read_channel_outbox",
    "UpdateDraftMessage": "update_draft_message",
    "UpdateReadFeaturedStickers": "update_read_featured_stickers",
    "UpdateRecentStickers": "update_recent_stickers",
    "UpdateConfig": "update_config",
    "UpdatePtsChanged": "update_pts_changed",
    "UpdateChannelWebPage": "update_channel_web_page",
    "UpdateDialogPinned": "update_dialog_pinned",
    "UpdatePinnedDialogs": "update_pinned_dialogs",
    "UpdateBotWebhookJSON": "update_bot_webhook_json",
    "UpdateBotWebhookJSONQuery": "update_bot_webhook_json_query",
    "UpdateBotShippingQuery": "update_bot_shipping_query",
    "UpdateBotPrecheckoutQuery": "update_bot_precheckout_query",
    "UpdatePhoneCall": "update_phone_call",
    "UpdateLangPackTooLong": "update_lang_pack_too_long",
    "UpdateLangPack": "update_lang_pack",
    "UpdateFavedStickers": "update_faved_stickers",
    "UpdateChannelReadMessagesContents": "update_channel_read_messages_contents",
    "UpdateContactsReset": "update_contacts_reset",
    "UpdateChannelAvailableMessages": "update_channel_available_messages",
    "UpdateDialogUnreadMark": "update_dialog_unread_mark",
    "UpdateMessagePoll": "update_message_poll",
    "UpdateChatDefaultBannedRights": "update_chat_default_banned_rights",
    "UpdateFolderPeers": "update_folder_peers",
    "UpdatePeerSettings": "update_peer_settings",
    "UpdatePeerLocated": "update_peer_located",
    "UpdateNewScheduledMessage": "update_new_scheduled_message",
    "UpdateDeleteScheduledMessages": "update_delete_scheduled_messages",
    "UpdateTheme": "update_theme",
    "UpdateGeoLiveViewed": "update_geo_live_viewed",
    "UpdateLoginToken": "update_login_token",
    "UpdateMessagePollVote": "update_message_poll_vote",
    "UpdateDialogFilter": "update_dialog_filter",
    "UpdateDialogFilterOrder": "update_dialog_filter_order",
    "UpdateDialogFilters": "update_dialog_filters",
    "UpdatePhoneCallSignalingData": "update_phone_call_signaling_data",
    "UpdateChannelMessageForwards": "update_channel_message_forwards",
    "UpdateReadChannelDiscussionInbox": "update_read_channel_discussion_inbox",
    "UpdateReadChannelDiscussionOutbox": "update_read_channel_discussion_outbox",
    "UpdatePeerBlocked": "update_peer_blocked",
    "UpdateChannelUserTyping": "update_channel_user_typing",
    "UpdatePinnedMessages": "update_pinned_messages",
    "UpdatePinnedChannelMessages": "update_pinned_channel_messages",
    "UpdateChat": "update_chat",
    "UpdateGroupCallParticipants": "update_group_call_participants",
    "UpdateGroupCall": "update_group_call",
    "UpdatePeerHistoryTTL": "update_peer_history_ttl",
    "UpdateChatParticipant": "update_chat_participant",
    "UpdateChannelParticipant": "update_channel_participant",
    "UpdateBotStopped": "update_bot_stopped",
    "UpdateGroupCallConnection": "update_group_call_connection",
    "UpdateBotCommands": "update_bot_commands",
    "UpdatePendingJoinRequests": "update_pending_join_requests",
    "UpdateBotChatInviteRequester": "update_bot_chat_invite_requester",
    "UpdateMessageReactions": "update_message_reactions",
    "UpdateAttachMenuBots": "update_attach_menu_bots",
    "UpdateWebViewResultSent": "update_web_view_result_sent",
    "UpdateBotMenuButton": "update_bot_menu_button",
    "UpdateSavedRingtones": "update_saved_ringtones",
    "UpdateTranscribedAudio": "update_transcribed_audio",
    "UpdateReadFeaturedEmojiStickers": "update_read_featured_emoji_stickers",
    "UpdateUserEmojiStatus": "update_user_emoji_status",
    "UpdateRecentEmojiStatuses": "update_recent_emoji_statuses",
    "UpdateRecentReactions": "update_recent_reactions",
    "UpdateMoveStickerSetToTop": "update_move_sticker_set_to_top",
    "UpdateMessageExtendedMedia": "update_message_extended_media",
    "UpdateUser": "update_user",
    "UpdateAutoSaveSettings": "update_auto_save_settings",
    "UpdateStory": "update_story",
    "UpdateReadStories": "update_read_stories",
    "UpdateStoryID": "update_story_id",
    "UpdateStoriesStealthMode": "update_stories_stealth_mode",
    "UpdateSentStoryReaction": "update_sent_story_reaction",
    "UpdateBotChatBoost": "update_bot_chat_boost",
    "UpdateChannelViewForumAsMessages": "update_channel_view_forum_as_messages",
    "UpdatePeerWallpaper": "update_peer_wallpaper",
    "UpdateBotMessageReaction": "update_bot_message_reaction",
    "UpdateBotMessageReactions": "update_bot_message_reactions",
    "UpdateSavedDialogPinned": "update_saved_dialog_pinned",
    "UpdatePinnedSavedDialogs": "update_pinned_saved_dialogs",
    "UpdateSavedReactionTags": "update_saved_reaction_tags",
    "UpdateSmsJob": "update_sms_job",
    "UpdateQuickReplies": "update_quick_replies",
    "UpdateNewQuickReply": "update_new_quick_reply",
    "UpdateDeleteQuickReply": "update_delete_quick_reply",
    "UpdateQuickReplyMessage": "update_quick_reply_message",
    "UpdateDeleteQuickReplyMessages": "update_delete_quick_reply_messages",
    "UpdateBotBusinessConnect": "update_bot_business_connect",
    "UpdateBotNewBusinessMessage": "update_bot_new_business_message",
    "UpdateBotEditBusinessMessage": "update_bot_edit_business_message",
    "UpdateBotDeleteBusinessMessage": "update_bot_delete_business_message",
    "UpdateNewStoryReaction": "update_new_story_reaction",
    "UpdateStarsBalance": "update_stars_balance",
    "UpdateBusinessBotCallbackQuery": "update_business_bot_callback_query",
    "UpdateStarsRevenueStatus": "update_stars_revenue_status",
    "UpdateBotPurchasedPaidMedia": "update_bot_purchased_paid_media",
    "UpdatePaidReactionPrivacy": "update_paid_reaction_privacy",
    "UpdateSentPhoneCode": "update_sent_phone_code",
    "UpdateGroupCallChainBlocks": "update_group_call_chain_blocks",
    "UpdateReadMonoForumInbox": "update_read_mono_forum_inbox",
    "UpdateReadMonoForumOutbox": "update_read_mono_forum_outbox",
    "UpdateMonoForumNoPaidException": "update_mono_forum_no_paid_exception",
    "UpdateGroupCallMessage": "update_group_call_message",
    "UpdateGroupCallEncryptedMessage": "update_group_call_encrypted_message",
    "UpdatePinnedForumTopic": "update_pinned_forum_topic",
    "UpdatePinnedForumTopics": "update_pinned_forum_topics",
    "UpdateDeleteGroupCallMessages": "update_delete_group_call_messages",
    "UpdateStarGiftAuctionState": "update_star_gift_auction_state",
    "UpdateStarGiftAuctionUserState": "update_star_gift_auction_user_state",
    "UpdateEmojiGameInfo": "update_emoji_game_info",
    "UpdateStarGiftCraftFail": "update_star_gift_craft_fail",
    "UpdateChatParticipantRank": "update_chat_participant_rank",
    "UpdateManagedBot": "update_managed_bot",
    "UpdateBotGuestChatQuery": "update_bot_guest_chat_query",
    "UpdateAiComposeTones": "update_ai_compose_tones",
    "UpdatesTooLong": "updates_too_long",
    "UpdateShortMessage": "update_short_message",
    "UpdateShortChatMessage": "update_short_chat_message",
    "UpdateShort": "update_short",
    "UpdatesCombined": "updates_combined",
    "Updates": "updates_t",
    "UpdateShortSentMessage": "update_short_sent_message",
    "DcOption": "dc_option",
    "Config": "config",
    "NearestDc": "nearest_dc",
    "EncryptedChatEmpty": "encrypted_chat_empty",
    "EncryptedChatWaiting": "encrypted_chat_waiting",
    "EncryptedChatRequested": "encrypted_chat_requested",
    "EncryptedChat": "encrypted_chat",
    "EncryptedChatDiscarded": "encrypted_chat_discarded",
    "InputEncryptedChat": "input_encrypted_chat",
    "EncryptedFileEmpty": "encrypted_file_empty",
    "EncryptedFile": "encrypted_file",
    "InputEncryptedFileEmpty": "input_encrypted_file_empty",
    "InputEncryptedFileUploaded": "input_encrypted_file_uploaded",
    "InputEncryptedFile": "input_encrypted_file",
    "InputEncryptedFileBigUploaded": "input_encrypted_file_big_uploaded",
    "EncryptedMessage": "encrypted_message",
    "EncryptedMessageService": "encrypted_message_service",
    "InputDocumentEmpty": "input_document_empty",
    "InputDocument": "input_document",
    "DocumentEmpty": "document_empty",
    "Document": "document",
    "NotifyPeer": "notify_peer",
    "NotifyUsers": "notify_users",
    "NotifyChats": "notify_chats",
    "NotifyBroadcasts": "notify_broadcasts",
    "NotifyForumTopic": "notify_forum_topic",
    "SendMessageTypingAction": "send_message_typing_action",
    "SendMessageCancelAction": "send_message_cancel_action",
    "SendMessageRecordVideoAction": "send_message_record_video_action",
    "SendMessageUploadVideoAction": "send_message_upload_video_action",
    "SendMessageRecordAudioAction": "send_message_record_audio_action",
    "SendMessageUploadAudioAction": "send_message_upload_audio_action",
    "SendMessageUploadPhotoAction": "send_message_upload_photo_action",
    "SendMessageUploadDocumentAction": "send_message_upload_document_action",
    "SendMessageGeoLocationAction": "send_message_geo_location_action",
    "SendMessageChooseContactAction": "send_message_choose_contact_action",
    "SendMessageGamePlayAction": "send_message_game_play_action",
    "SendMessageRecordRoundAction": "send_message_record_round_action",
    "SendMessageUploadRoundAction": "send_message_upload_round_action",
    "SpeakingInGroupCallAction": "speaking_in_group_call_action",
    "SendMessageHistoryImportAction": "send_message_history_import_action",
    "SendMessageChooseStickerAction": "send_message_choose_sticker_action",
    "SendMessageEmojiInteraction": "send_message_emoji_interaction",
    "SendMessageEmojiInteractionSeen": "send_message_emoji_interaction_seen",
    "SendMessageTextDraftAction": "send_message_text_draft_action",
    "InputPrivacyKeyStatusTimestamp": "input_privacy_key_status_timestamp",
    "InputPrivacyKeyChatInvite": "input_privacy_key_chat_invite",
    "InputPrivacyKeyPhoneCall": "input_privacy_key_phone_call",
    "InputPrivacyKeyPhoneP2P": "input_privacy_key_phone_p2_p",
    "InputPrivacyKeyForwards": "input_privacy_key_forwards",
    "InputPrivacyKeyProfilePhoto": "input_privacy_key_profile_photo",
    "InputPrivacyKeyPhoneNumber": "input_privacy_key_phone_number",
    "InputPrivacyKeyAddedByPhone": "input_privacy_key_added_by_phone",
    "InputPrivacyKeyVoiceMessages": "input_privacy_key_voice_messages",
    "InputPrivacyKeyAbout": "input_privacy_key_about",
    "InputPrivacyKeyBirthday": "input_privacy_key_birthday",
    "InputPrivacyKeyStarGiftsAutoSave": "input_privacy_key_star_gifts_auto_save",
    "InputPrivacyKeyNoPaidMessages": "input_privacy_key_no_paid_messages",
    "InputPrivacyKeySavedMusic": "input_privacy_key_saved_music",
    "PrivacyKeyStatusTimestamp": "privacy_key_status_timestamp",
    "PrivacyKeyChatInvite": "privacy_key_chat_invite",
    "PrivacyKeyPhoneCall": "privacy_key_phone_call",
    "PrivacyKeyPhoneP2P": "privacy_key_phone_p2_p",
    "PrivacyKeyForwards": "privacy_key_forwards",
    "PrivacyKeyProfilePhoto": "privacy_key_profile_photo",
    "PrivacyKeyPhoneNumber": "privacy_key_phone_number",
    "PrivacyKeyAddedByPhone": "privacy_key_added_by_phone",
    "PrivacyKeyVoiceMessages": "privacy_key_voice_messages",
    "PrivacyKeyAbout": "privacy_key_about",
    "PrivacyKeyBirthday": "privacy_key_birthday",
    "PrivacyKeyStarGiftsAutoSave": "privacy_key_star_gifts_auto_save",
    "PrivacyKeyNoPaidMessages": "privacy_key_no_paid_messages",
    "PrivacyKeySavedMusic": "privacy_key_saved_music",
    "InputPrivacyValueAllowContacts": "input_privacy_value_allow_contacts",
    "InputPrivacyValueAllowAll": "input_privacy_value_allow_all",
    "InputPrivacyValueAllowUsers": "input_privacy_value_allow_users",
    "InputPrivacyValueDisallowContacts": "input_privacy_value_disallow_contacts",
    "InputPrivacyValueDisallowAll": "input_privacy_value_disallow_all",
    "InputPrivacyValueDisallowUsers": "input_privacy_value_disallow_users",
    "InputPrivacyValueAllowChatParticipants": "input_privacy_value_allow_chat_participants",
    "InputPrivacyValueDisallowChatParticipants": "input_privacy_value_disallow_chat_participants",
    "InputPrivacyValueAllowCloseFriends": "input_privacy_value_allow_close_friends",
    "InputPrivacyValueAllowPremium": "input_privacy_value_allow_premium",
    "InputPrivacyValueAllowBots": "input_privacy_value_allow_bots",
    "InputPrivacyValueDisallowBots": "input_privacy_value_disallow_bots",
    "PrivacyValueAllowContacts": "privacy_value_allow_contacts",
    "PrivacyValueAllowAll": "privacy_value_allow_all",
    "PrivacyValueAllowUsers": "privacy_value_allow_users",
    "PrivacyValueDisallowContacts": "privacy_value_disallow_contacts",
    "PrivacyValueDisallowAll": "privacy_value_disallow_all",
    "PrivacyValueDisallowUsers": "privacy_value_disallow_users",
    "PrivacyValueAllowChatParticipants": "privacy_value_allow_chat_participants",
    "PrivacyValueDisallowChatParticipants": "privacy_value_disallow_chat_participants",
    "PrivacyValueAllowCloseFriends": "privacy_value_allow_close_friends",
    "PrivacyValueAllowPremium": "privacy_value_allow_premium",
    "PrivacyValueAllowBots": "privacy_value_allow_bots",
    "PrivacyValueDisallowBots": "privacy_value_disallow_bots",
    "AccountDaysTTL": "account_days_ttl",
    "DocumentAttributeImageSize": "document_attribute_image_size",
    "DocumentAttributeAnimated": "document_attribute_animated",
    "DocumentAttributeSticker": "document_attribute_sticker",
    "DocumentAttributeVideo": "document_attribute_video",
    "DocumentAttributeAudio": "document_attribute_audio",
    "DocumentAttributeFilename": "document_attribute_filename",
    "DocumentAttributeHasStickers": "document_attribute_has_stickers",
    "DocumentAttributeCustomEmoji": "document_attribute_custom_emoji",
    "StickerPack": "sticker_pack",
    "WebPageEmpty": "web_page_empty",
    "WebPagePending": "web_page_pending",
    "WebPage": "web_page",
    "WebPageNotModified": "web_page_not_modified",
    "Authorization": "authorization",
    "ReceivedNotifyMessage": "received_notify_message",
    "ChatInviteExported": "chat_invite_exported",
    "ChatInvitePublicJoinRequests": "chat_invite_public_join_requests",
    "ChatInviteAlready": "chat_invite_already",
    "ChatInvite": "chat_invite",
    "ChatInvitePeek": "chat_invite_peek",
    "InputStickerSetEmpty": "input_sticker_set_empty",
    "InputStickerSetID": "input_sticker_set_id",
    "InputStickerSetShortName": "input_sticker_set_short_name",
    "InputStickerSetAnimatedEmoji": "input_sticker_set_animated_emoji",
    "InputStickerSetDice": "input_sticker_set_dice",
    "InputStickerSetAnimatedEmojiAnimations": "input_sticker_set_animated_emoji_animations",
    "InputStickerSetPremiumGifts": "input_sticker_set_premium_gifts",
    "InputStickerSetEmojiGenericAnimations": "input_sticker_set_emoji_generic_animations",
    "InputStickerSetEmojiDefaultStatuses": "input_sticker_set_emoji_default_statuses",
    "InputStickerSetEmojiDefaultTopicIcons": "input_sticker_set_emoji_default_topic_icons",
    "InputStickerSetEmojiChannelDefaultStatuses": "input_sticker_set_emoji_channel_default_statuses",
    "InputStickerSetTonGifts": "input_sticker_set_ton_gifts",
    "StickerSet": "sticker_set",
    "BotCommand": "bot_command",
    "BotInfo": "bot_info",
    "KeyboardButton": "keyboard_button",
    "KeyboardButtonUrl": "keyboard_button_url",
    "KeyboardButtonCallback": "keyboard_button_callback",
    "KeyboardButtonRequestPhone": "keyboard_button_request_phone",
    "KeyboardButtonRequestGeoLocation": "keyboard_button_request_geo_location",
    "KeyboardButtonSwitchInline": "keyboard_button_switch_inline",
    "KeyboardButtonGame": "keyboard_button_game",
    "KeyboardButtonBuy": "keyboard_button_buy",
    "KeyboardButtonUrlAuth": "keyboard_button_url_auth",
    "InputKeyboardButtonUrlAuth": "input_keyboard_button_url_auth",
    "KeyboardButtonRequestPoll": "keyboard_button_request_poll",
    "InputKeyboardButtonUserProfile": "input_keyboard_button_user_profile",
    "KeyboardButtonUserProfile": "keyboard_button_user_profile",
    "KeyboardButtonWebView": "keyboard_button_web_view",
    "KeyboardButtonSimpleWebView": "keyboard_button_simple_web_view",
    "KeyboardButtonRequestPeer": "keyboard_button_request_peer",
    "InputKeyboardButtonRequestPeer": "input_keyboard_button_request_peer",
    "KeyboardButtonCopy": "keyboard_button_copy",
    "KeyboardButtonRow": "keyboard_button_row",
    "ReplyKeyboardHide": "reply_keyboard_hide",
    "ReplyKeyboardForceReply": "reply_keyboard_force_reply",
    "ReplyKeyboardMarkup": "reply_keyboard_markup",
    "ReplyInlineMarkup": "reply_inline_markup",
    "MessageEntityUnknown": "message_entity_unknown",
    "MessageEntityMention": "message_entity_mention",
    "MessageEntityHashtag": "message_entity_hashtag",
    "MessageEntityBotCommand": "message_entity_bot_command",
    "MessageEntityUrl": "message_entity_url",
    "MessageEntityEmail": "message_entity_email",
    "MessageEntityBold": "message_entity_bold",
    "MessageEntityItalic": "message_entity_italic",
    "MessageEntityCode": "message_entity_code",
    "MessageEntityPre": "message_entity_pre",
    "MessageEntityTextUrl": "message_entity_text_url",
    "MessageEntityMentionName": "message_entity_mention_name",
    "InputMessageEntityMentionName": "input_message_entity_mention_name",
    "MessageEntityPhone": "message_entity_phone",
    "MessageEntityCashtag": "message_entity_cashtag",
    "MessageEntityUnderline": "message_entity_underline",
    "MessageEntityStrike": "message_entity_strike",
    "MessageEntityBankCard": "message_entity_bank_card",
    "MessageEntitySpoiler": "message_entity_spoiler",
    "MessageEntityCustomEmoji": "message_entity_custom_emoji",
    "MessageEntityBlockquote": "message_entity_blockquote",
    "MessageEntityFormattedDate": "message_entity_formatted_date",
    "MessageEntityDiffInsert": "message_entity_diff_insert",
    "MessageEntityDiffReplace": "message_entity_diff_replace",
    "MessageEntityDiffDelete": "message_entity_diff_delete",
    "InputChannelEmpty": "input_channel_empty",
    "InputChannel": "input_channel",
    "InputChannelFromMessage": "input_channel_from_message",
    "MessageRange": "message_range",
    "ChannelMessagesFilterEmpty": "channel_messages_filter_empty",
    "ChannelMessagesFilter": "channel_messages_filter",
    "ChannelParticipant": "channel_participant",
    "ChannelParticipantSelf": "channel_participant_self",
    "ChannelParticipantCreator": "channel_participant_creator",
    "ChannelParticipantAdmin": "channel_participant_admin",
    "ChannelParticipantBanned": "channel_participant_banned",
    "ChannelParticipantLeft": "channel_participant_left",
    "ChannelParticipantsRecent": "channel_participants_recent",
    "ChannelParticipantsAdmins": "channel_participants_admins",
    "ChannelParticipantsKicked": "channel_participants_kicked",
    "ChannelParticipantsBots": "channel_participants_bots",
    "ChannelParticipantsBanned": "channel_participants_banned",
    "ChannelParticipantsSearch": "channel_participants_search",
    "ChannelParticipantsContacts": "channel_participants_contacts",
    "ChannelParticipantsMentions": "channel_participants_mentions",
    "InputBotInlineMessageMediaAuto": "input_bot_inline_message_media_auto",
    "InputBotInlineMessageText": "input_bot_inline_message_text",
    "InputBotInlineMessageMediaGeo": "input_bot_inline_message_media_geo",
    "InputBotInlineMessageMediaVenue": "input_bot_inline_message_media_venue",
    "InputBotInlineMessageMediaContact": "input_bot_inline_message_media_contact",
    "InputBotInlineMessageGame": "input_bot_inline_message_game",
    "InputBotInlineMessageMediaInvoice": "input_bot_inline_message_media_invoice",
    "InputBotInlineMessageMediaWebPage": "input_bot_inline_message_media_web_page",
    "InputBotInlineResult": "input_bot_inline_result",
    "InputBotInlineResultPhoto": "input_bot_inline_result_photo",
    "InputBotInlineResultDocument": "input_bot_inline_result_document",
    "InputBotInlineResultGame": "input_bot_inline_result_game",
    "BotInlineMessageMediaAuto": "bot_inline_message_media_auto",
    "BotInlineMessageText": "bot_inline_message_text",
    "BotInlineMessageMediaGeo": "bot_inline_message_media_geo",
    "BotInlineMessageMediaVenue": "bot_inline_message_media_venue",
    "BotInlineMessageMediaContact": "bot_inline_message_media_contact",
    "BotInlineMessageMediaInvoice": "bot_inline_message_media_invoice",
    "BotInlineMessageMediaWebPage": "bot_inline_message_media_web_page",
    "BotInlineResult": "bot_inline_result",
    "BotInlineMediaResult": "bot_inline_media_result",
    "ExportedMessageLink": "exported_message_link",
    "MessageFwdHeader": "message_fwd_header",
    "InputBotInlineMessageID": "input_bot_inline_message_id",
    "InputBotInlineMessageID64": "input_bot_inline_message_id64",
    "InlineBotSwitchPM": "inline_bot_switch_pm",
    "TopPeer": "top_peer",
    "TopPeerCategoryBotsPM": "top_peer_category_bots_pm",
    "TopPeerCategoryBotsInline": "top_peer_category_bots_inline",
    "TopPeerCategoryCorrespondents": "top_peer_category_correspondents",
    "TopPeerCategoryGroups": "top_peer_category_groups",
    "TopPeerCategoryChannels": "top_peer_category_channels",
    "TopPeerCategoryPhoneCalls": "top_peer_category_phone_calls",
    "TopPeerCategoryForwardUsers": "top_peer_category_forward_users",
    "TopPeerCategoryForwardChats": "top_peer_category_forward_chats",
    "TopPeerCategoryBotsApp": "top_peer_category_bots_app",
    "TopPeerCategoryBotsGuestChat": "top_peer_category_bots_guest_chat",
    "TopPeerCategoryPeers": "top_peer_category_peers",
    "DraftMessageEmpty": "draft_message_empty",
    "DraftMessage": "draft_message",
    "StickerSetCovered": "sticker_set_covered",
    "StickerSetMultiCovered": "sticker_set_multi_covered",
    "StickerSetFullCovered": "sticker_set_full_covered",
    "StickerSetNoCovered": "sticker_set_no_covered",
    "MaskCoords": "mask_coords",
    "InputStickeredMediaPhoto": "input_stickered_media_photo",
    "InputStickeredMediaDocument": "input_stickered_media_document",
    "Game": "game",
    "InputGameID": "input_game_id",
    "InputGameShortName": "input_game_short_name",
    "HighScore": "high_score",
    "TextEmpty": "text_empty",
    "TextPlain": "text_plain",
    "TextBold": "text_bold",
    "TextItalic": "text_italic",
    "TextUnderline": "text_underline",
    "TextStrike": "text_strike",
    "TextFixed": "text_fixed",
    "TextUrl": "text_url",
    "TextEmail": "text_email",
    "TextConcat": "text_concat",
    "TextSubscript": "text_subscript",
    "TextSuperscript": "text_superscript",
    "TextMarked": "text_marked",
    "TextPhone": "text_phone",
    "TextImage": "text_image",
    "TextAnchor": "text_anchor",
    "PageBlockUnsupported": "page_block_unsupported",
    "PageBlockTitle": "page_block_title",
    "PageBlockSubtitle": "page_block_subtitle",
    "PageBlockAuthorDate": "page_block_author_date",
    "PageBlockHeader": "page_block_header",
    "PageBlockSubheader": "page_block_subheader",
    "PageBlockParagraph": "page_block_paragraph",
    "PageBlockPreformatted": "page_block_preformatted",
    "PageBlockFooter": "page_block_footer",
    "PageBlockDivider": "page_block_divider",
    "PageBlockAnchor": "page_block_anchor",
    "PageBlockList": "page_block_list",
    "PageBlockBlockquote": "page_block_blockquote",
    "PageBlockPullquote": "page_block_pullquote",
    "PageBlockPhoto": "page_block_photo",
    "PageBlockVideo": "page_block_video",
    "PageBlockCover": "page_block_cover",
    "PageBlockEmbed": "page_block_embed",
    "PageBlockEmbedPost": "page_block_embed_post",
    "PageBlockCollage": "page_block_collage",
    "PageBlockSlideshow": "page_block_slideshow",
    "PageBlockChannel": "page_block_channel",
    "PageBlockAudio": "page_block_audio",
    "PageBlockKicker": "page_block_kicker",
    "PageBlockTable": "page_block_table",
    "PageBlockOrderedList": "page_block_ordered_list",
    "PageBlockDetails": "page_block_details",
    "PageBlockRelatedArticles": "page_block_related_articles",
    "PageBlockMap": "page_block_map",
    "PhoneCallDiscardReasonMissed": "phone_call_discard_reason_missed",
    "PhoneCallDiscardReasonDisconnect": "phone_call_discard_reason_disconnect",
    "PhoneCallDiscardReasonHangup": "phone_call_discard_reason_hangup",
    "PhoneCallDiscardReasonBusy": "phone_call_discard_reason_busy",
    "PhoneCallDiscardReasonMigrateConferenceCall": "phone_call_discard_reason_migrate_conference_call",
    "DataJSON": "data_json",
    "LabeledPrice": "labeled_price",
    "Invoice": "invoice",
    "PaymentCharge": "payment_charge",
    "PostAddress": "post_address",
    "PaymentRequestedInfo": "payment_requested_info",
    "PaymentSavedCredentialsCard": "payment_saved_credentials_card",
    "WebDocument": "web_document",
    "WebDocumentNoProxy": "web_document_no_proxy",
    "InputWebDocument": "input_web_document",
    "InputWebFileLocation": "input_web_file_location",
    "InputWebFileGeoPointLocation": "input_web_file_geo_point_location",
    "InputWebFileAudioAlbumThumbLocation": "input_web_file_audio_album_thumb_location",
    "InputPaymentCredentialsSaved": "input_payment_credentials_saved",
    "InputPaymentCredentials": "input_payment_credentials",
    "InputPaymentCredentialsApplePay": "input_payment_credentials_apple_pay",
    "InputPaymentCredentialsGooglePay": "input_payment_credentials_google_pay",
    "ShippingOption": "shipping_option",
    "InputStickerSetItem": "input_sticker_set_item",
    "InputPhoneCall": "input_phone_call",
    "PhoneCallEmpty": "phone_call_empty",
    "PhoneCallWaiting": "phone_call_waiting",
    "PhoneCallRequested": "phone_call_requested",
    "PhoneCallAccepted": "phone_call_accepted",
    "PhoneCall": "phone_call",
    "PhoneCallDiscarded": "phone_call_discarded",
    "PhoneConnection": "phone_connection",
    "PhoneConnectionWebrtc": "phone_connection_webrtc",
    "PhoneCallProtocol": "phone_call_protocol",
    "CdnPublicKey": "cdn_public_key",
    "CdnConfig": "cdn_config",
    "LangPackString": "lang_pack_string",
    "LangPackStringPluralized": "lang_pack_string_pluralized",
    "LangPackStringDeleted": "lang_pack_string_deleted",
    "LangPackDifference": "lang_pack_difference",
    "LangPackLanguage": "lang_pack_language",
    "ChannelAdminLogEventActionChangeTitle": "channel_admin_log_event_action_change_title",
    "ChannelAdminLogEventActionChangeAbout": "channel_admin_log_event_action_change_about",
    "ChannelAdminLogEventActionChangeUsername": "channel_admin_log_event_action_change_username",
    "ChannelAdminLogEventActionChangePhoto": "channel_admin_log_event_action_change_photo",
    "ChannelAdminLogEventActionToggleInvites": "channel_admin_log_event_action_toggle_invites",
    "ChannelAdminLogEventActionToggleSignatures": "channel_admin_log_event_action_toggle_signatures",
    "ChannelAdminLogEventActionUpdatePinned": "channel_admin_log_event_action_update_pinned",
    "ChannelAdminLogEventActionEditMessage": "channel_admin_log_event_action_edit_message",
    "ChannelAdminLogEventActionDeleteMessage": "channel_admin_log_event_action_delete_message",
    "ChannelAdminLogEventActionParticipantJoin": "channel_admin_log_event_action_participant_join",
    "ChannelAdminLogEventActionParticipantLeave": "channel_admin_log_event_action_participant_leave",
    "ChannelAdminLogEventActionParticipantInvite": "channel_admin_log_event_action_participant_invite",
    "ChannelAdminLogEventActionParticipantToggleBan": "channel_admin_log_event_action_participant_toggle_ban",
    "ChannelAdminLogEventActionParticipantToggleAdmin": "channel_admin_log_event_action_participant_toggle_admin",
    "ChannelAdminLogEventActionChangeStickerSet": "channel_admin_log_event_action_change_sticker_set",
    "ChannelAdminLogEventActionTogglePreHistoryHidden": "channel_admin_log_event_action_toggle_pre_history_hidden",
    "ChannelAdminLogEventActionDefaultBannedRights": "channel_admin_log_event_action_default_banned_rights",
    "ChannelAdminLogEventActionStopPoll": "channel_admin_log_event_action_stop_poll",
    "ChannelAdminLogEventActionChangeLinkedChat": "channel_admin_log_event_action_change_linked_chat",
    "ChannelAdminLogEventActionChangeLocation": "channel_admin_log_event_action_change_location",
    "ChannelAdminLogEventActionToggleSlowMode": "channel_admin_log_event_action_toggle_slow_mode",
    "ChannelAdminLogEventActionStartGroupCall": "channel_admin_log_event_action_start_group_call",
    "ChannelAdminLogEventActionDiscardGroupCall": "channel_admin_log_event_action_discard_group_call",
    "ChannelAdminLogEventActionParticipantMute": "channel_admin_log_event_action_participant_mute",
    "ChannelAdminLogEventActionParticipantUnmute": "channel_admin_log_event_action_participant_unmute",
    "ChannelAdminLogEventActionToggleGroupCallSetting": "channel_admin_log_event_action_toggle_group_call_setting",
    "ChannelAdminLogEventActionParticipantJoinByInvite": "channel_admin_log_event_action_participant_join_by_invite",
    "ChannelAdminLogEventActionExportedInviteDelete": "channel_admin_log_event_action_exported_invite_delete",
    "ChannelAdminLogEventActionExportedInviteRevoke": "channel_admin_log_event_action_exported_invite_revoke",
    "ChannelAdminLogEventActionExportedInviteEdit": "channel_admin_log_event_action_exported_invite_edit",
    "ChannelAdminLogEventActionParticipantVolume": "channel_admin_log_event_action_participant_volume",
    "ChannelAdminLogEventActionChangeHistoryTTL": "channel_admin_log_event_action_change_history_ttl",
    "ChannelAdminLogEventActionParticipantJoinByRequest": "channel_admin_log_event_action_participant_join_by_request",
    "ChannelAdminLogEventActionToggleNoForwards": "channel_admin_log_event_action_toggle_no_forwards",
    "ChannelAdminLogEventActionSendMessage": "channel_admin_log_event_action_send_message",
    "ChannelAdminLogEventActionChangeAvailableReactions": "channel_admin_log_event_action_change_available_reactions",
    "ChannelAdminLogEventActionChangeUsernames": "channel_admin_log_event_action_change_usernames",
    "ChannelAdminLogEventActionToggleForum": "channel_admin_log_event_action_toggle_forum",
    "ChannelAdminLogEventActionCreateTopic": "channel_admin_log_event_action_create_topic",
    "ChannelAdminLogEventActionEditTopic": "channel_admin_log_event_action_edit_topic",
    "ChannelAdminLogEventActionDeleteTopic": "channel_admin_log_event_action_delete_topic",
    "ChannelAdminLogEventActionPinTopic": "channel_admin_log_event_action_pin_topic",
    "ChannelAdminLogEventActionToggleAntiSpam": "channel_admin_log_event_action_toggle_anti_spam",
    "ChannelAdminLogEventActionChangePeerColor": "channel_admin_log_event_action_change_peer_color",
    "ChannelAdminLogEventActionChangeProfilePeerColor": "channel_admin_log_event_action_change_profile_peer_color",
    "ChannelAdminLogEventActionChangeWallpaper": "channel_admin_log_event_action_change_wallpaper",
    "ChannelAdminLogEventActionChangeEmojiStatus": "channel_admin_log_event_action_change_emoji_status",
    "ChannelAdminLogEventActionChangeEmojiStickerSet": "channel_admin_log_event_action_change_emoji_sticker_set",
    "ChannelAdminLogEventActionToggleSignatureProfiles": "channel_admin_log_event_action_toggle_signature_profiles",
    "ChannelAdminLogEventActionParticipantSubExtend": "channel_admin_log_event_action_participant_sub_extend",
    "ChannelAdminLogEventActionToggleAutotranslation": "channel_admin_log_event_action_toggle_autotranslation",
    "ChannelAdminLogEventActionParticipantEditRank": "channel_admin_log_event_action_participant_edit_rank",
    "ChannelAdminLogEvent": "channel_admin_log_event",
    "ChannelAdminLogEventsFilter": "channel_admin_log_events_filter",
    "PopularContact": "popular_contact",
    "RecentMeUrlUnknown": "recent_me_url_unknown",
    "RecentMeUrlUser": "recent_me_url_user",
    "RecentMeUrlChat": "recent_me_url_chat",
    "RecentMeUrlChatInvite": "recent_me_url_chat_invite",
    "RecentMeUrlStickerSet": "recent_me_url_sticker_set",
    "InputSingleMedia": "input_single_media",
    "WebAuthorization": "web_authorization",
    "InputMessageID": "input_message_id",
    "InputMessageReplyTo": "input_message_reply_to",
    "InputMessagePinned": "input_message_pinned",
    "InputMessageCallbackQuery": "input_message_callback_query",
    "InputDialogPeer": "input_dialog_peer",
    "InputDialogPeerFolder": "input_dialog_peer_folder",
    "DialogPeer": "dialog_peer",
    "DialogPeerFolder": "dialog_peer_folder",
    "FileHash": "file_hash",
    "InputClientProxy": "input_client_proxy",
    "InputSecureFileUploaded": "input_secure_file_uploaded",
    "InputSecureFile": "input_secure_file",
    "SecureFileEmpty": "secure_file_empty",
    "SecureFile": "secure_file",
    "SecureData": "secure_data",
    "SecurePlainPhone": "secure_plain_phone",
    "SecurePlainEmail": "secure_plain_email",
    "SecureValueTypePersonalDetails": "secure_value_type_personal_details",
    "SecureValueTypePassport": "secure_value_type_passport",
    "SecureValueTypeDriverLicense": "secure_value_type_driver_license",
    "SecureValueTypeIdentityCard": "secure_value_type_identity_card",
    "SecureValueTypeInternalPassport": "secure_value_type_internal_passport",
    "SecureValueTypeAddress": "secure_value_type_address",
    "SecureValueTypeUtilityBill": "secure_value_type_utility_bill",
    "SecureValueTypeBankStatement": "secure_value_type_bank_statement",
    "SecureValueTypeRentalAgreement": "secure_value_type_rental_agreement",
    "SecureValueTypePassportRegistration": "secure_value_type_passport_registration",
    "SecureValueTypeTemporaryRegistration": "secure_value_type_temporary_registration",
    "SecureValueTypePhone": "secure_value_type_phone",
    "SecureValueTypeEmail": "secure_value_type_email",
    "SecureValue": "secure_value",
    "InputSecureValue": "input_secure_value",
    "SecureValueHash": "secure_value_hash",
    "SecureValueErrorData": "secure_value_error_data",
    "SecureValueErrorFrontSide": "secure_value_error_front_side",
    "SecureValueErrorReverseSide": "secure_value_error_reverse_side",
    "SecureValueErrorSelfie": "secure_value_error_selfie",
    "SecureValueErrorFile": "secure_value_error_file",
    "SecureValueErrorFiles": "secure_value_error_files",
    "SecureValueError": "secure_value_error",
    "SecureValueErrorTranslationFile": "secure_value_error_translation_file",
    "SecureValueErrorTranslationFiles": "secure_value_error_translation_files",
    "SecureCredentialsEncrypted": "secure_credentials_encrypted",
    "SavedPhoneContact": "saved_phone_contact",
    "PasswordKdfAlgoUnknown": "password_kdf_algo_unknown",
    "PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow": "password_kdf_algo_sha256_sha256_pbkdf2_hmacsha512iter100000_sha256_mod_pow",
    "SecurePasswordKdfAlgoUnknown": "secure_password_kdf_algo_unknown",
    "SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000": "secure_password_kdf_algo_pbkdf2_hmacsha512iter100000",
    "SecurePasswordKdfAlgoSHA512": "secure_password_kdf_algo_sha512",
    "SecureSecretSettings": "secure_secret_settings",
    "InputCheckPasswordEmpty": "input_check_password_empty",
    "InputCheckPasswordSRP": "input_check_password_srp",
    "SecureRequiredType": "secure_required_type",
    "SecureRequiredTypeOneOf": "secure_required_type_one_of",
    "InputAppEvent": "input_app_event",
    "JsonObjectValue": "json_object_value",
    "JsonNull": "json_null",
    "JsonBool": "json_bool",
    "JsonNumber": "json_number",
    "JsonString": "json_string",
    "JsonArray": "json_array",
    "JsonObject": "json_object",
    "PageTableCell": "page_table_cell",
    "PageTableRow": "page_table_row",
    "PageCaption": "page_caption",
    "PageListItemText": "page_list_item_text",
    "PageListItemBlocks": "page_list_item_blocks",
    "PageListOrderedItemText": "page_list_ordered_item_text",
    "PageListOrderedItemBlocks": "page_list_ordered_item_blocks",
    "PageRelatedArticle": "page_related_article",
    "Page": "page",
    "PollAnswer": "poll_answer",
    "InputPollAnswer": "input_poll_answer",
    "Poll": "poll",
    "PollAnswerVoters": "poll_answer_voters",
    "PollResults": "poll_results",
    "ChatOnlines": "chat_onlines",
    "StatsURL": "stats_url",
    "ChatAdminRights": "chat_admin_rights",
    "ChatBannedRights": "chat_banned_rights",
    "InputWallPaper": "input_wall_paper",
    "InputWallPaperSlug": "input_wall_paper_slug",
    "InputWallPaperNoFile": "input_wall_paper_no_file",
    "CodeSettings": "code_settings",
    "WallPaperSettings": "wall_paper_settings",
    "AutoDownloadSettings": "auto_download_settings",
    "EmojiKeyword": "emoji_keyword",
    "EmojiKeywordDeleted": "emoji_keyword_deleted",
    "EmojiKeywordsDifference": "emoji_keywords_difference",
    "EmojiURL": "emoji_url",
    "EmojiLanguage": "emoji_language",
    "Folder": "folder",
    "InputFolderPeer": "input_folder_peer",
    "FolderPeer": "folder_peer",
    "UrlAuthResultRequest": "url_auth_result_request",
    "UrlAuthResultAccepted": "url_auth_result_accepted",
    "UrlAuthResultDefault": "url_auth_result_default",
    "ChannelLocationEmpty": "channel_location_empty",
    "ChannelLocation": "channel_location",
    "PeerLocated": "peer_located",
    "PeerSelfLocated": "peer_self_located",
    "RestrictionReason": "restriction_reason",
    "InputTheme": "input_theme",
    "InputThemeSlug": "input_theme_slug",
    "Theme": "theme",
    "BaseThemeClassic": "base_theme_classic",
    "BaseThemeDay": "base_theme_day",
    "BaseThemeNight": "base_theme_night",
    "BaseThemeTinted": "base_theme_tinted",
    "BaseThemeArctic": "base_theme_arctic",
    "InputThemeSettings": "input_theme_settings",
    "ThemeSettings": "theme_settings",
    "WebPageAttributeTheme": "web_page_attribute_theme",
    "WebPageAttributeStory": "web_page_attribute_story",
    "WebPageAttributeStickerSet": "web_page_attribute_sticker_set",
    "WebPageAttributeUniqueStarGift": "web_page_attribute_unique_star_gift",
    "WebPageAttributeStarGiftCollection": "web_page_attribute_star_gift_collection",
    "WebPageAttributeStarGiftAuction": "web_page_attribute_star_gift_auction",
    "WebPageAttributeAiComposeTone": "web_page_attribute_ai_compose_tone",
    "BankCardOpenUrl": "bank_card_open_url",
    "DialogFilter": "dialog_filter",
    "DialogFilterDefault": "dialog_filter_default",
    "DialogFilterChatlist": "dialog_filter_chatlist",
    "DialogFilterSuggested": "dialog_filter_suggested",
    "StatsDateRangeDays": "stats_date_range_days",
    "StatsAbsValueAndPrev": "stats_abs_value_and_prev",
    "StatsPercentValue": "stats_percent_value",
    "StatsGraphAsync": "stats_graph_async",
    "StatsGraphError": "stats_graph_error",
    "StatsGraph": "stats_graph",
    "VideoSize": "video_size",
    "VideoSizeEmojiMarkup": "video_size_emoji_markup",
    "VideoSizeStickerMarkup": "video_size_sticker_markup",
    "StatsGroupTopPoster": "stats_group_top_poster",
    "StatsGroupTopAdmin": "stats_group_top_admin",
    "StatsGroupTopInviter": "stats_group_top_inviter",
    "GlobalPrivacySettings": "global_privacy_settings",
    "MessageViews": "message_views",
    "MessageReplyHeader": "message_reply_header",
    "MessageReplyStoryHeader": "message_reply_story_header",
    "MessageReplies": "message_replies",
    "PeerBlocked": "peer_blocked",
    "GroupCallDiscarded": "group_call_discarded",
    "GroupCall": "group_call",
    "InputGroupCall": "input_group_call",
    "InputGroupCallSlug": "input_group_call_slug",
    "InputGroupCallInviteMessage": "input_group_call_invite_message",
    "GroupCallParticipant": "group_call_participant",
    "InlineQueryPeerTypeSameBotPM": "inline_query_peer_type_same_bot_pm",
    "InlineQueryPeerTypePM": "inline_query_peer_type_pm",
    "InlineQueryPeerTypeChat": "inline_query_peer_type_chat",
    "InlineQueryPeerTypeMegagroup": "inline_query_peer_type_megagroup",
    "InlineQueryPeerTypeBroadcast": "inline_query_peer_type_broadcast",
    "InlineQueryPeerTypeBotPM": "inline_query_peer_type_bot_pm",
    "ChatInviteImporter": "chat_invite_importer",
    "ChatAdminWithInvites": "chat_admin_with_invites",
    "GroupCallParticipantVideoSourceGroup": "group_call_participant_video_source_group",
    "GroupCallParticipantVideo": "group_call_participant_video",
    "BotCommandScopeDefault": "bot_command_scope_default",
    "BotCommandScopeUsers": "bot_command_scope_users",
    "BotCommandScopeChats": "bot_command_scope_chats",
    "BotCommandScopeChatAdmins": "bot_command_scope_chat_admins",
    "BotCommandScopePeer": "bot_command_scope_peer",
    "BotCommandScopePeerAdmins": "bot_command_scope_peer_admins",
    "BotCommandScopePeerUser": "bot_command_scope_peer_user",
    "ChatTheme": "chat_theme",
    "ChatThemeUniqueGift": "chat_theme_unique_gift",
    "SponsoredMessage": "sponsored_message",
    "SearchResultsCalendarPeriod": "search_results_calendar_period",
    "SearchResultPosition": "search_result_position",
    "ReactionCount": "reaction_count",
    "MessageReactions": "message_reactions",
    "AvailableReaction": "available_reaction",
    "MessagePeerReaction": "message_peer_reaction",
    "GroupCallStreamChannel": "group_call_stream_channel",
    "AttachMenuBotIconColor": "attach_menu_bot_icon_color",
    "AttachMenuBotIcon": "attach_menu_bot_icon",
    "AttachMenuBot": "attach_menu_bot",
    "AttachMenuBotsNotModified": "attach_menu_bots_not_modified",
    "AttachMenuBots": "attach_menu_bots",
    "AttachMenuBotsBot": "attach_menu_bots_bot",
    "WebViewResultUrl": "web_view_result_url",
    "WebViewMessageSent": "web_view_message_sent",
    "BotMenuButtonDefault": "bot_menu_button_default",
    "BotMenuButtonCommands": "bot_menu_button_commands",
    "BotMenuButton": "bot_menu_button",
    "NotificationSoundDefault": "notification_sound_default",
    "NotificationSoundNone": "notification_sound_none",
    "NotificationSoundLocal": "notification_sound_local",
    "NotificationSoundRingtone": "notification_sound_ringtone",
    "AttachMenuPeerTypeSameBotPM": "attach_menu_peer_type_same_bot_pm",
    "AttachMenuPeerTypeBotPM": "attach_menu_peer_type_bot_pm",
    "AttachMenuPeerTypePM": "attach_menu_peer_type_pm",
    "AttachMenuPeerTypeChat": "attach_menu_peer_type_chat",
    "AttachMenuPeerTypeBroadcast": "attach_menu_peer_type_broadcast",
    "InputInvoiceMessage": "input_invoice_message",
    "InputInvoiceSlug": "input_invoice_slug",
    "InputInvoicePremiumGiftCode": "input_invoice_premium_gift_code",
    "InputInvoiceStars": "input_invoice_stars",
    "InputInvoiceChatInviteSubscription": "input_invoice_chat_invite_subscription",
    "InputInvoiceStarGift": "input_invoice_star_gift",
    "InputInvoiceStarGiftUpgrade": "input_invoice_star_gift_upgrade",
    "InputInvoiceStarGiftTransfer": "input_invoice_star_gift_transfer",
    "InputInvoicePremiumGiftStars": "input_invoice_premium_gift_stars",
    "InputInvoiceBusinessBotTransferStars": "input_invoice_business_bot_transfer_stars",
    "InputInvoiceStarGiftResale": "input_invoice_star_gift_resale",
    "InputInvoiceStarGiftPrepaidUpgrade": "input_invoice_star_gift_prepaid_upgrade",
    "InputInvoicePremiumAuthCode": "input_invoice_premium_auth_code",
    "InputInvoiceStarGiftDropOriginalDetails": "input_invoice_star_gift_drop_original_details",
    "InputInvoiceStarGiftAuctionBid": "input_invoice_star_gift_auction_bid",
    "InputStorePaymentPremiumSubscription": "input_store_payment_premium_subscription",
    "InputStorePaymentGiftPremium": "input_store_payment_gift_premium",
    "InputStorePaymentPremiumGiftCode": "input_store_payment_premium_gift_code",
    "InputStorePaymentPremiumGiveaway": "input_store_payment_premium_giveaway",
    "InputStorePaymentStarsTopup": "input_store_payment_stars_topup",
    "InputStorePaymentStarsGift": "input_store_payment_stars_gift",
    "InputStorePaymentStarsGiveaway": "input_store_payment_stars_giveaway",
    "InputStorePaymentAuthCode": "input_store_payment_auth_code",
    "PaymentFormMethod": "payment_form_method",
    "EmojiStatusEmpty": "emoji_status_empty",
    "EmojiStatus": "emoji_status",
    "EmojiStatusCollectible": "emoji_status_collectible",
    "InputEmojiStatusCollectible": "input_emoji_status_collectible",
    "ReactionEmpty": "reaction_empty",
    "ReactionEmoji": "reaction_emoji",
    "ReactionCustomEmoji": "reaction_custom_emoji",
    "ReactionPaid": "reaction_paid",
    "ChatReactionsNone": "chat_reactions_none",
    "ChatReactionsAll": "chat_reactions_all",
    "ChatReactionsSome": "chat_reactions_some",
    "EmailVerifyPurposeLoginSetup": "email_verify_purpose_login_setup",
    "EmailVerifyPurposeLoginChange": "email_verify_purpose_login_change",
    "EmailVerifyPurposePassport": "email_verify_purpose_passport",
    "EmailVerificationCode": "email_verification_code",
    "EmailVerificationGoogle": "email_verification_google",
    "EmailVerificationApple": "email_verification_apple",
    "PremiumSubscriptionOption": "premium_subscription_option",
    "SendAsPeer": "send_as_peer",
    "MessageExtendedMediaPreview": "message_extended_media_preview",
    "MessageExtendedMedia": "message_extended_media",
    "StickerKeyword": "sticker_keyword",
    "Username": "username",
    "ForumTopicDeleted": "forum_topic_deleted",
    "ForumTopic": "forum_topic",
    "DefaultHistoryTTL": "default_history_ttl",
    "ExportedContactToken": "exported_contact_token",
    "RequestPeerTypeUser": "request_peer_type_user",
    "RequestPeerTypeChat": "request_peer_type_chat",
    "RequestPeerTypeBroadcast": "request_peer_type_broadcast",
    "RequestPeerTypeCreateBot": "request_peer_type_create_bot",
    "EmojiListNotModified": "emoji_list_not_modified",
    "EmojiList": "emoji_list",
    "EmojiGroup": "emoji_group",
    "EmojiGroupGreeting": "emoji_group_greeting",
    "EmojiGroupPremium": "emoji_group_premium",
    "TextWithEntities": "text_with_entities",
    "AutoSaveSettings": "auto_save_settings",
    "AutoSaveException": "auto_save_exception",
    "InputBotAppID": "input_bot_app_id",
    "InputBotAppShortName": "input_bot_app_short_name",
    "BotAppNotModified": "bot_app_not_modified",
    "BotApp": "bot_app",
    "InlineBotWebView": "inline_bot_web_view",
    "ReadParticipantDate": "read_participant_date",
    "InputChatlistDialogFilter": "input_chatlist_dialog_filter",
    "ExportedChatlistInvite": "exported_chatlist_invite",
    "MessagePeerVote": "message_peer_vote",
    "MessagePeerVoteInputOption": "message_peer_vote_input_option",
    "MessagePeerVoteMultiple": "message_peer_vote_multiple",
    "StoryViews": "story_views",
    "StoryItemDeleted": "story_item_deleted",
    "StoryItemSkipped": "story_item_skipped",
    "StoryItem": "story_item",
    "StoryView": "story_view",
    "StoryViewPublicForward": "story_view_public_forward",
    "StoryViewPublicRepost": "story_view_public_repost",
    "InputReplyToMessage": "input_reply_to_message",
    "InputReplyToStory": "input_reply_to_story",
    "InputReplyToMonoForum": "input_reply_to_mono_forum",
    "ExportedStoryLink": "exported_story_link",
    "StoriesStealthMode": "stories_stealth_mode",
    "MediaAreaCoordinates": "media_area_coordinates",
    "MediaAreaVenue": "media_area_venue",
    "InputMediaAreaVenue": "input_media_area_venue",
    "MediaAreaGeoPoint": "media_area_geo_point",
    "MediaAreaSuggestedReaction": "media_area_suggested_reaction",
    "MediaAreaChannelPost": "media_area_channel_post",
    "InputMediaAreaChannelPost": "input_media_area_channel_post",
    "MediaAreaUrl": "media_area_url",
    "MediaAreaWeather": "media_area_weather",
    "MediaAreaStarGift": "media_area_star_gift",
    "PeerStories": "peer_stories",
    "PremiumGiftCodeOption": "premium_gift_code_option",
    "PrepaidGiveaway": "prepaid_giveaway",
    "PrepaidStarsGiveaway": "prepaid_stars_giveaway",
    "Boost": "boost",
    "MyBoost": "my_boost",
    "StoryFwdHeader": "story_fwd_header",
    "PostInteractionCountersMessage": "post_interaction_counters_message",
    "PostInteractionCountersStory": "post_interaction_counters_story",
    "PublicForwardMessage": "public_forward_message",
    "PublicForwardStory": "public_forward_story",
    "PeerColor": "peer_color",
    "PeerColorCollectible": "peer_color_collectible",
    "InputPeerColorCollectible": "input_peer_color_collectible",
    "StoryReaction": "story_reaction",
    "StoryReactionPublicForward": "story_reaction_public_forward",
    "StoryReactionPublicRepost": "story_reaction_public_repost",
    "SavedDialog": "saved_dialog",
    "MonoForumDialog": "mono_forum_dialog",
    "SavedReactionTag": "saved_reaction_tag",
    "OutboxReadDate": "outbox_read_date",
    "SmsJob": "sms_job",
    "BusinessWeeklyOpen": "business_weekly_open",
    "BusinessWorkHours": "business_work_hours",
    "BusinessLocation": "business_location",
    "InputBusinessRecipients": "input_business_recipients",
    "BusinessRecipients": "business_recipients",
    "BusinessAwayMessageScheduleAlways": "business_away_message_schedule_always",
    "BusinessAwayMessageScheduleOutsideWorkHours": "business_away_message_schedule_outside_work_hours",
    "BusinessAwayMessageScheduleCustom": "business_away_message_schedule_custom",
    "InputBusinessGreetingMessage": "input_business_greeting_message",
    "BusinessGreetingMessage": "business_greeting_message",
    "InputBusinessAwayMessage": "input_business_away_message",
    "BusinessAwayMessage": "business_away_message",
    "Timezone": "timezone",
    "QuickReply": "quick_reply",
    "InputQuickReplyShortcut": "input_quick_reply_shortcut",
    "InputQuickReplyShortcutId": "input_quick_reply_shortcut_id",
    "ConnectedBot": "connected_bot",
    "Birthday": "birthday",
    "BotBusinessConnection": "bot_business_connection",
    "InputBusinessIntro": "input_business_intro",
    "BusinessIntro": "business_intro",
    "InputCollectibleUsername": "input_collectible_username",
    "InputCollectiblePhone": "input_collectible_phone",
    "InputBusinessBotRecipients": "input_business_bot_recipients",
    "BusinessBotRecipients": "business_bot_recipients",
    "ContactBirthday": "contact_birthday",
    "MissingInvitee": "missing_invitee",
    "InputBusinessChatLink": "input_business_chat_link",
    "BusinessChatLink": "business_chat_link",
    "RequestedPeerUser": "requested_peer_user",
    "RequestedPeerChat": "requested_peer_chat",
    "RequestedPeerChannel": "requested_peer_channel",
    "SponsoredMessageReportOption": "sponsored_message_report_option",
    "ReactionNotificationsFromContacts": "reaction_notifications_from_contacts",
    "ReactionNotificationsFromAll": "reaction_notifications_from_all",
    "ReactionsNotifySettings": "reactions_notify_settings",
    "AvailableEffect": "available_effect",
    "FactCheck": "fact_check",
    "StarsTransactionPeerUnsupported": "stars_transaction_peer_unsupported",
    "StarsTransactionPeerAppStore": "stars_transaction_peer_app_store",
    "StarsTransactionPeerPlayMarket": "stars_transaction_peer_play_market",
    "StarsTransactionPeerPremiumBot": "stars_transaction_peer_premium_bot",
    "StarsTransactionPeerFragment": "stars_transaction_peer_fragment",
    "StarsTransactionPeer": "stars_transaction_peer",
    "StarsTransactionPeerAds": "stars_transaction_peer_ads",
    "StarsTransactionPeerAPI": "stars_transaction_peer_api",
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
    "StarGiftUnique": "star_gift_unique",
    "MessageReportOption": "message_report_option",
    "ReportResultChooseOption": "report_result_choose_option",
    "ReportResultAddComment": "report_result_add_comment",
    "ReportResultReported": "report_result_reported",
    "BotAppSettings": "bot_app_settings",
    "StarRefProgram": "star_ref_program",
    "ConnectedBotStarRef": "connected_bot_star_ref",
    "StarsAmount": "stars_amount",
    "StarsTonAmount": "stars_ton_amount",
    "BotVerifierSettings": "bot_verifier_settings",
    "BotVerification": "bot_verification",
    "StarGiftAttributeModel": "star_gift_attribute_model",
    "StarGiftAttributePattern": "star_gift_attribute_pattern",
    "StarGiftAttributeBackdrop": "star_gift_attribute_backdrop",
    "StarGiftAttributeOriginalDetails": "star_gift_attribute_original_details",
    "SavedStarGift": "saved_star_gift",
    "InputSavedStarGiftUser": "input_saved_star_gift_user",
    "InputSavedStarGiftChat": "input_saved_star_gift_chat",
    "InputSavedStarGiftSlug": "input_saved_star_gift_slug",
    "PaidReactionPrivacyDefault": "paid_reaction_privacy_default",
    "PaidReactionPrivacyAnonymous": "paid_reaction_privacy_anonymous",
    "PaidReactionPrivacyPeer": "paid_reaction_privacy_peer",
    "RequirementToContactEmpty": "requirement_to_contact_empty",
    "RequirementToContactPremium": "requirement_to_contact_premium",
    "RequirementToContactPaidMessages": "requirement_to_contact_paid_messages",
    "BusinessBotRights": "business_bot_rights",
    "DisallowedGiftsSettings": "disallowed_gifts_settings",
    "SponsoredPeer": "sponsored_peer",
    "StarGiftAttributeIdModel": "star_gift_attribute_id_model",
    "StarGiftAttributeIdPattern": "star_gift_attribute_id_pattern",
    "StarGiftAttributeIdBackdrop": "star_gift_attribute_id_backdrop",
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
    "ProfileTabPosts": "profile_tab_posts",
    "ProfileTabGifts": "profile_tab_gifts",
    "ProfileTabMedia": "profile_tab_media",
    "ProfileTabFiles": "profile_tab_files",
    "ProfileTabMusic": "profile_tab_music",
    "ProfileTabVoice": "profile_tab_voice",
    "ProfileTabLinks": "profile_tab_links",
    "ProfileTabGifs": "profile_tab_gifs",
    "InputChatThemeEmpty": "input_chat_theme_empty",
    "InputChatTheme": "input_chat_theme",
    "InputChatThemeUniqueGift": "input_chat_theme_unique_gift",
    "StarGiftUpgradePrice": "star_gift_upgrade_price",
    "GroupCallMessage": "group_call_message",
    "GroupCallDonor": "group_call_donor",
    "RecentStory": "recent_story",
    "AuctionBidLevel": "auction_bid_level",
    "StarGiftAuctionStateNotModified": "star_gift_auction_state_not_modified",
    "StarGiftAuctionState": "star_gift_auction_state",
    "StarGiftAuctionStateFinished": "star_gift_auction_state_finished",
    "StarGiftAuctionUserState": "star_gift_auction_user_state",
    "StarGiftAuctionAcquiredGift": "star_gift_auction_acquired_gift",
    "StarGiftActiveAuctionState": "star_gift_active_auction_state",
    "InputStarGiftAuction": "input_star_gift_auction",
    "InputStarGiftAuctionSlug": "input_star_gift_auction_slug",
    "Passkey": "passkey",
    "InputPasskeyResponseRegister": "input_passkey_response_register",
    "InputPasskeyResponseLogin": "input_passkey_response_login",
    "InputPasskeyCredentialPublicKey": "input_passkey_credential_public_key",
    "InputPasskeyCredentialFirebasePNV": "input_passkey_credential_firebase_pnv",
    "StarGiftBackground": "star_gift_background",
    "StarGiftAuctionRound": "star_gift_auction_round",
    "StarGiftAuctionRoundExtendable": "star_gift_auction_round_extendable",
    "StarGiftAttributeRarity": "star_gift_attribute_rarity",
    "StarGiftAttributeRarityUncommon": "star_gift_attribute_rarity_uncommon",
    "StarGiftAttributeRarityRare": "star_gift_attribute_rarity_rare",
    "StarGiftAttributeRarityEpic": "star_gift_attribute_rarity_epic",
    "StarGiftAttributeRarityLegendary": "star_gift_attribute_rarity_legendary",
    "KeyboardButtonStyle": "keyboard_button_style",
    "InputMessageReadMetric": "input_message_read_metric",
    "InputAiComposeToneDefault": "input_ai_compose_tone_default",
    "InputAiComposeToneID": "input_ai_compose_tone_id",
    "InputAiComposeToneSlug": "input_ai_compose_tone_slug",
    "AiComposeTone": "ai_compose_tone",
    "AiComposeToneDefault": "ai_compose_tone_default",
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
    from .pq_inner_data_dc import PQInnerDataDc
    from .pq_inner_data_temp import PQInnerDataTemp
    from .pq_inner_data_temp_dc import PQInnerDataTempDc
    from .bind_auth_key_inner import BindAuthKeyInner
    from .server_dh_params_fail import ServerDHParamsFail
    from .server_dh_params_ok import ServerDHParamsOk
    from .server_dh_inner_data import ServerDHInnerData
    from .client_dh_inner_data import ClientDHInnerData
    from .dh_gen_ok import DhGenOk
    from .dh_gen_retry import DhGenRetry
    from .dh_gen_fail import DhGenFail
    from .destroy_auth_key_ok import DestroyAuthKeyOk
    from .destroy_auth_key_none import DestroyAuthKeyNone
    from .destroy_auth_key_fail import DestroyAuthKeyFail
    from .msgs_ack import MsgsAck
    from .bad_msg_notification import BadMsgNotification
    from .bad_server_salt import BadServerSalt
    from .msgs_state_req import MsgsStateReq
    from .msgs_state_info import MsgsStateInfo
    from .msgs_all_info import MsgsAllInfo
    from .msg_detailed_info import MsgDetailedInfo
    from .msg_new_detailed_info import MsgNewDetailedInfo
    from .msg_resend_req import MsgResendReq
    from .msg_resend_ans_req import MsgResendAnsReq
    from .rpc_result import RpcResult
    from .rpc_error import RpcError
    from .rpc_answer_unknown import RpcAnswerUnknown
    from .rpc_answer_dropped_running import RpcAnswerDroppedRunning
    from .rpc_answer_dropped import RpcAnswerDropped
    from .pong import Pong
    from .destroy_session_ok import DestroySessionOk
    from .destroy_session_none import DestroySessionNone
    from .new_session_created import NewSessionCreated
    from .http_wait import HttpWait
    from .ip_port import IpPort
    from .ip_port_secret import IpPortSecret
    from .access_point_rule import AccessPointRule
    from .input_peer_empty import InputPeerEmpty
    from .input_peer_self import InputPeerSelf
    from .input_peer_chat import InputPeerChat
    from .input_peer_user import InputPeerUser
    from .input_peer_channel import InputPeerChannel
    from .input_peer_user_from_message import InputPeerUserFromMessage
    from .input_peer_channel_from_message import InputPeerChannelFromMessage
    from .input_user_empty import InputUserEmpty
    from .input_user_self import InputUserSelf
    from .input_user import InputUser
    from .input_user_from_message import InputUserFromMessage
    from .input_phone_contact import InputPhoneContact
    from .input_file import InputFile
    from .input_file_big import InputFileBig
    from .input_file_story_document import InputFileStoryDocument
    from .input_media_empty import InputMediaEmpty
    from .input_media_uploaded_photo import InputMediaUploadedPhoto
    from .input_media_photo import InputMediaPhoto
    from .input_media_geo_point import InputMediaGeoPoint
    from .input_media_contact import InputMediaContact
    from .input_media_uploaded_document import InputMediaUploadedDocument
    from .input_media_document import InputMediaDocument
    from .input_media_venue import InputMediaVenue
    from .input_media_photo_external import InputMediaPhotoExternal
    from .input_media_document_external import InputMediaDocumentExternal
    from .input_media_game import InputMediaGame
    from .input_media_invoice import InputMediaInvoice
    from .input_media_geo_live import InputMediaGeoLive
    from .input_media_poll import InputMediaPoll
    from .input_media_dice import InputMediaDice
    from .input_media_story import InputMediaStory
    from .input_media_web_page import InputMediaWebPage
    from .input_media_paid_media import InputMediaPaidMedia
    from .input_media_todo import InputMediaTodo
    from .input_media_stake_dice import InputMediaStakeDice
    from .input_chat_photo_empty import InputChatPhotoEmpty
    from .input_chat_uploaded_photo import InputChatUploadedPhoto
    from .input_chat_photo import InputChatPhoto
    from .input_geo_point_empty import InputGeoPointEmpty
    from .input_geo_point import InputGeoPoint
    from .input_photo_empty import InputPhotoEmpty
    from .input_photo import InputPhoto
    from .input_file_location import InputFileLocation
    from .input_encrypted_file_location import InputEncryptedFileLocation
    from .input_document_file_location import InputDocumentFileLocation
    from .input_secure_file_location import InputSecureFileLocation
    from .input_takeout_file_location import InputTakeoutFileLocation
    from .input_photo_file_location import InputPhotoFileLocation
    from .input_photo_legacy_file_location import InputPhotoLegacyFileLocation
    from .input_peer_photo_file_location import InputPeerPhotoFileLocation
    from .input_sticker_set_thumb import InputStickerSetThumb
    from .input_group_call_stream import InputGroupCallStream
    from .peer_user import PeerUser
    from .peer_chat import PeerChat
    from .peer_channel import PeerChannel
    from .user_empty import UserEmpty
    from .user import User
    from .user_profile_photo_empty import UserProfilePhotoEmpty
    from .user_profile_photo import UserProfilePhoto
    from .user_status_empty import UserStatusEmpty
    from .user_status_online import UserStatusOnline
    from .user_status_offline import UserStatusOffline
    from .user_status_recently import UserStatusRecently
    from .user_status_last_week import UserStatusLastWeek
    from .user_status_last_month import UserStatusLastMonth
    from .chat_empty import ChatEmpty
    from .chat import Chat
    from .chat_forbidden import ChatForbidden
    from .channel import Channel
    from .channel_forbidden import ChannelForbidden
    from .chat_full import ChatFull
    from .channel_full import ChannelFull
    from .chat_participant import ChatParticipant
    from .chat_participant_creator import ChatParticipantCreator
    from .chat_participant_admin import ChatParticipantAdmin
    from .chat_participants_forbidden import ChatParticipantsForbidden
    from .chat_participants import ChatParticipants
    from .chat_photo_empty import ChatPhotoEmpty
    from .chat_photo import ChatPhoto
    from .message_empty import MessageEmpty
    from .message import Message
    from .message_service import MessageService
    from .message_media_empty import MessageMediaEmpty
    from .message_media_photo import MessageMediaPhoto
    from .message_media_geo import MessageMediaGeo
    from .message_media_contact import MessageMediaContact
    from .message_media_unsupported import MessageMediaUnsupported
    from .message_media_document import MessageMediaDocument
    from .message_media_web_page import MessageMediaWebPage
    from .message_media_venue import MessageMediaVenue
    from .message_media_game import MessageMediaGame
    from .message_media_invoice import MessageMediaInvoice
    from .message_media_geo_live import MessageMediaGeoLive
    from .message_media_poll import MessageMediaPoll
    from .message_media_dice import MessageMediaDice
    from .message_media_story import MessageMediaStory
    from .message_media_giveaway import MessageMediaGiveaway
    from .message_media_giveaway_results import MessageMediaGiveawayResults
    from .message_media_paid_media import MessageMediaPaidMedia
    from .message_media_to_do import MessageMediaToDo
    from .message_media_video_stream import MessageMediaVideoStream
    from .message_action_empty import MessageActionEmpty
    from .message_action_chat_create import MessageActionChatCreate
    from .message_action_chat_edit_title import MessageActionChatEditTitle
    from .message_action_chat_edit_photo import MessageActionChatEditPhoto
    from .message_action_chat_delete_photo import MessageActionChatDeletePhoto
    from .message_action_chat_add_user import MessageActionChatAddUser
    from .message_action_chat_delete_user import MessageActionChatDeleteUser
    from .message_action_chat_joined_by_link import MessageActionChatJoinedByLink
    from .message_action_channel_create import MessageActionChannelCreate
    from .message_action_chat_migrate_to import MessageActionChatMigrateTo
    from .message_action_channel_migrate_from import MessageActionChannelMigrateFrom
    from .message_action_pin_message import MessageActionPinMessage
    from .message_action_history_clear import MessageActionHistoryClear
    from .message_action_game_score import MessageActionGameScore
    from .message_action_payment_sent_me import MessageActionPaymentSentMe
    from .message_action_payment_sent import MessageActionPaymentSent
    from .message_action_phone_call import MessageActionPhoneCall
    from .message_action_screenshot_taken import MessageActionScreenshotTaken
    from .message_action_custom_action import MessageActionCustomAction
    from .message_action_bot_allowed import MessageActionBotAllowed
    from .message_action_secure_values_sent_me import MessageActionSecureValuesSentMe
    from .message_action_secure_values_sent import MessageActionSecureValuesSent
    from .message_action_contact_sign_up import MessageActionContactSignUp
    from .message_action_geo_proximity_reached import MessageActionGeoProximityReached
    from .message_action_group_call import MessageActionGroupCall
    from .message_action_invite_to_group_call import MessageActionInviteToGroupCall
    from .message_action_set_messages_ttl import MessageActionSetMessagesTTL
    from .message_action_group_call_scheduled import MessageActionGroupCallScheduled
    from .message_action_set_chat_theme import MessageActionSetChatTheme
    from .message_action_chat_joined_by_request import MessageActionChatJoinedByRequest
    from .message_action_web_view_data_sent_me import MessageActionWebViewDataSentMe
    from .message_action_web_view_data_sent import MessageActionWebViewDataSent
    from .message_action_gift_premium import MessageActionGiftPremium
    from .message_action_topic_create import MessageActionTopicCreate
    from .message_action_topic_edit import MessageActionTopicEdit
    from .message_action_suggest_profile_photo import MessageActionSuggestProfilePhoto
    from .message_action_requested_peer import MessageActionRequestedPeer
    from .message_action_set_chat_wall_paper import MessageActionSetChatWallPaper
    from .message_action_gift_code import MessageActionGiftCode
    from .message_action_giveaway_launch import MessageActionGiveawayLaunch
    from .message_action_giveaway_results import MessageActionGiveawayResults
    from .message_action_boost_apply import MessageActionBoostApply
    from .message_action_requested_peer_sent_me import MessageActionRequestedPeerSentMe
    from .message_action_payment_refunded import MessageActionPaymentRefunded
    from .message_action_gift_stars import MessageActionGiftStars
    from .message_action_prize_stars import MessageActionPrizeStars
    from .message_action_star_gift import MessageActionStarGift
    from .message_action_star_gift_unique import MessageActionStarGiftUnique
    from .message_action_paid_messages_refunded import MessageActionPaidMessagesRefunded
    from .message_action_paid_messages_price import MessageActionPaidMessagesPrice
    from .message_action_conference_call import MessageActionConferenceCall
    from .message_action_todo_completions import MessageActionTodoCompletions
    from .message_action_todo_append_tasks import MessageActionTodoAppendTasks
    from .message_action_suggested_post_approval import MessageActionSuggestedPostApproval
    from .message_action_suggested_post_success import MessageActionSuggestedPostSuccess
    from .message_action_suggested_post_refund import MessageActionSuggestedPostRefund
    from .message_action_gift_ton import MessageActionGiftTon
    from .message_action_suggest_birthday import MessageActionSuggestBirthday
    from .message_action_star_gift_purchase_offer import MessageActionStarGiftPurchaseOffer
    from .message_action_star_gift_purchase_offer_declined import MessageActionStarGiftPurchaseOfferDeclined
    from .message_action_new_creator_pending import MessageActionNewCreatorPending
    from .message_action_change_creator import MessageActionChangeCreator
    from .message_action_no_forwards_toggle import MessageActionNoForwardsToggle
    from .message_action_no_forwards_request import MessageActionNoForwardsRequest
    from .message_action_poll_append_answer import MessageActionPollAppendAnswer
    from .message_action_poll_delete_answer import MessageActionPollDeleteAnswer
    from .message_action_managed_bot_created import MessageActionManagedBotCreated
    from .dialog import Dialog
    from .dialog_folder import DialogFolder
    from .photo_empty import PhotoEmpty
    from .photo import Photo
    from .photo_size_empty import PhotoSizeEmpty
    from .photo_size import PhotoSize
    from .photo_cached_size import PhotoCachedSize
    from .photo_stripped_size import PhotoStrippedSize
    from .photo_size_progressive import PhotoSizeProgressive
    from .photo_path_size import PhotoPathSize
    from .geo_point_empty import GeoPointEmpty
    from .geo_point import GeoPoint
    from .input_notify_peer import InputNotifyPeer
    from .input_notify_users import InputNotifyUsers
    from .input_notify_chats import InputNotifyChats
    from .input_notify_broadcasts import InputNotifyBroadcasts
    from .input_notify_forum_topic import InputNotifyForumTopic
    from .input_peer_notify_settings import InputPeerNotifySettings
    from .peer_notify_settings import PeerNotifySettings
    from .peer_settings import PeerSettings
    from .wall_paper import WallPaper
    from .wall_paper_no_file import WallPaperNoFile
    from .input_report_reason_spam import InputReportReasonSpam
    from .input_report_reason_violence import InputReportReasonViolence
    from .input_report_reason_pornography import InputReportReasonPornography
    from .input_report_reason_child_abuse import InputReportReasonChildAbuse
    from .input_report_reason_other import InputReportReasonOther
    from .input_report_reason_copyright import InputReportReasonCopyright
    from .input_report_reason_geo_irrelevant import InputReportReasonGeoIrrelevant
    from .input_report_reason_fake import InputReportReasonFake
    from .input_report_reason_illegal_drugs import InputReportReasonIllegalDrugs
    from .input_report_reason_personal_details import InputReportReasonPersonalDetails
    from .user_full import UserFull
    from .contact import Contact
    from .imported_contact import ImportedContact
    from .contact_status import ContactStatus
    from .input_messages_filter_empty import InputMessagesFilterEmpty
    from .input_messages_filter_photos import InputMessagesFilterPhotos
    from .input_messages_filter_video import InputMessagesFilterVideo
    from .input_messages_filter_photo_video import InputMessagesFilterPhotoVideo
    from .input_messages_filter_document import InputMessagesFilterDocument
    from .input_messages_filter_url import InputMessagesFilterUrl
    from .input_messages_filter_gif import InputMessagesFilterGif
    from .input_messages_filter_voice import InputMessagesFilterVoice
    from .input_messages_filter_music import InputMessagesFilterMusic
    from .input_messages_filter_chat_photos import InputMessagesFilterChatPhotos
    from .input_messages_filter_phone_calls import InputMessagesFilterPhoneCalls
    from .input_messages_filter_round_voice import InputMessagesFilterRoundVoice
    from .input_messages_filter_round_video import InputMessagesFilterRoundVideo
    from .input_messages_filter_my_mentions import InputMessagesFilterMyMentions
    from .input_messages_filter_geo import InputMessagesFilterGeo
    from .input_messages_filter_contacts import InputMessagesFilterContacts
    from .input_messages_filter_pinned import InputMessagesFilterPinned
    from .input_messages_filter_poll import InputMessagesFilterPoll
    from .update_new_message import UpdateNewMessage
    from .update_message_id import UpdateMessageID
    from .update_delete_messages import UpdateDeleteMessages
    from .update_user_typing import UpdateUserTyping
    from .update_chat_user_typing import UpdateChatUserTyping
    from .update_chat_participants import UpdateChatParticipants
    from .update_user_status import UpdateUserStatus
    from .update_user_name import UpdateUserName
    from .update_new_authorization import UpdateNewAuthorization
    from .update_new_encrypted_message import UpdateNewEncryptedMessage
    from .update_encrypted_chat_typing import UpdateEncryptedChatTyping
    from .update_encryption import UpdateEncryption
    from .update_encrypted_messages_read import UpdateEncryptedMessagesRead
    from .update_chat_participant_add import UpdateChatParticipantAdd
    from .update_chat_participant_delete import UpdateChatParticipantDelete
    from .update_dc_options import UpdateDcOptions
    from .update_notify_settings import UpdateNotifySettings
    from .update_service_notification import UpdateServiceNotification
    from .update_privacy import UpdatePrivacy
    from .update_user_phone import UpdateUserPhone
    from .update_read_history_inbox import UpdateReadHistoryInbox
    from .update_read_history_outbox import UpdateReadHistoryOutbox
    from .update_web_page import UpdateWebPage
    from .update_read_messages_contents import UpdateReadMessagesContents
    from .update_channel_too_long import UpdateChannelTooLong
    from .update_channel import UpdateChannel
    from .update_new_channel_message import UpdateNewChannelMessage
    from .update_read_channel_inbox import UpdateReadChannelInbox
    from .update_delete_channel_messages import UpdateDeleteChannelMessages
    from .update_channel_message_views import UpdateChannelMessageViews
    from .update_chat_participant_admin import UpdateChatParticipantAdmin
    from .update_new_sticker_set import UpdateNewStickerSet
    from .update_sticker_sets_order import UpdateStickerSetsOrder
    from .update_sticker_sets import UpdateStickerSets
    from .update_saved_gifs import UpdateSavedGifs
    from .update_bot_inline_query import UpdateBotInlineQuery
    from .update_bot_inline_send import UpdateBotInlineSend
    from .update_edit_channel_message import UpdateEditChannelMessage
    from .update_bot_callback_query import UpdateBotCallbackQuery
    from .update_edit_message import UpdateEditMessage
    from .update_inline_bot_callback_query import UpdateInlineBotCallbackQuery
    from .update_read_channel_outbox import UpdateReadChannelOutbox
    from .update_draft_message import UpdateDraftMessage
    from .update_read_featured_stickers import UpdateReadFeaturedStickers
    from .update_recent_stickers import UpdateRecentStickers
    from .update_config import UpdateConfig
    from .update_pts_changed import UpdatePtsChanged
    from .update_channel_web_page import UpdateChannelWebPage
    from .update_dialog_pinned import UpdateDialogPinned
    from .update_pinned_dialogs import UpdatePinnedDialogs
    from .update_bot_webhook_json import UpdateBotWebhookJSON
    from .update_bot_webhook_json_query import UpdateBotWebhookJSONQuery
    from .update_bot_shipping_query import UpdateBotShippingQuery
    from .update_bot_precheckout_query import UpdateBotPrecheckoutQuery
    from .update_phone_call import UpdatePhoneCall
    from .update_lang_pack_too_long import UpdateLangPackTooLong
    from .update_lang_pack import UpdateLangPack
    from .update_faved_stickers import UpdateFavedStickers
    from .update_channel_read_messages_contents import UpdateChannelReadMessagesContents
    from .update_contacts_reset import UpdateContactsReset
    from .update_channel_available_messages import UpdateChannelAvailableMessages
    from .update_dialog_unread_mark import UpdateDialogUnreadMark
    from .update_message_poll import UpdateMessagePoll
    from .update_chat_default_banned_rights import UpdateChatDefaultBannedRights
    from .update_folder_peers import UpdateFolderPeers
    from .update_peer_settings import UpdatePeerSettings
    from .update_peer_located import UpdatePeerLocated
    from .update_new_scheduled_message import UpdateNewScheduledMessage
    from .update_delete_scheduled_messages import UpdateDeleteScheduledMessages
    from .update_theme import UpdateTheme
    from .update_geo_live_viewed import UpdateGeoLiveViewed
    from .update_login_token import UpdateLoginToken
    from .update_message_poll_vote import UpdateMessagePollVote
    from .update_dialog_filter import UpdateDialogFilter
    from .update_dialog_filter_order import UpdateDialogFilterOrder
    from .update_dialog_filters import UpdateDialogFilters
    from .update_phone_call_signaling_data import UpdatePhoneCallSignalingData
    from .update_channel_message_forwards import UpdateChannelMessageForwards
    from .update_read_channel_discussion_inbox import UpdateReadChannelDiscussionInbox
    from .update_read_channel_discussion_outbox import UpdateReadChannelDiscussionOutbox
    from .update_peer_blocked import UpdatePeerBlocked
    from .update_channel_user_typing import UpdateChannelUserTyping
    from .update_pinned_messages import UpdatePinnedMessages
    from .update_pinned_channel_messages import UpdatePinnedChannelMessages
    from .update_chat import UpdateChat
    from .update_group_call_participants import UpdateGroupCallParticipants
    from .update_group_call import UpdateGroupCall
    from .update_peer_history_ttl import UpdatePeerHistoryTTL
    from .update_chat_participant import UpdateChatParticipant
    from .update_channel_participant import UpdateChannelParticipant
    from .update_bot_stopped import UpdateBotStopped
    from .update_group_call_connection import UpdateGroupCallConnection
    from .update_bot_commands import UpdateBotCommands
    from .update_pending_join_requests import UpdatePendingJoinRequests
    from .update_bot_chat_invite_requester import UpdateBotChatInviteRequester
    from .update_message_reactions import UpdateMessageReactions
    from .update_attach_menu_bots import UpdateAttachMenuBots
    from .update_web_view_result_sent import UpdateWebViewResultSent
    from .update_bot_menu_button import UpdateBotMenuButton
    from .update_saved_ringtones import UpdateSavedRingtones
    from .update_transcribed_audio import UpdateTranscribedAudio
    from .update_read_featured_emoji_stickers import UpdateReadFeaturedEmojiStickers
    from .update_user_emoji_status import UpdateUserEmojiStatus
    from .update_recent_emoji_statuses import UpdateRecentEmojiStatuses
    from .update_recent_reactions import UpdateRecentReactions
    from .update_move_sticker_set_to_top import UpdateMoveStickerSetToTop
    from .update_message_extended_media import UpdateMessageExtendedMedia
    from .update_user import UpdateUser
    from .update_auto_save_settings import UpdateAutoSaveSettings
    from .update_story import UpdateStory
    from .update_read_stories import UpdateReadStories
    from .update_story_id import UpdateStoryID
    from .update_stories_stealth_mode import UpdateStoriesStealthMode
    from .update_sent_story_reaction import UpdateSentStoryReaction
    from .update_bot_chat_boost import UpdateBotChatBoost
    from .update_channel_view_forum_as_messages import UpdateChannelViewForumAsMessages
    from .update_peer_wallpaper import UpdatePeerWallpaper
    from .update_bot_message_reaction import UpdateBotMessageReaction
    from .update_bot_message_reactions import UpdateBotMessageReactions
    from .update_saved_dialog_pinned import UpdateSavedDialogPinned
    from .update_pinned_saved_dialogs import UpdatePinnedSavedDialogs
    from .update_saved_reaction_tags import UpdateSavedReactionTags
    from .update_sms_job import UpdateSmsJob
    from .update_quick_replies import UpdateQuickReplies
    from .update_new_quick_reply import UpdateNewQuickReply
    from .update_delete_quick_reply import UpdateDeleteQuickReply
    from .update_quick_reply_message import UpdateQuickReplyMessage
    from .update_delete_quick_reply_messages import UpdateDeleteQuickReplyMessages
    from .update_bot_business_connect import UpdateBotBusinessConnect
    from .update_bot_new_business_message import UpdateBotNewBusinessMessage
    from .update_bot_edit_business_message import UpdateBotEditBusinessMessage
    from .update_bot_delete_business_message import UpdateBotDeleteBusinessMessage
    from .update_new_story_reaction import UpdateNewStoryReaction
    from .update_stars_balance import UpdateStarsBalance
    from .update_business_bot_callback_query import UpdateBusinessBotCallbackQuery
    from .update_stars_revenue_status import UpdateStarsRevenueStatus
    from .update_bot_purchased_paid_media import UpdateBotPurchasedPaidMedia
    from .update_paid_reaction_privacy import UpdatePaidReactionPrivacy
    from .update_sent_phone_code import UpdateSentPhoneCode
    from .update_group_call_chain_blocks import UpdateGroupCallChainBlocks
    from .update_read_mono_forum_inbox import UpdateReadMonoForumInbox
    from .update_read_mono_forum_outbox import UpdateReadMonoForumOutbox
    from .update_mono_forum_no_paid_exception import UpdateMonoForumNoPaidException
    from .update_group_call_message import UpdateGroupCallMessage
    from .update_group_call_encrypted_message import UpdateGroupCallEncryptedMessage
    from .update_pinned_forum_topic import UpdatePinnedForumTopic
    from .update_pinned_forum_topics import UpdatePinnedForumTopics
    from .update_delete_group_call_messages import UpdateDeleteGroupCallMessages
    from .update_star_gift_auction_state import UpdateStarGiftAuctionState
    from .update_star_gift_auction_user_state import UpdateStarGiftAuctionUserState
    from .update_emoji_game_info import UpdateEmojiGameInfo
    from .update_star_gift_craft_fail import UpdateStarGiftCraftFail
    from .update_chat_participant_rank import UpdateChatParticipantRank
    from .update_managed_bot import UpdateManagedBot
    from .update_bot_guest_chat_query import UpdateBotGuestChatQuery
    from .update_ai_compose_tones import UpdateAiComposeTones
    from .updates_too_long import UpdatesTooLong
    from .update_short_message import UpdateShortMessage
    from .update_short_chat_message import UpdateShortChatMessage
    from .update_short import UpdateShort
    from .updates_combined import UpdatesCombined
    from .updates_t import Updates
    from .update_short_sent_message import UpdateShortSentMessage
    from .dc_option import DcOption
    from .config import Config
    from .nearest_dc import NearestDc
    from .encrypted_chat_empty import EncryptedChatEmpty
    from .encrypted_chat_waiting import EncryptedChatWaiting
    from .encrypted_chat_requested import EncryptedChatRequested
    from .encrypted_chat import EncryptedChat
    from .encrypted_chat_discarded import EncryptedChatDiscarded
    from .input_encrypted_chat import InputEncryptedChat
    from .encrypted_file_empty import EncryptedFileEmpty
    from .encrypted_file import EncryptedFile
    from .input_encrypted_file_empty import InputEncryptedFileEmpty
    from .input_encrypted_file_uploaded import InputEncryptedFileUploaded
    from .input_encrypted_file import InputEncryptedFile
    from .input_encrypted_file_big_uploaded import InputEncryptedFileBigUploaded
    from .encrypted_message import EncryptedMessage
    from .encrypted_message_service import EncryptedMessageService
    from .input_document_empty import InputDocumentEmpty
    from .input_document import InputDocument
    from .document_empty import DocumentEmpty
    from .document import Document
    from .notify_peer import NotifyPeer
    from .notify_users import NotifyUsers
    from .notify_chats import NotifyChats
    from .notify_broadcasts import NotifyBroadcasts
    from .notify_forum_topic import NotifyForumTopic
    from .send_message_typing_action import SendMessageTypingAction
    from .send_message_cancel_action import SendMessageCancelAction
    from .send_message_record_video_action import SendMessageRecordVideoAction
    from .send_message_upload_video_action import SendMessageUploadVideoAction
    from .send_message_record_audio_action import SendMessageRecordAudioAction
    from .send_message_upload_audio_action import SendMessageUploadAudioAction
    from .send_message_upload_photo_action import SendMessageUploadPhotoAction
    from .send_message_upload_document_action import SendMessageUploadDocumentAction
    from .send_message_geo_location_action import SendMessageGeoLocationAction
    from .send_message_choose_contact_action import SendMessageChooseContactAction
    from .send_message_game_play_action import SendMessageGamePlayAction
    from .send_message_record_round_action import SendMessageRecordRoundAction
    from .send_message_upload_round_action import SendMessageUploadRoundAction
    from .speaking_in_group_call_action import SpeakingInGroupCallAction
    from .send_message_history_import_action import SendMessageHistoryImportAction
    from .send_message_choose_sticker_action import SendMessageChooseStickerAction
    from .send_message_emoji_interaction import SendMessageEmojiInteraction
    from .send_message_emoji_interaction_seen import SendMessageEmojiInteractionSeen
    from .send_message_text_draft_action import SendMessageTextDraftAction
    from .input_privacy_key_status_timestamp import InputPrivacyKeyStatusTimestamp
    from .input_privacy_key_chat_invite import InputPrivacyKeyChatInvite
    from .input_privacy_key_phone_call import InputPrivacyKeyPhoneCall
    from .input_privacy_key_phone_p2_p import InputPrivacyKeyPhoneP2P
    from .input_privacy_key_forwards import InputPrivacyKeyForwards
    from .input_privacy_key_profile_photo import InputPrivacyKeyProfilePhoto
    from .input_privacy_key_phone_number import InputPrivacyKeyPhoneNumber
    from .input_privacy_key_added_by_phone import InputPrivacyKeyAddedByPhone
    from .input_privacy_key_voice_messages import InputPrivacyKeyVoiceMessages
    from .input_privacy_key_about import InputPrivacyKeyAbout
    from .input_privacy_key_birthday import InputPrivacyKeyBirthday
    from .input_privacy_key_star_gifts_auto_save import InputPrivacyKeyStarGiftsAutoSave
    from .input_privacy_key_no_paid_messages import InputPrivacyKeyNoPaidMessages
    from .input_privacy_key_saved_music import InputPrivacyKeySavedMusic
    from .privacy_key_status_timestamp import PrivacyKeyStatusTimestamp
    from .privacy_key_chat_invite import PrivacyKeyChatInvite
    from .privacy_key_phone_call import PrivacyKeyPhoneCall
    from .privacy_key_phone_p2_p import PrivacyKeyPhoneP2P
    from .privacy_key_forwards import PrivacyKeyForwards
    from .privacy_key_profile_photo import PrivacyKeyProfilePhoto
    from .privacy_key_phone_number import PrivacyKeyPhoneNumber
    from .privacy_key_added_by_phone import PrivacyKeyAddedByPhone
    from .privacy_key_voice_messages import PrivacyKeyVoiceMessages
    from .privacy_key_about import PrivacyKeyAbout
    from .privacy_key_birthday import PrivacyKeyBirthday
    from .privacy_key_star_gifts_auto_save import PrivacyKeyStarGiftsAutoSave
    from .privacy_key_no_paid_messages import PrivacyKeyNoPaidMessages
    from .privacy_key_saved_music import PrivacyKeySavedMusic
    from .input_privacy_value_allow_contacts import InputPrivacyValueAllowContacts
    from .input_privacy_value_allow_all import InputPrivacyValueAllowAll
    from .input_privacy_value_allow_users import InputPrivacyValueAllowUsers
    from .input_privacy_value_disallow_contacts import InputPrivacyValueDisallowContacts
    from .input_privacy_value_disallow_all import InputPrivacyValueDisallowAll
    from .input_privacy_value_disallow_users import InputPrivacyValueDisallowUsers
    from .input_privacy_value_allow_chat_participants import InputPrivacyValueAllowChatParticipants
    from .input_privacy_value_disallow_chat_participants import InputPrivacyValueDisallowChatParticipants
    from .input_privacy_value_allow_close_friends import InputPrivacyValueAllowCloseFriends
    from .input_privacy_value_allow_premium import InputPrivacyValueAllowPremium
    from .input_privacy_value_allow_bots import InputPrivacyValueAllowBots
    from .input_privacy_value_disallow_bots import InputPrivacyValueDisallowBots
    from .privacy_value_allow_contacts import PrivacyValueAllowContacts
    from .privacy_value_allow_all import PrivacyValueAllowAll
    from .privacy_value_allow_users import PrivacyValueAllowUsers
    from .privacy_value_disallow_contacts import PrivacyValueDisallowContacts
    from .privacy_value_disallow_all import PrivacyValueDisallowAll
    from .privacy_value_disallow_users import PrivacyValueDisallowUsers
    from .privacy_value_allow_chat_participants import PrivacyValueAllowChatParticipants
    from .privacy_value_disallow_chat_participants import PrivacyValueDisallowChatParticipants
    from .privacy_value_allow_close_friends import PrivacyValueAllowCloseFriends
    from .privacy_value_allow_premium import PrivacyValueAllowPremium
    from .privacy_value_allow_bots import PrivacyValueAllowBots
    from .privacy_value_disallow_bots import PrivacyValueDisallowBots
    from .account_days_ttl import AccountDaysTTL
    from .document_attribute_image_size import DocumentAttributeImageSize
    from .document_attribute_animated import DocumentAttributeAnimated
    from .document_attribute_sticker import DocumentAttributeSticker
    from .document_attribute_video import DocumentAttributeVideo
    from .document_attribute_audio import DocumentAttributeAudio
    from .document_attribute_filename import DocumentAttributeFilename
    from .document_attribute_has_stickers import DocumentAttributeHasStickers
    from .document_attribute_custom_emoji import DocumentAttributeCustomEmoji
    from .sticker_pack import StickerPack
    from .web_page_empty import WebPageEmpty
    from .web_page_pending import WebPagePending
    from .web_page import WebPage
    from .web_page_not_modified import WebPageNotModified
    from .authorization import Authorization
    from .received_notify_message import ReceivedNotifyMessage
    from .chat_invite_exported import ChatInviteExported
    from .chat_invite_public_join_requests import ChatInvitePublicJoinRequests
    from .chat_invite_already import ChatInviteAlready
    from .chat_invite import ChatInvite
    from .chat_invite_peek import ChatInvitePeek
    from .input_sticker_set_empty import InputStickerSetEmpty
    from .input_sticker_set_id import InputStickerSetID
    from .input_sticker_set_short_name import InputStickerSetShortName
    from .input_sticker_set_animated_emoji import InputStickerSetAnimatedEmoji
    from .input_sticker_set_dice import InputStickerSetDice
    from .input_sticker_set_animated_emoji_animations import InputStickerSetAnimatedEmojiAnimations
    from .input_sticker_set_premium_gifts import InputStickerSetPremiumGifts
    from .input_sticker_set_emoji_generic_animations import InputStickerSetEmojiGenericAnimations
    from .input_sticker_set_emoji_default_statuses import InputStickerSetEmojiDefaultStatuses
    from .input_sticker_set_emoji_default_topic_icons import InputStickerSetEmojiDefaultTopicIcons
    from .input_sticker_set_emoji_channel_default_statuses import InputStickerSetEmojiChannelDefaultStatuses
    from .input_sticker_set_ton_gifts import InputStickerSetTonGifts
    from .sticker_set import StickerSet
    from .bot_command import BotCommand
    from .bot_info import BotInfo
    from .keyboard_button import KeyboardButton
    from .keyboard_button_url import KeyboardButtonUrl
    from .keyboard_button_callback import KeyboardButtonCallback
    from .keyboard_button_request_phone import KeyboardButtonRequestPhone
    from .keyboard_button_request_geo_location import KeyboardButtonRequestGeoLocation
    from .keyboard_button_switch_inline import KeyboardButtonSwitchInline
    from .keyboard_button_game import KeyboardButtonGame
    from .keyboard_button_buy import KeyboardButtonBuy
    from .keyboard_button_url_auth import KeyboardButtonUrlAuth
    from .input_keyboard_button_url_auth import InputKeyboardButtonUrlAuth
    from .keyboard_button_request_poll import KeyboardButtonRequestPoll
    from .input_keyboard_button_user_profile import InputKeyboardButtonUserProfile
    from .keyboard_button_user_profile import KeyboardButtonUserProfile
    from .keyboard_button_web_view import KeyboardButtonWebView
    from .keyboard_button_simple_web_view import KeyboardButtonSimpleWebView
    from .keyboard_button_request_peer import KeyboardButtonRequestPeer
    from .input_keyboard_button_request_peer import InputKeyboardButtonRequestPeer
    from .keyboard_button_copy import KeyboardButtonCopy
    from .keyboard_button_row import KeyboardButtonRow
    from .reply_keyboard_hide import ReplyKeyboardHide
    from .reply_keyboard_force_reply import ReplyKeyboardForceReply
    from .reply_keyboard_markup import ReplyKeyboardMarkup
    from .reply_inline_markup import ReplyInlineMarkup
    from .message_entity_unknown import MessageEntityUnknown
    from .message_entity_mention import MessageEntityMention
    from .message_entity_hashtag import MessageEntityHashtag
    from .message_entity_bot_command import MessageEntityBotCommand
    from .message_entity_url import MessageEntityUrl
    from .message_entity_email import MessageEntityEmail
    from .message_entity_bold import MessageEntityBold
    from .message_entity_italic import MessageEntityItalic
    from .message_entity_code import MessageEntityCode
    from .message_entity_pre import MessageEntityPre
    from .message_entity_text_url import MessageEntityTextUrl
    from .message_entity_mention_name import MessageEntityMentionName
    from .input_message_entity_mention_name import InputMessageEntityMentionName
    from .message_entity_phone import MessageEntityPhone
    from .message_entity_cashtag import MessageEntityCashtag
    from .message_entity_underline import MessageEntityUnderline
    from .message_entity_strike import MessageEntityStrike
    from .message_entity_bank_card import MessageEntityBankCard
    from .message_entity_spoiler import MessageEntitySpoiler
    from .message_entity_custom_emoji import MessageEntityCustomEmoji
    from .message_entity_blockquote import MessageEntityBlockquote
    from .message_entity_formatted_date import MessageEntityFormattedDate
    from .message_entity_diff_insert import MessageEntityDiffInsert
    from .message_entity_diff_replace import MessageEntityDiffReplace
    from .message_entity_diff_delete import MessageEntityDiffDelete
    from .input_channel_empty import InputChannelEmpty
    from .input_channel import InputChannel
    from .input_channel_from_message import InputChannelFromMessage
    from .message_range import MessageRange
    from .channel_messages_filter_empty import ChannelMessagesFilterEmpty
    from .channel_messages_filter import ChannelMessagesFilter
    from .channel_participant import ChannelParticipant
    from .channel_participant_self import ChannelParticipantSelf
    from .channel_participant_creator import ChannelParticipantCreator
    from .channel_participant_admin import ChannelParticipantAdmin
    from .channel_participant_banned import ChannelParticipantBanned
    from .channel_participant_left import ChannelParticipantLeft
    from .channel_participants_recent import ChannelParticipantsRecent
    from .channel_participants_admins import ChannelParticipantsAdmins
    from .channel_participants_kicked import ChannelParticipantsKicked
    from .channel_participants_bots import ChannelParticipantsBots
    from .channel_participants_banned import ChannelParticipantsBanned
    from .channel_participants_search import ChannelParticipantsSearch
    from .channel_participants_contacts import ChannelParticipantsContacts
    from .channel_participants_mentions import ChannelParticipantsMentions
    from .input_bot_inline_message_media_auto import InputBotInlineMessageMediaAuto
    from .input_bot_inline_message_text import InputBotInlineMessageText
    from .input_bot_inline_message_media_geo import InputBotInlineMessageMediaGeo
    from .input_bot_inline_message_media_venue import InputBotInlineMessageMediaVenue
    from .input_bot_inline_message_media_contact import InputBotInlineMessageMediaContact
    from .input_bot_inline_message_game import InputBotInlineMessageGame
    from .input_bot_inline_message_media_invoice import InputBotInlineMessageMediaInvoice
    from .input_bot_inline_message_media_web_page import InputBotInlineMessageMediaWebPage
    from .input_bot_inline_result import InputBotInlineResult
    from .input_bot_inline_result_photo import InputBotInlineResultPhoto
    from .input_bot_inline_result_document import InputBotInlineResultDocument
    from .input_bot_inline_result_game import InputBotInlineResultGame
    from .bot_inline_message_media_auto import BotInlineMessageMediaAuto
    from .bot_inline_message_text import BotInlineMessageText
    from .bot_inline_message_media_geo import BotInlineMessageMediaGeo
    from .bot_inline_message_media_venue import BotInlineMessageMediaVenue
    from .bot_inline_message_media_contact import BotInlineMessageMediaContact
    from .bot_inline_message_media_invoice import BotInlineMessageMediaInvoice
    from .bot_inline_message_media_web_page import BotInlineMessageMediaWebPage
    from .bot_inline_result import BotInlineResult
    from .bot_inline_media_result import BotInlineMediaResult
    from .exported_message_link import ExportedMessageLink
    from .message_fwd_header import MessageFwdHeader
    from .input_bot_inline_message_id import InputBotInlineMessageID
    from .input_bot_inline_message_id64 import InputBotInlineMessageID64
    from .inline_bot_switch_pm import InlineBotSwitchPM
    from .top_peer import TopPeer
    from .top_peer_category_bots_pm import TopPeerCategoryBotsPM
    from .top_peer_category_bots_inline import TopPeerCategoryBotsInline
    from .top_peer_category_correspondents import TopPeerCategoryCorrespondents
    from .top_peer_category_groups import TopPeerCategoryGroups
    from .top_peer_category_channels import TopPeerCategoryChannels
    from .top_peer_category_phone_calls import TopPeerCategoryPhoneCalls
    from .top_peer_category_forward_users import TopPeerCategoryForwardUsers
    from .top_peer_category_forward_chats import TopPeerCategoryForwardChats
    from .top_peer_category_bots_app import TopPeerCategoryBotsApp
    from .top_peer_category_bots_guest_chat import TopPeerCategoryBotsGuestChat
    from .top_peer_category_peers import TopPeerCategoryPeers
    from .draft_message_empty import DraftMessageEmpty
    from .draft_message import DraftMessage
    from .sticker_set_covered import StickerSetCovered
    from .sticker_set_multi_covered import StickerSetMultiCovered
    from .sticker_set_full_covered import StickerSetFullCovered
    from .sticker_set_no_covered import StickerSetNoCovered
    from .mask_coords import MaskCoords
    from .input_stickered_media_photo import InputStickeredMediaPhoto
    from .input_stickered_media_document import InputStickeredMediaDocument
    from .game import Game
    from .input_game_id import InputGameID
    from .input_game_short_name import InputGameShortName
    from .high_score import HighScore
    from .text_empty import TextEmpty
    from .text_plain import TextPlain
    from .text_bold import TextBold
    from .text_italic import TextItalic
    from .text_underline import TextUnderline
    from .text_strike import TextStrike
    from .text_fixed import TextFixed
    from .text_url import TextUrl
    from .text_email import TextEmail
    from .text_concat import TextConcat
    from .text_subscript import TextSubscript
    from .text_superscript import TextSuperscript
    from .text_marked import TextMarked
    from .text_phone import TextPhone
    from .text_image import TextImage
    from .text_anchor import TextAnchor
    from .page_block_unsupported import PageBlockUnsupported
    from .page_block_title import PageBlockTitle
    from .page_block_subtitle import PageBlockSubtitle
    from .page_block_author_date import PageBlockAuthorDate
    from .page_block_header import PageBlockHeader
    from .page_block_subheader import PageBlockSubheader
    from .page_block_paragraph import PageBlockParagraph
    from .page_block_preformatted import PageBlockPreformatted
    from .page_block_footer import PageBlockFooter
    from .page_block_divider import PageBlockDivider
    from .page_block_anchor import PageBlockAnchor
    from .page_block_list import PageBlockList
    from .page_block_blockquote import PageBlockBlockquote
    from .page_block_pullquote import PageBlockPullquote
    from .page_block_photo import PageBlockPhoto
    from .page_block_video import PageBlockVideo
    from .page_block_cover import PageBlockCover
    from .page_block_embed import PageBlockEmbed
    from .page_block_embed_post import PageBlockEmbedPost
    from .page_block_collage import PageBlockCollage
    from .page_block_slideshow import PageBlockSlideshow
    from .page_block_channel import PageBlockChannel
    from .page_block_audio import PageBlockAudio
    from .page_block_kicker import PageBlockKicker
    from .page_block_table import PageBlockTable
    from .page_block_ordered_list import PageBlockOrderedList
    from .page_block_details import PageBlockDetails
    from .page_block_related_articles import PageBlockRelatedArticles
    from .page_block_map import PageBlockMap
    from .phone_call_discard_reason_missed import PhoneCallDiscardReasonMissed
    from .phone_call_discard_reason_disconnect import PhoneCallDiscardReasonDisconnect
    from .phone_call_discard_reason_hangup import PhoneCallDiscardReasonHangup
    from .phone_call_discard_reason_busy import PhoneCallDiscardReasonBusy
    from .phone_call_discard_reason_migrate_conference_call import PhoneCallDiscardReasonMigrateConferenceCall
    from .data_json import DataJSON
    from .labeled_price import LabeledPrice
    from .invoice import Invoice
    from .payment_charge import PaymentCharge
    from .post_address import PostAddress
    from .payment_requested_info import PaymentRequestedInfo
    from .payment_saved_credentials_card import PaymentSavedCredentialsCard
    from .web_document import WebDocument
    from .web_document_no_proxy import WebDocumentNoProxy
    from .input_web_document import InputWebDocument
    from .input_web_file_location import InputWebFileLocation
    from .input_web_file_geo_point_location import InputWebFileGeoPointLocation
    from .input_web_file_audio_album_thumb_location import InputWebFileAudioAlbumThumbLocation
    from .input_payment_credentials_saved import InputPaymentCredentialsSaved
    from .input_payment_credentials import InputPaymentCredentials
    from .input_payment_credentials_apple_pay import InputPaymentCredentialsApplePay
    from .input_payment_credentials_google_pay import InputPaymentCredentialsGooglePay
    from .shipping_option import ShippingOption
    from .input_sticker_set_item import InputStickerSetItem
    from .input_phone_call import InputPhoneCall
    from .phone_call_empty import PhoneCallEmpty
    from .phone_call_waiting import PhoneCallWaiting
    from .phone_call_requested import PhoneCallRequested
    from .phone_call_accepted import PhoneCallAccepted
    from .phone_call import PhoneCall
    from .phone_call_discarded import PhoneCallDiscarded
    from .phone_connection import PhoneConnection
    from .phone_connection_webrtc import PhoneConnectionWebrtc
    from .phone_call_protocol import PhoneCallProtocol
    from .cdn_public_key import CdnPublicKey
    from .cdn_config import CdnConfig
    from .lang_pack_string import LangPackString
    from .lang_pack_string_pluralized import LangPackStringPluralized
    from .lang_pack_string_deleted import LangPackStringDeleted
    from .lang_pack_difference import LangPackDifference
    from .lang_pack_language import LangPackLanguage
    from .channel_admin_log_event_action_change_title import ChannelAdminLogEventActionChangeTitle
    from .channel_admin_log_event_action_change_about import ChannelAdminLogEventActionChangeAbout
    from .channel_admin_log_event_action_change_username import ChannelAdminLogEventActionChangeUsername
    from .channel_admin_log_event_action_change_photo import ChannelAdminLogEventActionChangePhoto
    from .channel_admin_log_event_action_toggle_invites import ChannelAdminLogEventActionToggleInvites
    from .channel_admin_log_event_action_toggle_signatures import ChannelAdminLogEventActionToggleSignatures
    from .channel_admin_log_event_action_update_pinned import ChannelAdminLogEventActionUpdatePinned
    from .channel_admin_log_event_action_edit_message import ChannelAdminLogEventActionEditMessage
    from .channel_admin_log_event_action_delete_message import ChannelAdminLogEventActionDeleteMessage
    from .channel_admin_log_event_action_participant_join import ChannelAdminLogEventActionParticipantJoin
    from .channel_admin_log_event_action_participant_leave import ChannelAdminLogEventActionParticipantLeave
    from .channel_admin_log_event_action_participant_invite import ChannelAdminLogEventActionParticipantInvite
    from .channel_admin_log_event_action_participant_toggle_ban import ChannelAdminLogEventActionParticipantToggleBan
    from .channel_admin_log_event_action_participant_toggle_admin import ChannelAdminLogEventActionParticipantToggleAdmin
    from .channel_admin_log_event_action_change_sticker_set import ChannelAdminLogEventActionChangeStickerSet
    from .channel_admin_log_event_action_toggle_pre_history_hidden import ChannelAdminLogEventActionTogglePreHistoryHidden
    from .channel_admin_log_event_action_default_banned_rights import ChannelAdminLogEventActionDefaultBannedRights
    from .channel_admin_log_event_action_stop_poll import ChannelAdminLogEventActionStopPoll
    from .channel_admin_log_event_action_change_linked_chat import ChannelAdminLogEventActionChangeLinkedChat
    from .channel_admin_log_event_action_change_location import ChannelAdminLogEventActionChangeLocation
    from .channel_admin_log_event_action_toggle_slow_mode import ChannelAdminLogEventActionToggleSlowMode
    from .channel_admin_log_event_action_start_group_call import ChannelAdminLogEventActionStartGroupCall
    from .channel_admin_log_event_action_discard_group_call import ChannelAdminLogEventActionDiscardGroupCall
    from .channel_admin_log_event_action_participant_mute import ChannelAdminLogEventActionParticipantMute
    from .channel_admin_log_event_action_participant_unmute import ChannelAdminLogEventActionParticipantUnmute
    from .channel_admin_log_event_action_toggle_group_call_setting import ChannelAdminLogEventActionToggleGroupCallSetting
    from .channel_admin_log_event_action_participant_join_by_invite import ChannelAdminLogEventActionParticipantJoinByInvite
    from .channel_admin_log_event_action_exported_invite_delete import ChannelAdminLogEventActionExportedInviteDelete
    from .channel_admin_log_event_action_exported_invite_revoke import ChannelAdminLogEventActionExportedInviteRevoke
    from .channel_admin_log_event_action_exported_invite_edit import ChannelAdminLogEventActionExportedInviteEdit
    from .channel_admin_log_event_action_participant_volume import ChannelAdminLogEventActionParticipantVolume
    from .channel_admin_log_event_action_change_history_ttl import ChannelAdminLogEventActionChangeHistoryTTL
    from .channel_admin_log_event_action_participant_join_by_request import ChannelAdminLogEventActionParticipantJoinByRequest
    from .channel_admin_log_event_action_toggle_no_forwards import ChannelAdminLogEventActionToggleNoForwards
    from .channel_admin_log_event_action_send_message import ChannelAdminLogEventActionSendMessage
    from .channel_admin_log_event_action_change_available_reactions import ChannelAdminLogEventActionChangeAvailableReactions
    from .channel_admin_log_event_action_change_usernames import ChannelAdminLogEventActionChangeUsernames
    from .channel_admin_log_event_action_toggle_forum import ChannelAdminLogEventActionToggleForum
    from .channel_admin_log_event_action_create_topic import ChannelAdminLogEventActionCreateTopic
    from .channel_admin_log_event_action_edit_topic import ChannelAdminLogEventActionEditTopic
    from .channel_admin_log_event_action_delete_topic import ChannelAdminLogEventActionDeleteTopic
    from .channel_admin_log_event_action_pin_topic import ChannelAdminLogEventActionPinTopic
    from .channel_admin_log_event_action_toggle_anti_spam import ChannelAdminLogEventActionToggleAntiSpam
    from .channel_admin_log_event_action_change_peer_color import ChannelAdminLogEventActionChangePeerColor
    from .channel_admin_log_event_action_change_profile_peer_color import ChannelAdminLogEventActionChangeProfilePeerColor
    from .channel_admin_log_event_action_change_wallpaper import ChannelAdminLogEventActionChangeWallpaper
    from .channel_admin_log_event_action_change_emoji_status import ChannelAdminLogEventActionChangeEmojiStatus
    from .channel_admin_log_event_action_change_emoji_sticker_set import ChannelAdminLogEventActionChangeEmojiStickerSet
    from .channel_admin_log_event_action_toggle_signature_profiles import ChannelAdminLogEventActionToggleSignatureProfiles
    from .channel_admin_log_event_action_participant_sub_extend import ChannelAdminLogEventActionParticipantSubExtend
    from .channel_admin_log_event_action_toggle_autotranslation import ChannelAdminLogEventActionToggleAutotranslation
    from .channel_admin_log_event_action_participant_edit_rank import ChannelAdminLogEventActionParticipantEditRank
    from .channel_admin_log_event import ChannelAdminLogEvent
    from .channel_admin_log_events_filter import ChannelAdminLogEventsFilter
    from .popular_contact import PopularContact
    from .recent_me_url_unknown import RecentMeUrlUnknown
    from .recent_me_url_user import RecentMeUrlUser
    from .recent_me_url_chat import RecentMeUrlChat
    from .recent_me_url_chat_invite import RecentMeUrlChatInvite
    from .recent_me_url_sticker_set import RecentMeUrlStickerSet
    from .input_single_media import InputSingleMedia
    from .web_authorization import WebAuthorization
    from .input_message_id import InputMessageID
    from .input_message_reply_to import InputMessageReplyTo
    from .input_message_pinned import InputMessagePinned
    from .input_message_callback_query import InputMessageCallbackQuery
    from .input_dialog_peer import InputDialogPeer
    from .input_dialog_peer_folder import InputDialogPeerFolder
    from .dialog_peer import DialogPeer
    from .dialog_peer_folder import DialogPeerFolder
    from .file_hash import FileHash
    from .input_client_proxy import InputClientProxy
    from .input_secure_file_uploaded import InputSecureFileUploaded
    from .input_secure_file import InputSecureFile
    from .secure_file_empty import SecureFileEmpty
    from .secure_file import SecureFile
    from .secure_data import SecureData
    from .secure_plain_phone import SecurePlainPhone
    from .secure_plain_email import SecurePlainEmail
    from .secure_value_type_personal_details import SecureValueTypePersonalDetails
    from .secure_value_type_passport import SecureValueTypePassport
    from .secure_value_type_driver_license import SecureValueTypeDriverLicense
    from .secure_value_type_identity_card import SecureValueTypeIdentityCard
    from .secure_value_type_internal_passport import SecureValueTypeInternalPassport
    from .secure_value_type_address import SecureValueTypeAddress
    from .secure_value_type_utility_bill import SecureValueTypeUtilityBill
    from .secure_value_type_bank_statement import SecureValueTypeBankStatement
    from .secure_value_type_rental_agreement import SecureValueTypeRentalAgreement
    from .secure_value_type_passport_registration import SecureValueTypePassportRegistration
    from .secure_value_type_temporary_registration import SecureValueTypeTemporaryRegistration
    from .secure_value_type_phone import SecureValueTypePhone
    from .secure_value_type_email import SecureValueTypeEmail
    from .secure_value import SecureValue
    from .input_secure_value import InputSecureValue
    from .secure_value_hash import SecureValueHash
    from .secure_value_error_data import SecureValueErrorData
    from .secure_value_error_front_side import SecureValueErrorFrontSide
    from .secure_value_error_reverse_side import SecureValueErrorReverseSide
    from .secure_value_error_selfie import SecureValueErrorSelfie
    from .secure_value_error_file import SecureValueErrorFile
    from .secure_value_error_files import SecureValueErrorFiles
    from .secure_value_error import SecureValueError
    from .secure_value_error_translation_file import SecureValueErrorTranslationFile
    from .secure_value_error_translation_files import SecureValueErrorTranslationFiles
    from .secure_credentials_encrypted import SecureCredentialsEncrypted
    from .saved_phone_contact import SavedPhoneContact
    from .password_kdf_algo_unknown import PasswordKdfAlgoUnknown
    from .password_kdf_algo_sha256_sha256_pbkdf2_hmacsha512iter100000_sha256_mod_pow import PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow
    from .secure_password_kdf_algo_unknown import SecurePasswordKdfAlgoUnknown
    from .secure_password_kdf_algo_pbkdf2_hmacsha512iter100000 import SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000
    from .secure_password_kdf_algo_sha512 import SecurePasswordKdfAlgoSHA512
    from .secure_secret_settings import SecureSecretSettings
    from .input_check_password_empty import InputCheckPasswordEmpty
    from .input_check_password_srp import InputCheckPasswordSRP
    from .secure_required_type import SecureRequiredType
    from .secure_required_type_one_of import SecureRequiredTypeOneOf
    from .input_app_event import InputAppEvent
    from .json_object_value import JsonObjectValue
    from .json_null import JsonNull
    from .json_bool import JsonBool
    from .json_number import JsonNumber
    from .json_string import JsonString
    from .json_array import JsonArray
    from .json_object import JsonObject
    from .page_table_cell import PageTableCell
    from .page_table_row import PageTableRow
    from .page_caption import PageCaption
    from .page_list_item_text import PageListItemText
    from .page_list_item_blocks import PageListItemBlocks
    from .page_list_ordered_item_text import PageListOrderedItemText
    from .page_list_ordered_item_blocks import PageListOrderedItemBlocks
    from .page_related_article import PageRelatedArticle
    from .page import Page
    from .poll_answer import PollAnswer
    from .input_poll_answer import InputPollAnswer
    from .poll import Poll
    from .poll_answer_voters import PollAnswerVoters
    from .poll_results import PollResults
    from .chat_onlines import ChatOnlines
    from .stats_url import StatsURL
    from .chat_admin_rights import ChatAdminRights
    from .chat_banned_rights import ChatBannedRights
    from .input_wall_paper import InputWallPaper
    from .input_wall_paper_slug import InputWallPaperSlug
    from .input_wall_paper_no_file import InputWallPaperNoFile
    from .code_settings import CodeSettings
    from .wall_paper_settings import WallPaperSettings
    from .auto_download_settings import AutoDownloadSettings
    from .emoji_keyword import EmojiKeyword
    from .emoji_keyword_deleted import EmojiKeywordDeleted
    from .emoji_keywords_difference import EmojiKeywordsDifference
    from .emoji_url import EmojiURL
    from .emoji_language import EmojiLanguage
    from .folder import Folder
    from .input_folder_peer import InputFolderPeer
    from .folder_peer import FolderPeer
    from .url_auth_result_request import UrlAuthResultRequest
    from .url_auth_result_accepted import UrlAuthResultAccepted
    from .url_auth_result_default import UrlAuthResultDefault
    from .channel_location_empty import ChannelLocationEmpty
    from .channel_location import ChannelLocation
    from .peer_located import PeerLocated
    from .peer_self_located import PeerSelfLocated
    from .restriction_reason import RestrictionReason
    from .input_theme import InputTheme
    from .input_theme_slug import InputThemeSlug
    from .theme import Theme
    from .base_theme_classic import BaseThemeClassic
    from .base_theme_day import BaseThemeDay
    from .base_theme_night import BaseThemeNight
    from .base_theme_tinted import BaseThemeTinted
    from .base_theme_arctic import BaseThemeArctic
    from .input_theme_settings import InputThemeSettings
    from .theme_settings import ThemeSettings
    from .web_page_attribute_theme import WebPageAttributeTheme
    from .web_page_attribute_story import WebPageAttributeStory
    from .web_page_attribute_sticker_set import WebPageAttributeStickerSet
    from .web_page_attribute_unique_star_gift import WebPageAttributeUniqueStarGift
    from .web_page_attribute_star_gift_collection import WebPageAttributeStarGiftCollection
    from .web_page_attribute_star_gift_auction import WebPageAttributeStarGiftAuction
    from .web_page_attribute_ai_compose_tone import WebPageAttributeAiComposeTone
    from .bank_card_open_url import BankCardOpenUrl
    from .dialog_filter import DialogFilter
    from .dialog_filter_default import DialogFilterDefault
    from .dialog_filter_chatlist import DialogFilterChatlist
    from .dialog_filter_suggested import DialogFilterSuggested
    from .stats_date_range_days import StatsDateRangeDays
    from .stats_abs_value_and_prev import StatsAbsValueAndPrev
    from .stats_percent_value import StatsPercentValue
    from .stats_graph_async import StatsGraphAsync
    from .stats_graph_error import StatsGraphError
    from .stats_graph import StatsGraph
    from .video_size import VideoSize
    from .video_size_emoji_markup import VideoSizeEmojiMarkup
    from .video_size_sticker_markup import VideoSizeStickerMarkup
    from .stats_group_top_poster import StatsGroupTopPoster
    from .stats_group_top_admin import StatsGroupTopAdmin
    from .stats_group_top_inviter import StatsGroupTopInviter
    from .global_privacy_settings import GlobalPrivacySettings
    from .message_views import MessageViews
    from .message_reply_header import MessageReplyHeader
    from .message_reply_story_header import MessageReplyStoryHeader
    from .message_replies import MessageReplies
    from .peer_blocked import PeerBlocked
    from .group_call_discarded import GroupCallDiscarded
    from .group_call import GroupCall
    from .input_group_call import InputGroupCall
    from .input_group_call_slug import InputGroupCallSlug
    from .input_group_call_invite_message import InputGroupCallInviteMessage
    from .group_call_participant import GroupCallParticipant
    from .inline_query_peer_type_same_bot_pm import InlineQueryPeerTypeSameBotPM
    from .inline_query_peer_type_pm import InlineQueryPeerTypePM
    from .inline_query_peer_type_chat import InlineQueryPeerTypeChat
    from .inline_query_peer_type_megagroup import InlineQueryPeerTypeMegagroup
    from .inline_query_peer_type_broadcast import InlineQueryPeerTypeBroadcast
    from .inline_query_peer_type_bot_pm import InlineQueryPeerTypeBotPM
    from .chat_invite_importer import ChatInviteImporter
    from .chat_admin_with_invites import ChatAdminWithInvites
    from .group_call_participant_video_source_group import GroupCallParticipantVideoSourceGroup
    from .group_call_participant_video import GroupCallParticipantVideo
    from .bot_command_scope_default import BotCommandScopeDefault
    from .bot_command_scope_users import BotCommandScopeUsers
    from .bot_command_scope_chats import BotCommandScopeChats
    from .bot_command_scope_chat_admins import BotCommandScopeChatAdmins
    from .bot_command_scope_peer import BotCommandScopePeer
    from .bot_command_scope_peer_admins import BotCommandScopePeerAdmins
    from .bot_command_scope_peer_user import BotCommandScopePeerUser
    from .chat_theme import ChatTheme
    from .chat_theme_unique_gift import ChatThemeUniqueGift
    from .sponsored_message import SponsoredMessage
    from .search_results_calendar_period import SearchResultsCalendarPeriod
    from .search_result_position import SearchResultPosition
    from .reaction_count import ReactionCount
    from .message_reactions import MessageReactions
    from .available_reaction import AvailableReaction
    from .message_peer_reaction import MessagePeerReaction
    from .group_call_stream_channel import GroupCallStreamChannel
    from .attach_menu_bot_icon_color import AttachMenuBotIconColor
    from .attach_menu_bot_icon import AttachMenuBotIcon
    from .attach_menu_bot import AttachMenuBot
    from .attach_menu_bots_not_modified import AttachMenuBotsNotModified
    from .attach_menu_bots import AttachMenuBots
    from .attach_menu_bots_bot import AttachMenuBotsBot
    from .web_view_result_url import WebViewResultUrl
    from .web_view_message_sent import WebViewMessageSent
    from .bot_menu_button_default import BotMenuButtonDefault
    from .bot_menu_button_commands import BotMenuButtonCommands
    from .bot_menu_button import BotMenuButton
    from .notification_sound_default import NotificationSoundDefault
    from .notification_sound_none import NotificationSoundNone
    from .notification_sound_local import NotificationSoundLocal
    from .notification_sound_ringtone import NotificationSoundRingtone
    from .attach_menu_peer_type_same_bot_pm import AttachMenuPeerTypeSameBotPM
    from .attach_menu_peer_type_bot_pm import AttachMenuPeerTypeBotPM
    from .attach_menu_peer_type_pm import AttachMenuPeerTypePM
    from .attach_menu_peer_type_chat import AttachMenuPeerTypeChat
    from .attach_menu_peer_type_broadcast import AttachMenuPeerTypeBroadcast
    from .input_invoice_message import InputInvoiceMessage
    from .input_invoice_slug import InputInvoiceSlug
    from .input_invoice_premium_gift_code import InputInvoicePremiumGiftCode
    from .input_invoice_stars import InputInvoiceStars
    from .input_invoice_chat_invite_subscription import InputInvoiceChatInviteSubscription
    from .input_invoice_star_gift import InputInvoiceStarGift
    from .input_invoice_star_gift_upgrade import InputInvoiceStarGiftUpgrade
    from .input_invoice_star_gift_transfer import InputInvoiceStarGiftTransfer
    from .input_invoice_premium_gift_stars import InputInvoicePremiumGiftStars
    from .input_invoice_business_bot_transfer_stars import InputInvoiceBusinessBotTransferStars
    from .input_invoice_star_gift_resale import InputInvoiceStarGiftResale
    from .input_invoice_star_gift_prepaid_upgrade import InputInvoiceStarGiftPrepaidUpgrade
    from .input_invoice_premium_auth_code import InputInvoicePremiumAuthCode
    from .input_invoice_star_gift_drop_original_details import InputInvoiceStarGiftDropOriginalDetails
    from .input_invoice_star_gift_auction_bid import InputInvoiceStarGiftAuctionBid
    from .input_store_payment_premium_subscription import InputStorePaymentPremiumSubscription
    from .input_store_payment_gift_premium import InputStorePaymentGiftPremium
    from .input_store_payment_premium_gift_code import InputStorePaymentPremiumGiftCode
    from .input_store_payment_premium_giveaway import InputStorePaymentPremiumGiveaway
    from .input_store_payment_stars_topup import InputStorePaymentStarsTopup
    from .input_store_payment_stars_gift import InputStorePaymentStarsGift
    from .input_store_payment_stars_giveaway import InputStorePaymentStarsGiveaway
    from .input_store_payment_auth_code import InputStorePaymentAuthCode
    from .payment_form_method import PaymentFormMethod
    from .emoji_status_empty import EmojiStatusEmpty
    from .emoji_status import EmojiStatus
    from .emoji_status_collectible import EmojiStatusCollectible
    from .input_emoji_status_collectible import InputEmojiStatusCollectible
    from .reaction_empty import ReactionEmpty
    from .reaction_emoji import ReactionEmoji
    from .reaction_custom_emoji import ReactionCustomEmoji
    from .reaction_paid import ReactionPaid
    from .chat_reactions_none import ChatReactionsNone
    from .chat_reactions_all import ChatReactionsAll
    from .chat_reactions_some import ChatReactionsSome
    from .email_verify_purpose_login_setup import EmailVerifyPurposeLoginSetup
    from .email_verify_purpose_login_change import EmailVerifyPurposeLoginChange
    from .email_verify_purpose_passport import EmailVerifyPurposePassport
    from .email_verification_code import EmailVerificationCode
    from .email_verification_google import EmailVerificationGoogle
    from .email_verification_apple import EmailVerificationApple
    from .premium_subscription_option import PremiumSubscriptionOption
    from .send_as_peer import SendAsPeer
    from .message_extended_media_preview import MessageExtendedMediaPreview
    from .message_extended_media import MessageExtendedMedia
    from .sticker_keyword import StickerKeyword
    from .username import Username
    from .forum_topic_deleted import ForumTopicDeleted
    from .forum_topic import ForumTopic
    from .default_history_ttl import DefaultHistoryTTL
    from .exported_contact_token import ExportedContactToken
    from .request_peer_type_user import RequestPeerTypeUser
    from .request_peer_type_chat import RequestPeerTypeChat
    from .request_peer_type_broadcast import RequestPeerTypeBroadcast
    from .request_peer_type_create_bot import RequestPeerTypeCreateBot
    from .emoji_list_not_modified import EmojiListNotModified
    from .emoji_list import EmojiList
    from .emoji_group import EmojiGroup
    from .emoji_group_greeting import EmojiGroupGreeting
    from .emoji_group_premium import EmojiGroupPremium
    from .text_with_entities import TextWithEntities
    from .auto_save_settings import AutoSaveSettings
    from .auto_save_exception import AutoSaveException
    from .input_bot_app_id import InputBotAppID
    from .input_bot_app_short_name import InputBotAppShortName
    from .bot_app_not_modified import BotAppNotModified
    from .bot_app import BotApp
    from .inline_bot_web_view import InlineBotWebView
    from .read_participant_date import ReadParticipantDate
    from .input_chatlist_dialog_filter import InputChatlistDialogFilter
    from .exported_chatlist_invite import ExportedChatlistInvite
    from .message_peer_vote import MessagePeerVote
    from .message_peer_vote_input_option import MessagePeerVoteInputOption
    from .message_peer_vote_multiple import MessagePeerVoteMultiple
    from .story_views import StoryViews
    from .story_item_deleted import StoryItemDeleted
    from .story_item_skipped import StoryItemSkipped
    from .story_item import StoryItem
    from .story_view import StoryView
    from .story_view_public_forward import StoryViewPublicForward
    from .story_view_public_repost import StoryViewPublicRepost
    from .input_reply_to_message import InputReplyToMessage
    from .input_reply_to_story import InputReplyToStory
    from .input_reply_to_mono_forum import InputReplyToMonoForum
    from .exported_story_link import ExportedStoryLink
    from .stories_stealth_mode import StoriesStealthMode
    from .media_area_coordinates import MediaAreaCoordinates
    from .media_area_venue import MediaAreaVenue
    from .input_media_area_venue import InputMediaAreaVenue
    from .media_area_geo_point import MediaAreaGeoPoint
    from .media_area_suggested_reaction import MediaAreaSuggestedReaction
    from .media_area_channel_post import MediaAreaChannelPost
    from .input_media_area_channel_post import InputMediaAreaChannelPost
    from .media_area_url import MediaAreaUrl
    from .media_area_weather import MediaAreaWeather
    from .media_area_star_gift import MediaAreaStarGift
    from .peer_stories import PeerStories
    from .premium_gift_code_option import PremiumGiftCodeOption
    from .prepaid_giveaway import PrepaidGiveaway
    from .prepaid_stars_giveaway import PrepaidStarsGiveaway
    from .boost import Boost
    from .my_boost import MyBoost
    from .story_fwd_header import StoryFwdHeader
    from .post_interaction_counters_message import PostInteractionCountersMessage
    from .post_interaction_counters_story import PostInteractionCountersStory
    from .public_forward_message import PublicForwardMessage
    from .public_forward_story import PublicForwardStory
    from .peer_color import PeerColor
    from .peer_color_collectible import PeerColorCollectible
    from .input_peer_color_collectible import InputPeerColorCollectible
    from .story_reaction import StoryReaction
    from .story_reaction_public_forward import StoryReactionPublicForward
    from .story_reaction_public_repost import StoryReactionPublicRepost
    from .saved_dialog import SavedDialog
    from .mono_forum_dialog import MonoForumDialog
    from .saved_reaction_tag import SavedReactionTag
    from .outbox_read_date import OutboxReadDate
    from .sms_job import SmsJob
    from .business_weekly_open import BusinessWeeklyOpen
    from .business_work_hours import BusinessWorkHours
    from .business_location import BusinessLocation
    from .input_business_recipients import InputBusinessRecipients
    from .business_recipients import BusinessRecipients
    from .business_away_message_schedule_always import BusinessAwayMessageScheduleAlways
    from .business_away_message_schedule_outside_work_hours import BusinessAwayMessageScheduleOutsideWorkHours
    from .business_away_message_schedule_custom import BusinessAwayMessageScheduleCustom
    from .input_business_greeting_message import InputBusinessGreetingMessage
    from .business_greeting_message import BusinessGreetingMessage
    from .input_business_away_message import InputBusinessAwayMessage
    from .business_away_message import BusinessAwayMessage
    from .timezone import Timezone
    from .quick_reply import QuickReply
    from .input_quick_reply_shortcut import InputQuickReplyShortcut
    from .input_quick_reply_shortcut_id import InputQuickReplyShortcutId
    from .connected_bot import ConnectedBot
    from .birthday import Birthday
    from .bot_business_connection import BotBusinessConnection
    from .input_business_intro import InputBusinessIntro
    from .business_intro import BusinessIntro
    from .input_collectible_username import InputCollectibleUsername
    from .input_collectible_phone import InputCollectiblePhone
    from .input_business_bot_recipients import InputBusinessBotRecipients
    from .business_bot_recipients import BusinessBotRecipients
    from .contact_birthday import ContactBirthday
    from .missing_invitee import MissingInvitee
    from .input_business_chat_link import InputBusinessChatLink
    from .business_chat_link import BusinessChatLink
    from .requested_peer_user import RequestedPeerUser
    from .requested_peer_chat import RequestedPeerChat
    from .requested_peer_channel import RequestedPeerChannel
    from .sponsored_message_report_option import SponsoredMessageReportOption
    from .reaction_notifications_from_contacts import ReactionNotificationsFromContacts
    from .reaction_notifications_from_all import ReactionNotificationsFromAll
    from .reactions_notify_settings import ReactionsNotifySettings
    from .available_effect import AvailableEffect
    from .fact_check import FactCheck
    from .stars_transaction_peer_unsupported import StarsTransactionPeerUnsupported
    from .stars_transaction_peer_app_store import StarsTransactionPeerAppStore
    from .stars_transaction_peer_play_market import StarsTransactionPeerPlayMarket
    from .stars_transaction_peer_premium_bot import StarsTransactionPeerPremiumBot
    from .stars_transaction_peer_fragment import StarsTransactionPeerFragment
    from .stars_transaction_peer import StarsTransactionPeer
    from .stars_transaction_peer_ads import StarsTransactionPeerAds
    from .stars_transaction_peer_api import StarsTransactionPeerAPI
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
    from .star_gift_unique import StarGiftUnique
    from .message_report_option import MessageReportOption
    from .report_result_choose_option import ReportResultChooseOption
    from .report_result_add_comment import ReportResultAddComment
    from .report_result_reported import ReportResultReported
    from .bot_app_settings import BotAppSettings
    from .star_ref_program import StarRefProgram
    from .connected_bot_star_ref import ConnectedBotStarRef
    from .stars_amount import StarsAmount
    from .stars_ton_amount import StarsTonAmount
    from .bot_verifier_settings import BotVerifierSettings
    from .bot_verification import BotVerification
    from .star_gift_attribute_model import StarGiftAttributeModel
    from .star_gift_attribute_pattern import StarGiftAttributePattern
    from .star_gift_attribute_backdrop import StarGiftAttributeBackdrop
    from .star_gift_attribute_original_details import StarGiftAttributeOriginalDetails
    from .saved_star_gift import SavedStarGift
    from .input_saved_star_gift_user import InputSavedStarGiftUser
    from .input_saved_star_gift_chat import InputSavedStarGiftChat
    from .input_saved_star_gift_slug import InputSavedStarGiftSlug
    from .paid_reaction_privacy_default import PaidReactionPrivacyDefault
    from .paid_reaction_privacy_anonymous import PaidReactionPrivacyAnonymous
    from .paid_reaction_privacy_peer import PaidReactionPrivacyPeer
    from .requirement_to_contact_empty import RequirementToContactEmpty
    from .requirement_to_contact_premium import RequirementToContactPremium
    from .requirement_to_contact_paid_messages import RequirementToContactPaidMessages
    from .business_bot_rights import BusinessBotRights
    from .disallowed_gifts_settings import DisallowedGiftsSettings
    from .sponsored_peer import SponsoredPeer
    from .star_gift_attribute_id_model import StarGiftAttributeIdModel
    from .star_gift_attribute_id_pattern import StarGiftAttributeIdPattern
    from .star_gift_attribute_id_backdrop import StarGiftAttributeIdBackdrop
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
    from .profile_tab_posts import ProfileTabPosts
    from .profile_tab_gifts import ProfileTabGifts
    from .profile_tab_media import ProfileTabMedia
    from .profile_tab_files import ProfileTabFiles
    from .profile_tab_music import ProfileTabMusic
    from .profile_tab_voice import ProfileTabVoice
    from .profile_tab_links import ProfileTabLinks
    from .profile_tab_gifs import ProfileTabGifs
    from .input_chat_theme_empty import InputChatThemeEmpty
    from .input_chat_theme import InputChatTheme
    from .input_chat_theme_unique_gift import InputChatThemeUniqueGift
    from .star_gift_upgrade_price import StarGiftUpgradePrice
    from .group_call_message import GroupCallMessage
    from .group_call_donor import GroupCallDonor
    from .recent_story import RecentStory
    from .auction_bid_level import AuctionBidLevel
    from .star_gift_auction_state_not_modified import StarGiftAuctionStateNotModified
    from .star_gift_auction_state import StarGiftAuctionState
    from .star_gift_auction_state_finished import StarGiftAuctionStateFinished
    from .star_gift_auction_user_state import StarGiftAuctionUserState
    from .star_gift_auction_acquired_gift import StarGiftAuctionAcquiredGift
    from .star_gift_active_auction_state import StarGiftActiveAuctionState
    from .input_star_gift_auction import InputStarGiftAuction
    from .input_star_gift_auction_slug import InputStarGiftAuctionSlug
    from .passkey import Passkey
    from .input_passkey_response_register import InputPasskeyResponseRegister
    from .input_passkey_response_login import InputPasskeyResponseLogin
    from .input_passkey_credential_public_key import InputPasskeyCredentialPublicKey
    from .input_passkey_credential_firebase_pnv import InputPasskeyCredentialFirebasePNV
    from .star_gift_background import StarGiftBackground
    from .star_gift_auction_round import StarGiftAuctionRound
    from .star_gift_auction_round_extendable import StarGiftAuctionRoundExtendable
    from .star_gift_attribute_rarity import StarGiftAttributeRarity
    from .star_gift_attribute_rarity_uncommon import StarGiftAttributeRarityUncommon
    from .star_gift_attribute_rarity_rare import StarGiftAttributeRarityRare
    from .star_gift_attribute_rarity_epic import StarGiftAttributeRarityEpic
    from .star_gift_attribute_rarity_legendary import StarGiftAttributeRarityLegendary
    from .keyboard_button_style import KeyboardButtonStyle
    from .input_message_read_metric import InputMessageReadMetric
    from .input_ai_compose_tone_default import InputAiComposeToneDefault
    from .input_ai_compose_tone_id import InputAiComposeToneID
    from .input_ai_compose_tone_slug import InputAiComposeToneSlug
    from .ai_compose_tone import AiComposeTone
    from .ai_compose_tone_default import AiComposeToneDefault
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
