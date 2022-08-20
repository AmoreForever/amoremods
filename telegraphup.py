#        ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#        █▀█ █░▀░█ █▄█ █▀▄ ██▄
#
#                 © Copyright 2022
#
#          https://t.me/the_farkhodov
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.3.0
# meta developer: @amoremods
# meta pic: https://te.legra.ph/file/5ef64ee0466032d8a4687.png
# meta banner: https://imgur.com/rb3bkdJ

from .. import loader, utils
import asyncio
import requests
from telethon.tl.types import DocumentAttributeFilename


@loader.tds
class Telegraph(loader.Module):
    """Upload video and photo to telegraph"""

    strings = {
        "name": "TelegraphUP",
        "here": "✨ Your file here",
        "info": "ℹ Info",
        "pls_reply": "⚠️ Reply to photo or video/gif",
    }

    @loader.sudo
    async def thupcmd(self, message):
        """<reply photo or video>"""
        if message.is_reply:
            reply_message = await message.get_reply_message()
            data = await check_media(reply_message)
            if isinstance(data, bool):
                await message.edit(self.strings("pls_reply"))
                return
        else:
            await message.edit(self.strings("pls_reply"))
            return

        file = await message.client.download_media(data, bytes)
        path = requests.post(
            "https://te.legra.ph/upload", files={"file": ("file", file, None)}
        ).json()
        try:
            amore = "https://te.legra.ph" + path[0]["src"]
        except KeyError:
            amore = path["error"]
        await self.inline.form(
            text=f"🦜 Your file has been successfully uploaded. \n💾 Copy link: <code>{amore}</code>",
            reply_markup=[
                [
                    {
                        "text": self.strings("here"),
                        "url": f"{amore}",
                    }
                ],
                [
                    {
                        "text": self.strings("info"),
                        "action": "answer",
                        "message": "ℹ This module upload photo/video/gif to telegra.ph",
                    }
                ],
            ],
            **{"photo": f"{amore}"},
            message=message,
        )


async def check_media(reply_message):
    if reply_message and reply_message.media:
        if reply_message.photo:
            data = reply_message.photo
        elif reply_message.document:
            if (
                DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
                in reply_message.media.document.attributes
            ):
                return False
            if reply_message.audio or reply_message.voice:
                return False
            data = reply_message.media.document
        else:
            return False
    else:
        return False
    if not data or data is None:
        return False
    else:
        return data
