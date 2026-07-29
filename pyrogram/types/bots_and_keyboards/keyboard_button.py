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

from typing import Optional

from pyrogram import raw, enums, types
from ..object import Object


def _build_raw_style(
    style: "enums.ButtonStyle",
    icon: int = None
) -> Optional["raw.types.KeyboardButtonStyle"]:
    """Build a raw KeyboardButtonStyle from a color style and/or a custom emoji icon id.

    A style object is emitted whenever *either* a color style or a custom emoji icon is given,
    so a premium/custom emoji icon can be used on a button with no color at all.
    """
    has_color = style is not None and style != enums.ButtonStyle.DEFAULT

    if not has_color and icon is None:
        return None

    return raw.types.KeyboardButtonStyle(
        bg_primary=(style == enums.ButtonStyle.PRIMARY),
        bg_danger=(style == enums.ButtonStyle.DANGER),
        bg_success=(style == enums.ButtonStyle.SUCCESS),
        icon=int(icon) if icon is not None else None,
    )


def _read_raw_style(b) -> Optional["enums.ButtonStyle"]:
    """Read raw KeyboardButtonStyle and return ButtonStyle enum."""
    s = getattr(b, "style", None)
    if s is None:
        return None
    if getattr(s, "bg_primary", False):
        return enums.ButtonStyle.PRIMARY
    if getattr(s, "bg_danger", False):
        return enums.ButtonStyle.DANGER
    if getattr(s, "bg_success", False):
        return enums.ButtonStyle.SUCCESS
    return enums.ButtonStyle.DEFAULT


def _read_raw_icon(b) -> Optional[int]:
    """Read the custom emoji id used as icon from a raw KeyboardButtonStyle, if any."""
    s = getattr(b, "style", None)
    return getattr(s, "icon", None) if s is not None else None


class KeyboardButton(Object):
    """One button of the reply keyboard.

    For simple text buttons String can be used instead of this object to specify text of the button.
    Optional fields are mutually exclusive.

    Parameters:
        text (``str``):\n            Text of the button.

        request_contact (``bool``, *optional*):\n            If True, the user's phone number will be sent as a contact when the button is pressed.

        request_location (``bool``, *optional*):\n            If True, the user's current location will be sent when the button is pressed.

        web_app (:obj:`~pyrogram.types.WebAppInfo`, *optional*):\n            If specified, the described Web App will be launched when the button is pressed.

        style (:obj:`~pyrogram.enums.ButtonStyle`, *optional*):\n            Button color style. Use PRIMARY, DANGER, or SUCCESS.

        style_icon (``int``, *optional*):\n            Deprecated alias of ``icon_custom_emoji_id``. Kept for backward compatibility.

        icon_custom_emoji_id (``int``, *optional*):\n            Identifier of a custom emoji (premium emoji) to be shown as an icon on the button.
            Works with or without ``style``.
    """

    def __init__(
        self,
        text: str,
        request_contact: bool = None,
        request_location: bool = None,
        web_app: "types.WebAppInfo" = None,
        style: "enums.ButtonStyle" = None,
        style_icon: Optional[int] = None,
        icon_custom_emoji_id: Optional[int] = None,
    ):
        super().__init__()

        self.text = str(text)
        self.request_contact = request_contact
        self.request_location = request_location
        self.web_app = web_app
        self.style = style
        # ``icon_custom_emoji_id`` is the canonical name; ``style_icon`` is the legacy alias.
        self.icon_custom_emoji_id = (
            icon_custom_emoji_id if icon_custom_emoji_id is not None else style_icon
        )

    @property
    def style_icon(self) -> Optional[int]:
        """Deprecated alias of :attr:`icon_custom_emoji_id`."""
        return self.icon_custom_emoji_id

    @style_icon.setter
    def style_icon(self, value: Optional[int]):
        self.icon_custom_emoji_id = value

    @staticmethod
    def read(b):
        style = _read_raw_style(b)
        icon = _read_raw_icon(b)

        if isinstance(b, raw.types.KeyboardButtonRequestPhone):
            return KeyboardButton(
                text=b.text,
                request_contact=True,
                style=style,
                icon_custom_emoji_id=icon,
            )

        if isinstance(b, raw.types.KeyboardButtonRequestGeoLocation):
            return KeyboardButton(
                text=b.text,
                request_location=True,
                style=style,
                icon_custom_emoji_id=icon,
            )

        if isinstance(b, raw.types.KeyboardButtonSimpleWebView):
            return KeyboardButton(
                text=b.text,
                web_app=types.WebAppInfo(url=b.url),
                style=style,
                icon_custom_emoji_id=icon,
            )

        if isinstance(b, raw.types.KeyboardButton):
            # A styled plain button must keep its style, so it can no longer be
            # collapsed into a bare string.
            if style is None and icon is None:
                return b.text

            return KeyboardButton(
                text=b.text,
                style=style,
                icon_custom_emoji_id=icon,
            )

    def write(self):
        raw_style = _build_raw_style(self.style, self.icon_custom_emoji_id)

        if self.request_contact:
            return raw.types.KeyboardButtonRequestPhone(text=self.text, style=raw_style)
        elif self.request_location:
            return raw.types.KeyboardButtonRequestGeoLocation(text=self.text, style=raw_style)
        elif self.web_app:
            return raw.types.KeyboardButtonSimpleWebView(text=self.text, url=self.web_app.url, style=raw_style)
        else:
            return raw.types.KeyboardButton(text=self.text, style=raw_style)
