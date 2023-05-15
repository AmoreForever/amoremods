# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta pic: https://te.legra.ph/file/868a280910e7f61f6ab0e.png
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Abstract.jpg


from .. import utils, loader

chat = "@aeabstractbot"


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
            reply_to=message.reply_to_msg_id,
        )

        for msg in msgs + [m]:
            await msg.delete()

        if message.out:
            await message.delete()

        await self.client.delete_dialog(chat)
