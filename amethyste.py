# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://github.com/AmoreForever/assets/blob/master/Amethyste.jpg?raw=true

from .. import utils, loader
from hikkatl.errors.common import AlreadyInConversationError
from telethon.tl.types import Message


@loader.tds
class Amethyste(loader.Module):
    """Generate memes image"""

    strings = {
        "name": "Amethyste",
        "wait": "<emoji document_id=5328115567314346398>🫥</emoji> <b>Wait...</b>",
        "already_open": "<emoji document_id=5330241494521487534>😹</emoji> <b>Conversation already opened Please wait.</b>",
        "r_photo": "<emoji document_id=5298636457982826800>🖼</emoji> <b>Please reply to image.</b>",
        "no_args": "<emoji document_id=5877477244938489129>🚫</emoji> <b>Pls provide args</b>",
        "not_found": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji> <b>Not found</b>",
    }

    strings_ru = {
        "wait": "<emoji document_id=5328115567314346398>🫥</emoji> <b>Подождите...</b>",
        "already_open": "<emoji document_id=5330241494521487534>😹</emoji> <b>Диалог уже открыт. Подождите.</b>",
        "r_photo": "<emoji document_id=5298636457982826800>🖼</emoji> <b>Ответьте на фото.</b>",
        "no_args": "<emoji document_id=5877477244938489129>🚫</emoji> <b>Укажите аргументы</b>",
        "not_found": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji> <b>Не найдено</b>",
    }

    strings_uz = {
        "wait": "<emoji document_id=5328115567314346398>🫥</emoji> <b>Kuting...</b>",
        "already_open": "<emoji document_id=5330241494521487534>😹</emoji> <b>Dialog allaqachon ochilgan. Iltimos, kuting.</b>",
        "r_photo": "<emoji document_id=5298636457982826800>🖼</emoji> <b>Rasmga javob bering.</b>",
        "no_args": "<emoji document_id=5877477244938489129>🚫</emoji> <b>Argumetlarni ko'rsating</b>",
        "not_found": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji> <b>Topilmadi</b>",
    }

    _list = [
        "3000years",
        "approved",
        "beautiful",
        "brazzers",
        "burn",
        "challenger",
        "circle",
        "contrast",
        "crush",
        "ddungeon",
        "dictator",
        "distort",
        "emboss",
        "fire",
        "frame",
        "afusion",
        "glitch",
        "greyscale",
        "instagram",
        "invert",
        "jail",
        "magik",
        "missionpassed",
        "moustache",
        "ps4",
        "posterize",
        "rejected",
        "rip",
        "scary",
        "scrolloftruth",
        "sepia",
        "sharpen",
        "sniper",
        "thanos",
        "trinity",
        "triggered",
        "unsharpen",
        "utatoo",
        "wanted",
        "wasted",
    ]

    async def amegencmd(self, message: Message):
        """Generate memes image"""
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        await utils.answer(message, self.strings["wait"])
        if not args:
            return await utils.answer(message, self.strings["no_args"])
        elif not reply.photo:
            return await utils.answer(message, self.strings["r_photo"])
        elif args not in self._list:
            return await utils.answer(message, self.strings["not_found"])
        async with self.client.conversation("@aozoram_bot") as conv:
            try:
                msg = await conv.send_message("/start")
                s = await conv.get_response()
                f = await conv.send_file(file=reply)
                m = await f.reply(f"/amegen {args}")
                await conv.get_response()  # wait for response
                response = await conv.get_response()
                await utils.answer_file(message, response.media)
                await s.delete()
                await msg.delete()
                await m.delete()
            except AlreadyInConversationError:
                await utils.answer(message, self.strings["already_open"])
        await self.client.delete_dialog("@aozoram_bot")

    async def amelistcmd(self, message: Message):
        """List of memes"""
        spis = "\n".join([f"• <code>{i}</code>" for i in self._list])
        await utils.answer(message, f"<b>Available memes:</b>\n\n{spis}")
