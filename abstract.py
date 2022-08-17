# ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
# █▀█ █░▀░█ █▄█ █▀▄ ██▄
#
#             © Copyright 2022
#
#          https://t.me/the_farkhodov
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: inline
# scope: hikka_only
# scope: hikka_min 1.3.0
# meta developer: @amoremods
# meta pic: https://imgur.com/WoKzecb
# meta banner: https://imgur.com/EzGrs6h

from telethon import events
from .. import utils, loader

chat = "@amoreconverterbot"


class AbstractMod(loader.Module):
    """Write a beautiful summary on a notebook"""

    strings = {
        "name": "Abstract",
        "processing": (
            "<emoji document_id='6318766236746384900'>🕔</emoji> <b>Processing...</b>"
        ),
    }

    @loader.owner
    @loader.command(ru_doc="<текст> - Создать конспект")
    async def konspcmd(self, message):
        """<text> - Create summary"""
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
            caption="❤ @amoremods",
            reply_to=message.reply_to_msg_id,
        )

        for msg in msgs + [m]:
            await msg.delete()

        if message.out:
            await message.delete()

        await self.client.delete_dialog(chat)
