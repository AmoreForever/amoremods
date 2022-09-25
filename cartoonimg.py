#            ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#            █▀█ █░▀░█ █▄█ █▀▄ ██▄
#
#          https://t.me/the_farkhodov
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @amoremods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Cartoon.jpg
__version__ = (1, 0, 0)

import imghdr
import io
import random

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import Message
from .. import loader, utils

chat = "@PhotoCartoonEffectBot"

class CartoonMod(loader.Module):
    """Make Cartoon image"""

    strings = {
        "name": "CartoonIMG",
        "processing": (
            "<emoji document_id=5787254181211409873>🖌</emoji> <b>Processing...</b>"
        ),
        "only_photo": (
            "<emoji document_id=4920738602188538629>💬</emoji> Reply to photo"
        ),
        "what": (
            "<emoji document_id=4920604831137137376>❔</emoji> No reply or photo"
        )
    }
    
    strings_ru = {
        "processing": (
            "<emoji document_id=5787254181211409873>🖌</emoji> <b>Процесс...</b>"
        ),
        "only_photo": (
            "<emoji document_id=4920738602188538629>💬</emoji> Ответом на фото"
        ),
        "what": (
            "<emoji document_id=4920604831137137376>❔</emoji> Нет реплая или фото"
        )
    }

    async def get_media(self, message: Message):
        reply = await message.get_reply_message()
        m = None
        if reply and reply.media:
            m = reply
        elif message.media:
            m = message
        elif not reply:
            await utils.answer(message, self.strings("what"))
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
                            random.choice("abcdefghijklmnopqrstuvwxyz1234567890")
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

        if imghdr.what(file) not in ["png", "jpg", "jpeg"]:
            await utils.answer(message, self.strings("only_photo"))
            return False

        return file

    async def captcmd(self, message: Message):
        """mult photo"""
        message = await utils.answer(message, self.strings("processing"))   
        await message.delete()
        file = await self.get_image(message)
        if not file:
            return

        async with self._client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("🌀 Multik Rasm")
                amore = await conv.send_message(file=file)
                m = await conv.get_response()
            except YouBlockedUserError:
                await utils.answer(message, self.strings("ban"))
                return

            await self._client.send_file(
            message.peer_id,
            m.media,
            reply_to=message.reply_to_msg_id,
        )
         
            await self.client.delete_dialog(chat)
