# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta pic: https://te.legra.ph/file/0251f5d602a8f32cd7368.png
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Instsave.jpg
__version__ = (1, 0, 0)

from .. import utils, loader

chat = "@SaveAsBot"


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
