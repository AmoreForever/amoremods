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
# meta pic: https://imgur.com/4W7CzvT
# meta banner: https://imgur.com/fQebpqe

from telethon import events
from .. import utils, loader

chat = "@UltraDownBot"


class InstagramMod(loader.Module):
    """Download video from instagram without watermark"""

    strings = {
        "name": "InstSave",
        "processing": (
            "<emoji document_id='6318766236746384900'>🕔</emoji> <b>Processing...</b>"
        ),
        "mods": (
            "<b>Successfuly downloaded</b> <emoji document_id='6320882302708614449'>🚀</emoji></b>"
        ),        
    }

    @loader.group_member
    @loader.command(ru_doc="<линк> - Скачать видео из инстаграм")
    async def instascmd(self, message):
        """instagram video/reels/photo url"""
        text = utils.get_args_raw(message)
        message = await utils.answer(message, self.strings("processing"))
        async with self._client.conversation(chat) as conv:
            msgs = []
            msgs += [await conv.send_message("/start")]
            msgs += [await conv.get_response()]
            msgs += [await conv.send_message(text)]
            m = await conv.get_response()

        await self._client.send_file(
            message.peer_id,
            m.media,
            caption=self.strings("mods"),
            reply_to=message.reply_to_msg_id,
        )

        for msg in msgs + [m]:
            await msg.delete()

        if message.out:
            await message.delete()

        await self.client.delete_dialog(chat)
