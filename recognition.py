# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/recognition.jpg

from .. import utils, loader
import imghdr
import io
import random
from telethon.tl.types import Message


@loader.tds
class RecognitionMod(loader.Module):
    """Recognition from photo"""

    strings = {
        'name': 'Recognition',
        'args': "No args!"
    }

    async def get_media(self, message: Message):
        reply = await message.get_reply_message()
        m = None
        if reply and reply.media:
            m = reply
        elif message.media:
            m = message
        elif not reply:
            await utils.answer(message, self.strings('args'))
            return False

        if not m:
            file = io.BytesIO(bytes(reply.raw_text, "utf-8"))
            file.name = "file.txt"
        else:
            file = io.BytesIO(await self._client.download_media(m, bytes))
            file.name = (
                m.file.name
                or (
                    "".join(
                        [
                            random.choice(
                                "abcdefghijklmnopqrstuvwxyz1234567890")
                            for _ in range(16)
                        ]
                    )
                )
                + m.file.ext
            )

        return file

    async def get_image(self, message: Message):
        file = await self.get_media(message)
        if not file:
            return False

        if imghdr.what(file) not in ["gif", "png", "jpg", "jpeg", "tiff", "bmp"]:
            return False
        return file

    @loader.command()
    async def reco(self, message: Message):
        """recognize from photo <reply to photo>"""
        file = await self.get_image(message)
        if not file:
            return False
        async with self._client.conversation("@Rekognition_Bot") as conv:
            await conv.send_message(file=file)  # upload step
            await conv.get_response()  # ignore message
            cp = await conv.get_response()  # get message

        await utils.answer(message, cp)
        await self.client.delete_dialog("@Rekognition_Bot")
