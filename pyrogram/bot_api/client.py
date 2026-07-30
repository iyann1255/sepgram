import requests
from typing import Optional, Dict, Any, Union, List


class BotAPIClient:
    def __init__(self, bot_token: str):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"

    def request(self, method: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{method}"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    async def get_me(self) -> Dict[str, Any]:
        return self.request("getMe")

    async def log_out(self) -> bool:
        result = self.request("logOut")
        return result.get("ok", False)

    async def close(self) -> bool:
        result = self.request("close")
        return result.get("ok", False)

    async def get_updates(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[list] = None,
    ) -> list:
        data = {}
        if offset:
            data["offset"] = offset
        if limit:
            data["limit"] = limit
        if timeout:
            data["timeout"] = timeout
        if allowed_updates:
            data["allowed_updates"] = allowed_updates

        result = self.request("getUpdates", data)
        return result.get("result", [])

    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str,
        parse_mode: Optional[str] = None,
        entities: Optional[list] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "text": text}
        if parse_mode:
            data["parse_mode"] = parse_mode
        if entities:
            data["entities"] = entities
        if disable_web_page_preview is not None:
            data["disable_web_page_preview"] = disable_web_page_preview
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendMessage", data)
        return result.get("result", {})

    async def send_photo(
        self,
        chat_id: Union[int, str],
        photo: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "photo": photo}
        if caption:
            data["caption"] = caption
        if parse_mode:
            data["parse_mode"] = parse_mode
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendPhoto", data)
        return result.get("result", {})

    async def send_media_group(
        self,
        chat_id: Union[int, str],
        media: List[Dict[str, Any]],
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
    ) -> List[Dict[str, Any]]:
        data = {"chat_id": chat_id, "media": media}
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply

        result = self.request("sendMediaGroup", data)
        return result.get("result", [])

    async def edit_message_live_location(
        self,
        chat_id: Union[int, str],
        message_id: int,
        latitude: float,
        longitude: float,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Union[bool, Dict[str, Any]]:
        data = {
            "chat_id": chat_id,
            "message_id": message_id,
            "latitude": latitude,
            "longitude": longitude,
        }
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("editMessageLiveLocation", data)
        return result.get("result", False)

    async def stop_message_live_location(
        self,
        chat_id: Union[int, str],
        message_id: int,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Union[bool, Dict[str, Any]]:
        data = {"chat_id": chat_id, "message_id": message_id}
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("stopMessageLiveLocation", data)
        return result.get("result", False)

    # ========== Stickers ==========
    async def send_sticker(
        self,
        chat_id: Union[int, str],
        sticker: str,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "sticker": sticker}
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendSticker", data)
        return result.get("result", {})

    async def get_sticker_set(self, name: str) -> Dict[str, Any]:
        data = {"name": name}
        result = self.request("getStickerSet", data)
        return result.get("result", {})

    async def get_custom_emoji_stickers(self, custom_emoji_ids: List[str]) -> List[Dict[str, Any]]:
        data = {"custom_emoji_ids": custom_emoji_ids}
        result = self.request("getCustomEmojiStickers", data)
        return result.get("result", [])

    async def upload_sticker_file(
        self,
        user_id: int,
        png_sticker: str,
    ) -> Dict[str, Any]:
        data = {"user_id": user_id, "png_sticker": png_sticker}
        result = self.request("uploadStickerFile", data)
        return result.get("result", {})

    async def create_new_sticker_set(
        self,
        user_id: int,
        name: str,
        title: str,
        stickers: List[Dict[str, Any]],
        sticker_format: str,
        sticker_type: Optional[str] = None,
        needs_repainting: Optional[bool] = None,
    ) -> bool:
        data = {
            "user_id": user_id,
            "name": name,
            "title": title,
            "stickers": stickers,
            "sticker_format": sticker_format,
        }
        if sticker_type:
            data["sticker_type"] = sticker_type
        if needs_repainting is not None:
            data["needs_repainting"] = needs_repainting

        result = self.request("createNewStickerSet", data)
        return result.get("ok", False)

    async def add_sticker_to_set(
        self,
        user_id: int,
        name: str,
        sticker: Dict[str, Any],
    ) -> bool:
        data = {"user_id": user_id, "name": name, "sticker": sticker}
        result = self.request("addStickerToSet", data)
        return result.get("ok", False)

    async def set_sticker_position_in_set(
        self,
        sticker: str,
        position: int,
    ) -> bool:
        data = {"sticker": sticker, "position": position}
        result = self.request("setStickerPositionInSet", data)
        return result.get("ok", False)

    async def delete_sticker_from_set(self, sticker: str) -> bool:
        data = {"sticker": sticker}
        result = self.request("deleteStickerFromSet", data)
        return result.get("ok", False)

    async def set_sticker_emoji_list(
        self,
        sticker: str,
        emoji_list: List[str],
    ) -> bool:
        data = {"sticker": sticker, "emoji_list": emoji_list}
        result = self.request("setStickerEmojiList", data)
        return result.get("ok", False)

    async def set_sticker_keywords(
        self,
        sticker: str,
        keywords: Optional[List[str]] = None,
    ) -> bool:
        data = {"sticker": sticker}
        if keywords:
            data["keywords"] = keywords

        result = self.request("setStickerKeywords", data)
        return result.get("ok", False)

    async def set_sticker_mask_position(
        self,
        sticker: str,
        mask_position: Optional[Dict[str, Any]] = None,
    ) -> bool:
        data = {"sticker": sticker}
        if mask_position:
            data["mask_position"] = mask_position

        result = self.request("setStickerMaskPosition", data)
        return result.get("ok", False)

    async def set_sticker_set_title(self, name: str, title: str) -> bool:
        data = {"name": name, "title": title}
        result = self.request("setStickerSetTitle", data)
        return result.get("ok", False)

    async def set_sticker_set_thumbnail(
        self,
        name: str,
        user_id: int,
        thumbnail: Optional[str] = None,
    ) -> bool:
        data = {"name": name, "user_id": user_id}
        if thumbnail:
            data["thumbnail"] = thumbnail

        result = self.request("setStickerSetThumbnail", data)
        return result.get("ok", False)

    async def set_custom_emoji_sticker_set_thumbnail(
        self,
        name: str,
        custom_emoji_id: Optional[str] = None,
    ) -> bool:
        data = {"name": name}
        if custom_emoji_id:
            data["custom_emoji_id"] = custom_emoji_id

        result = self.request("setCustomEmojiStickerSetThumbnail", data)
        return result.get("ok", False)

    async def delete_sticker_set(self, name: str) -> bool:
        data = {"name": name}
        result = self.request("deleteStickerSet", data)
        return result.get("ok", False)

    async def send_chat_action(
        self,
        chat_id: Union[int, str],
        action: str,
    ) -> bool:
        data = {"chat_id": chat_id, "action": action}
        result = self.request("sendChatAction", data)
        return result.get("ok", False)

    async def get_chat(
        self,
        chat_id: Union[int, str],
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id}
        result = self.request("getChat", data)
        return result.get("result", {})

    async def send_venue(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {
            "chat_id": chat_id,
            "latitude": latitude,
            "longitude": longitude,
            "title": title,
            "address": address,
        }
        if foursquare_id:
            data["foursquare_id"] = foursquare_id
        if foursquare_type:
            data["foursquare_type"] = foursquare_type
        if google_place_id:
            data["google_place_id"] = google_place_id
        if google_place_type:
            data["google_place_type"] = google_place_type
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendVenue", data)
        return result.get("result", {})

    async def send_contact(
        self,
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {
            "chat_id": chat_id,
            "phone_number": phone_number,
            "first_name": first_name,
        }
        if last_name:
            data["last_name"] = last_name
        if vcard:
            data["vcard"] = vcard
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendContact", data)
        return result.get("result", {})

    async def send_poll(
        self,
        chat_id: Union[int, str],
        question: str,
        options: list,
        is_anonymous: Optional[bool] = None,
        type: Optional[str] = None,
        allows_multiple_answers: Optional[bool] = None,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional[str] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
        is_closed: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {
            "chat_id": chat_id,
            "question": question,
            "options": options,
        }
        if is_anonymous is not None:
            data["is_anonymous"] = is_anonymous
        if type:
            data["type"] = type
        if allows_multiple_answers is not None:
            data["allows_multiple_answers"] = allows_multiple_answers
        if correct_option_id is not None:
            data["correct_option_id"] = correct_option_id
        if explanation:
            data["explanation"] = explanation
        if explanation_parse_mode:
            data["explanation_parse_mode"] = explanation_parse_mode
        if open_period:
            data["open_period"] = open_period
        if close_date:
            data["close_date"] = close_date
        if is_closed is not None:
            data["is_closed"] = is_closed
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendPoll", data)
        return result.get("result", {})

    async def send_dice(
        self,
        chat_id: Union[int, str],
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id}
        if emoji:
            data["emoji"] = emoji
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendDice", data)
        return result.get("result", {})

    async def send_sticker(
        self,
        chat_id: Union[int, str],
        sticker: str,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "sticker": sticker}
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendSticker", data)
        return result.get("result", {})

    async def get_file(
        self,
        file_id: str,
    ) -> Dict[str, Any]:
        data = {"file_id": file_id}
        result = self.request("getFile", data)
        return result.get("result", {})

    async def answer_inline_query(
        self,
        inline_query_id: str,
        results: List[Dict[str, Any]],
        cache_time: Optional[int] = None,
        is_personal: Optional[bool] = None,
        next_offset: Optional[str] = None,
        switch_pm_text: Optional[str] = None,
        switch_pm_parameter: Optional[str] = None,
    ) -> bool:
        data = {"inline_query_id": inline_query_id, "results": results}
        if cache_time:
            data["cache_time"] = cache_time
        if is_personal is not None:
            data["is_personal"] = is_personal
        if next_offset:
            data["next_offset"] = next_offset
        if switch_pm_text:
            data["switch_pm_text"] = switch_pm_text
        if switch_pm_parameter:
            data["switch_pm_parameter"] = switch_pm_parameter

        result = self.request("answerInlineQuery", data)
        return result.get("ok", False)

    async def send_invoice(
        self,
        chat_id: Union[int, str],
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: List[Dict[str, Any]],
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[List[int]] = None,
        start_parameter: Optional[str] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {
            "chat_id": chat_id,
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": provider_token,
            "currency": currency,
            "prices": prices,
        }
        if max_tip_amount:
            data["max_tip_amount"] = max_tip_amount
        if suggested_tip_amounts:
            data["suggested_tip_amounts"] = suggested_tip_amounts
        if start_parameter:
            data["start_parameter"] = start_parameter
        if provider_data:
            data["provider_data"] = provider_data
        if photo_url:
            data["photo_url"] = photo_url
        if need_name is not None:
            data["need_name"] = need_name
        if need_phone_number is not None:
            data["need_phone_number"] = need_phone_number
        if need_email is not None:
            data["need_email"] = need_email
        if need_shipping_address is not None:
            data["need_shipping_address"] = need_shipping_address
        if send_phone_number_to_provider is not None:
            data["send_phone_number_to_provider"] = send_phone_number_to_provider
        if send_email_to_provider is not None:
            data["send_email_to_provider"] = send_email_to_provider
        if is_flexible is not None:
            data["is_flexible"] = is_flexible
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendInvoice", data)
        return result.get("result", {})

    async def set_chat_menu_button(
        self,
        chat_id: Optional[int] = None,
        menu_button: Optional[Dict[str, Any]] = None,
    ) -> bool:
        data = {}
        if chat_id:
            data["chat_id"] = chat_id
        if menu_button:
            data["menu_button"] = menu_button

        result = self.request("setChatMenuButton", data)
        return result.get("ok", False)

    async def get_chat_menu_button(
        self,
        chat_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        data = {}
        if chat_id:
            data["chat_id"] = chat_id

        result = self.request("getChatMenuButton", data)
        return result.get("result", {})

    async def send_dice(
        self,
        chat_id: Union[int, str],
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id}
        if emoji:
            data["emoji"] = emoji
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendDice", data)
        return result.get("result", {})

    async def send_audio(
        self,
        chat_id: Union[int, str],
        audio: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        thumb: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "audio": audio}
        if caption:
            data["caption"] = caption
        if parse_mode:
            data["parse_mode"] = parse_mode
        if duration:
            data["duration"] = duration
        if performer:
            data["performer"] = performer
        if title:
            data["title"] = title
        if thumb:
            data["thumb"] = thumb
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendAudio", data)
        return result.get("result", {})

    async def send_document(
        self,
        chat_id: Union[int, str],
        document: str,
        thumb: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "document": document}
        if thumb:
            data["thumb"] = thumb
        if caption:
            data["caption"] = caption
        if parse_mode:
            data["parse_mode"] = parse_mode
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendDocument", data)
        return result.get("result", {})

    async def send_video(
        self,
        chat_id: Union[int, str],
        video: str,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumb: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        supports_streaming: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "video": video}
        if duration:
            data["duration"] = duration
        if width:
            data["width"] = width
        if height:
            data["height"] = height
        if thumb:
            data["thumb"] = thumb
        if caption:
            data["caption"] = caption
        if parse_mode:
            data["parse_mode"] = parse_mode
        if supports_streaming is not None:
            data["supports_streaming"] = supports_streaming
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendVideo", data)
        return result.get("result", {})

    async def send_animation(
        self,
        chat_id: Union[int, str],
        animation: str,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumb: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "animation": animation}
        if duration:
            data["duration"] = duration
        if width:
            data["width"] = width
        if height:
            data["height"] = height
        if thumb:
            data["thumb"] = thumb
        if caption:
            data["caption"] = caption
        if parse_mode:
            data["parse_mode"] = parse_mode
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendAnimation", data)
        return result.get("result", {})

    async def send_voice(
        self,
        chat_id: Union[int, str],
        voice: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "voice": voice}
        if caption:
            data["caption"] = caption
        if parse_mode:
            data["parse_mode"] = parse_mode
        if duration:
            data["duration"] = duration
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendVoice", data)
        return result.get("result", {})

    async def send_video_note(
        self,
        chat_id: Union[int, str],
        video_note: str,
        duration: Optional[int] = None,
        length: Optional[int] = None,
        thumb: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "video_note": video_note}
        if duration:
            data["duration"] = duration
        if length:
            data["length"] = length
        if thumb:
            data["thumb"] = thumb
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendVideoNote", data)
        return result.get("result", {})

    async def send_location(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "latitude": latitude, "longitude": longitude}
        if horizontal_accuracy:
            data["horizontal_accuracy"] = horizontal_accuracy
        if live_period:
            data["live_period"] = live_period
        if heading:
            data["heading"] = heading
        if proximity_alert_radius:
            data["proximity_alert_radius"] = proximity_alert_radius
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendLocation", data)
        return result.get("result", {})

    async def send_venue(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {
            "chat_id": chat_id,
            "latitude": latitude,
            "longitude": longitude,
            "title": title,
            "address": address,
        }
        if foursquare_id:
            data["foursquare_id"] = foursquare_id
        if foursquare_type:
            data["foursquare_type"] = foursquare_type
        if google_place_id:
            data["google_place_id"] = google_place_id
        if google_place_type:
            data["google_place_type"] = google_place_type
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendVenue", data)
        return result.get("result", {})

    async def send_contact(
        self,
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {
            "chat_id": chat_id,
            "phone_number": phone_number,
            "first_name": first_name,
        }
        if last_name:
            data["last_name"] = last_name
        if vcard:
            data["vcard"] = vcard
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendContact", data)
        return result.get("result", {})

    async def send_rich_message(
        self,
        chat_id: Union[int, str],
        message: Dict[str, Any],
        receiver_user_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "message": message}
        if receiver_user_id:
            data["receiver_user_id"] = receiver_user_id  # Ephemeral Messages
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendRichMessage", data)
        return result.get("result", {})

    async def send_rich_message_draft(
        self,
        chat_id: Union[int, str],
        draft: Dict[str, Any],
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "draft": draft}
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendRichMessageDraft", data)
        return result.get("result", {})

    async def get_managed_bot_token(
        self,
        bot_username: str,
        scope: Optional[str] = None,
        permissions: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"bot_username": bot_username}
        if scope:
            data["scope"] = scope
        if permissions:
            data["permissions"] = permissions

        result = self.request("getManagedBotToken", data)
        return result.get("result", {})

    # ========== Communities ==========
    async def create_community(
        self,
        title: str,
        description: str,
        members: Optional[List[Union[int, str]]] = None,
    ) -> Dict[str, Any]:
        data = {"title": title, "description": description}
        if members:
            data["members"] = members

        result = self.request("createCommunity", data)
        return result.get("result", {})

    async def edit_community(
        self,
        community_id: Union[int, str],
        title: Optional[str] = None,
        description: Optional[str] = None,
    ) -> bool:
        data = {"community_id": community_id}
        if title:
            data["title"] = title
        if description:
            data["description"] = description

        result = self.request("editCommunity", data)
        return result.get("ok", False)

    async def delete_community(
        self,
        community_id: Union[int, str],
    ) -> bool:
        data = {"community_id": community_id}
        result = self.request("deleteCommunity", data)
        return result.get("ok", False)

    async def add_community_member(
        self,
        community_id: Union[int, str],
        user_id: Union[int, str],
    ) -> bool:
        data = {"community_id": community_id, "user_id": user_id}
        result = self.request("addCommunityMember", data)
        return result.get("ok", False)

    async def remove_community_member(
        self,
        community_id: Union[int, str],
        user_id: Union[int, str],
    ) -> bool:
        data = {"community_id": community_id, "user_id": user_id}
        result = self.request("removeCommunityMember", data)
        return result.get("ok", False)

    # ========== Subscription & Payment ==========
    async def send_subscription_invoice(
        self,
        chat_id: Union[int, str],
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: List[Dict[str, Any]],
        subscription_period: str,
        subscription_price: Dict[str, Any],
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {
            "chat_id": chat_id,
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": provider_token,
            "currency": currency,
            "prices": prices,
            "subscription_period": subscription_period,
            "subscription_price": subscription_price,
        }
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendSubscriptionInvoice", data)
        return result.get("result", {})

    # ========== Live Photos ==========
    async def send_live_photo(
        self,
        chat_id: Union[int, str],
        photo: str,
        video: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "photo": photo, "video": video}
        if caption:
            data["caption"] = caption
        if parse_mode:
            data["parse_mode"] = parse_mode
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendLivePhoto", data)
        return result.get("result", {})

    # ========== Guest Mode ==========
    async def send_message_guest(
        self,
        chat_id: Union[int, str],
        text: str,
        parse_mode: Optional[str] = None,
        entities: Optional[list] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"chat_id": chat_id, "text": text, "guest_mode": True}
        if parse_mode:
            data["parse_mode"] = parse_mode
        if entities:
            data["entities"] = entities
        if disable_web_page_preview is not None:
            data["disable_web_page_preview"] = disable_web_page_preview
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendMessage", data)
        return result.get("result", {})

    # ========== Polls (minimal 1 opsi) ==========
    async def send_poll(
        self,
        chat_id: Union[int, str],
        question: str,
        options: list,
        is_anonymous: Optional[bool] = None,
        type: Optional[str] = None,
        allows_multiple_answers: Optional[bool] = None,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional[str] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
        is_closed: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        if len(options) < 1:
            raise ValueError("Poll must have at least 1 option")

        data = {
            "chat_id": chat_id,
            "question": question,
            "options": options,
        }
        if is_anonymous is not None:
            data["is_anonymous"] = is_anonymous
        if type:
            data["type"] = type
        if allows_multiple_answers is not None:
            data["allows_multiple_answers"] = allows_multiple_answers
        if correct_option_id is not None:
            data["correct_option_id"] = correct_option_id
        if explanation:
            data["explanation"] = explanation
        if explanation_parse_mode:
            data["explanation_parse_mode"] = explanation_parse_mode
        if open_period:
            data["open_period"] = open_period
        if close_date:
            data["close_date"] = close_date
        if is_closed is not None:
            data["is_closed"] = is_closed
        if disable_notification is not None:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        if allow_sending_without_reply is not None:
            data["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup:
            data["reply_markup"] = reply_markup

        result = self.request("sendPoll", data)
        return result.get("result", {})
        result = self.request("getChat", data)
        return result.get("result", {})