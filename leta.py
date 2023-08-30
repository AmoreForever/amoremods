# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru


# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/leta.jpg

# I don't care about other people's opinions, if you don't like it, don't use it. i will update this module in the future, if i have time.

import time 
import logging
from .. import loader, utils
from telethon.errors import ChatAdminRequiredError

logger = logging.getLogger(__name__)

class Leta(loader.Module):
    """Customizable nightmode [Leta] for your group"""
    
    strings = {
        "name": "Leta",
        "info": (
                "🐈‍⬛ Heeey! I'm <b>Leta</b>! I'm a module for nightmode in your group.\n"
                "📫 You can get acquainted with my settings using the command <code>.help Leta</code>."
            ),
        "wrong_format": "<emoji document_id=5258419835922030550>🕔</emoji> <b>Enter the time in the format HH:MM</b>",
        "day": "<emoji document_id=6334559815041287464>🌞</emoji> <b>Good morning!</b>\n<b>Night mode is disabled.</b>",
        "night": "<emoji document_id=6334806423473489632>🌚</emoji> <b>Good night!</b>\n<b>Night mode is enabled.</b>",
        "mor_set": "<emoji document_id=5021905410089550576>✅</emoji> <b>Morning time set to: <code>{}</code> in this chat.</b>",
        "ngs_set": "<emoji document_id=5021905410089550576>✅</emoji> <b>Night time set to: <code>{}</code> in this chat.</b>",
        "rm": "<emoji document_id=5021905410089550576>✅</emoji> <b>Removed nightmode.</b>",
        "rm_notfound": "<emoji document_id=5456652110143693064>🤷‍♂️</emoji> <b>Nightmode is not set.</b>",
        }
    
    strings_ru = {
        "info": (
                "🐈‍⬛ Привет! Я <b>Leta</b>! Я модуль для ночного режима в вашей группе.\n"
                "📫 Ознакомиться с моими настройками можно с помощью команды <code>.help Leta</code>."
            ),
        "wrong_format": "<emoji document_id=5258419835922030550>🕔</emoji> <b>Введите время в формате HH:MM</b>",
        "day": "<emoji document_id=6334559815041287464>🌞</emoji> <b>Доброе утро!</b>\n<b>Ночной режим отключен.</b>",
        "night": "<emoji document_id=6334806423473489632>🌚</emoji> <b>Доброй ночи!</b>\n<b>Ночной режим включен.</b>",
        "mor_set": "<emoji document_id=5021905410089550576>✅</emoji> <b>Утреннее время установлено на: <code>{}</code> в этом чате.</b>",
        "ngs_set": "<emoji document_id=5021905410089550576>✅</emoji> <b>Ночное время установлено на: <code>{}</code> в этом чате.</b>",
        "rm": "<emoji document_id=5021905410089550576>✅</emoji> <b>Удален ночной режим.</b>",
        "rm_notfound": "<emoji document_id=5456652110143693064>🤷‍♂️</emoji> <b>Ночной режим не установлен.</b>",
        }
    
    
    def resolve_id(self, marked_id):
        if marked_id >= 0:
            return "user"
        marked_id = -marked_id
        marked_id -= 1000000000000
        return "chat"
    
    async def client_ready(self, client, db):
        if not self.get("info", False):
            await self.inline.bot.send_animation(
                self._tg_id,
                "https://0x0.st/Hpqm.mp4",
                caption=self.strings("info"),
                parse_mode="HTML",
            )
            self.set("info", True)
            
                    
    async def letnightcmd(self, message):
        """Set night time [HH:MM]"""
        args = utils.get_args_raw(message)
        resolving = self.resolve_id(message.chat_id)
        logging.info(resolving)
        if resolving != "chat":
            return await utils.answer(message, "<b>Use this command in group</b>")
        if not args:
            return await utils.answer(message, self.strings("wrong_format"))
        if args.count(":") != 1:
            return await utils.answer(message, self.strings('wrong_format'))
        try:
            h, m = map(int, args.split(":"))
            if h > 23 or h < 0 or m > 59 or m < 0:
                return await utils.answer(message, self.strings('wrong_format'))
        except Exception:
            return await utils.answer(message, self.strings('wrong_format'))
        self.set(
            "ngs",
            {
               message.chat_id: {
                    "time": args,
                    "chat": message.chat_id
               },
            }
        )
        await utils.answer(message, self.strings("ngs_set").format(args))
        
    async def letdaycmd(self, message):
        """Set day time [HH:MM]"""
        args = utils.get_args_raw(message)
        if not args:
            return await utils.answer(message, self.strings('wrong_format'))
        if args.count(":") != 1:
            return await utils.answer(message, self.strings('wrong_format'))
        try:
            h, m = map(int, args.split(":"))
            if h > 23 or h < 0 or m > 59 or m < 0:
                return await utils.answer(message, self.strings('wrong_format'))
        except Exception:
            return await utils.answer(message, self.strings('wrong_format'))
        self.set(
            "ngs",
            {
               message.chat_id: {
                    "day": args,
               },
            }
        )
        await utils.answer(message, self.strings("mor_set").format(args))
        
    async def letrmchatcmd(self, message):
        """Remove nightmode - chat-id"""
        try:
            args = int(utils.get_args_raw(message))
            d = self.get("ngs", {})
            logging.info(d)
            if not args:
                return await utils.answer(message, self.strings("rm_notfound"))
            if args not in d:
                return await utils.answer(message, self.strings("rm_notfound"))
            del d[args]
            self.set("ngs", d)
            await utils.answer(message, self.strings("rm"))
        except ValueError:
            await utils.answer(message, self.strings("rm_notfound"))
        
    @loader.loop(interval=60, autostart=True)
    async def checker_loop_night(self):
        """Check time"""
        ngs = self.get("ngs", {})
        for i in ngs:
            if ngs[i]["time"] == time.strftime("%H:%M"):
                try:
                    await self.client.send_message(ngs[i]["chat"], self.strings("night"))
                    await self.client.edit_permissions(ngs[i]['chat'], send_messages=False)
                except ChatAdminRequiredError:
                    await self.inline.bot.send_message(
                        self._tg_id,
                        f"👎 You don't have enough rights to change permissions in <code>{i['chat']}</code>",
                        parse_mode="HTML",
                    )
                    
    async def letchatscmd(self, message):
        """Get all chats with nightmode"""
        ngs = self.get("ngs", {})
        if not ngs:
            return await utils.answer(message, "<b>There are no chats with nightmode</b>")
        msg = "<b>Chats with nightmode:</b>\n"
        for i in ngs:
            msg += f"\n<code>{i}</code>"
        await utils.answer(message, msg + "\n")

    @loader.loop(interval=60, autostart=True)
    async def checker_loop_day(self):
        """Check time"""
        ngs = self.get("ngs", {})
        for i in ngs:
            if ngs[i]["day"] == time.strftime("%H:%M"):
                try:
                    await self.client.edit_permissions(ngs[i]['chat'], send_messages=True)
                    await self.client.send_message(ngs[i]["chat"], self.strings("day"))
                except ChatAdminRequiredError:
                    await self.inline.bot.send_message(
                        self._tg_id,
                        f"👎 You don't have enough rights to change permissions in <code>{i['chat']}</code>",
                        parse_mode="HTML",
                    )