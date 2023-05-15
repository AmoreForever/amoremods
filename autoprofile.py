#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods, FTG
__version__ = (1, 1, 0)

import asyncio
import datetime

from telethon.tl import functions
from telethon.utils import get_display_name

from .. import loader, utils


@loader.tds
class AutoProfileMod(loader.Module):
    """Automatic stuff for your profile :P"""

    strings = {
        "name": "AutoProfile",
        "invalid_args": (
            "<b>Missing parameters, please read the <code>.aguide</code>  <emoji document_id=5213468029597261187>✔️</emoji></b>"
        ),
        "missing_time": (
            "<b>Time was not specified in bio <emoji document_id=5215273032553078755>❎</emoji></b>"
        ),
        "enabled_bio": (
            "<b>Enabled bio clock <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),
        "bio_not_enabled": (
            "<b>Bio clock is not enabled <emoji document_id=5215273032553078755>❎</emoji></b>"
        ),
        "disabled_bio": (
            "<b>Disabled bio clock <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),
        "enabled_name": ( 
            "<b>Enabled name clock <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),
        "name_not_enabled": (
            "<b>Name clock is not enabled <emoji document_id=5215273032553078755>❎</emoji></b>"
        ),
        "disabled_name": (
            "<b>Name clock disabled <emoji document_id=5215273032553078755>❎</emoji></b>"
        ),
        "_cfg_time": "Use timezone 1, -1, -3 etc.",
    }

    strings_uz = {
        "invalid_args": (
            "<b>to'g'ri argumetlar emas, <code > ni o'qing.aguide</code> <emoji document_id=5213468029597261187>✔️</emoji></b>"
        ),
        "missing_time": (
            "<b>vaqt bio-da o'rnatilmagan<emoji document_id=5215273032553078755 > ❎< / emoji></b>"
        ),
        "enabled_bio": (
            "<b>Bio soat muvaffaqiyatli o'rnatildi <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),
        "bio_not_enabled": (
            "<b>soat bio-ga o'rnatilmagan<emoji document_id=5215273032553078755 > ❎< / emoji > </b>"
        ),
        "disabled_bio": (
            "<b > Bio-dagi vaqt muvaffaqiyatli o'chirildi <emoji document_id = 5212932275376759608>✅</emoji></b>"
        ),
        "enabled_name": (
            "<b>soat taxallusga muvaffaqiyatli o'rnatildi <emoji document_id = 5212932275376759608>✅</emoji></b>"
        ),
        "name_not_enabled": (
            "<b>soat taxallusga o'rnatilmagan<emoji document_id=5215273032553078755 > ❎< / emoji > </b>"
        ),
        "disabled_name": (
            "<b>taxallusdagi vaqt muvaffaqiyatli o'chirildi <emoji document_id = 5212932275376759608>✅</emoji></b>"
        ),  
        "_cfg_time": "vaqt zonasidan foydalaning 1, -1, -3 va boshqalar.",
    }

    strings_ru = {
        "invalid_args": (
            "<b>Не правильные аргуметы, прочитай <code>.aguide</code> <emoji document_id=5213468029597261187>✔️</emoji></b>"
        ),
        "missing_time": (
            "<b>Время не было установлено в био<emoji document_id=5215273032553078755>❎</emoji></b>"
        ),
        "enabled_bio": (
            "<b>Био часы успешно установлены <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),
        "bio_not_enabled": (
            "<b>Часы не установлено в био<emoji document_id=5215273032553078755>❎</emoji></b>"
        ),
        "disabled_bio": (
            "<b>Время в био успешно отключен <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),
        "enabled_name": (
            "<b>Часы в ник успешно установлены <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),
        "name_not_enabled": (
            "<b>Часы не установлены в ник<emoji document_id=5215273032553078755>❎</emoji></b>"
        ),
        "disabled_name": (
            "<b>Время в нике успешно отключен <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),  
        "_cfg_time": "Используй таймзону 1, -1, -3 и тд.",
    }

    strings_de = {
        "invalid_args": (
            "<b>Sind nicht die richtigen Argumente, lies <code>.aguide</code> <emoji document_id=5213468029597261187>✔️</emoji></b>"
        ),
        "missing_time": (
            "<b>Die Zeit wurde nicht auf bio gesetzt<emoji document_id=5215273032553078755>❎</emoji></b>"
        ),
        "enabled_bio": (
            "<b>Bio-Uhr wurde erfolgreich installiert <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),
        "bio_not_enabled": (
            "<b>Die Uhr ist nicht auf bio eingestellt<emoji document_id=5215273032553078755>❎</emoji></b>"
        ),
        "disabled_bio": (
            "<b>Zeit in bio erfolgreich deaktiviert <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),
        "enabled_name": (
            "<b>Die Uhr wurde erfolgreich auf den Nickname gesetzt <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),
        "name_not_enabled": (
            "<b>Die Uhr ist nicht auf den Spitznamen<emoji document_id=5215273032553078755>❎</emoji></b> eingestellt"
        ),
        "disabled_name": (
            "<b>Nickzeit wurde erfolgreich deaktiviert <emoji document_id=5212932275376759608>✅</emoji></b>"
        ),  
        "_cfg_time": "Benutze die Zeitzone 1, -1, -3 usw.",
    }

    def __init__(self):
        self.bio_enabled = False
        self.name_enabled = False
        self.raw_bio = None
        self.raw_name = None
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "timezone",
                "+5",
                lambda: self.strings("_cfg_time"),
            ),
        )

    async def client_ready(self, client, db):
        self.client = client
        self._me = await client.get_me()
 
    @loader.command(ru_doc="""Что-бы указать таймзону через конфиг""")
    async def cfautoprofcmd(self, message):
        """To specify the timezone via the config"""
        name = self.strings("name")
        await self.allmodules.commands["config"](
        await utils.answer(message, 
             f"{self.get_prefix()}config {name}")
             ) 

    @loader.command(ru_doc="""Автоматически изменяет биографию вашей учетной записи с учетом текущего времени, использования: .autobio 'сообщение, время как {time}'""")
    async def autobiocmd(self, message):
        """Automatically changes your account's bio with current time, usage:
        .autobio 'message, time as {time}'"""

        msg = utils.get_args(message)
        if len(msg) != 1:
            return await utils.answer(message, self.strings("invalid_args", message))
        raw_bio = msg[0]
        if "{time}" not in raw_bio:
            return await utils.answer(message, self.strings("missing_time", message))

        
        self.bio_enabled = True
        self.raw_bio = raw_bio
        await self.allmodules.log("start_autobio")
        await utils.answer(message, self.strings("enabled_bio", message))

        while self.bio_enabled:
            offset = datetime.timedelta(hours=self.config["timezone"])
            tz = datetime.timezone(offset)
            time1 = datetime.datetime.now(tz)
            current_time = time1.strftime("%H:%M")
            bio = raw_bio.format(time=current_time)
            await self.client(functions.account.UpdateProfileRequest(about=bio))
            await asyncio.sleep(60)

    @loader.command(ru_doc="""Что-бы остановить время в био введи .stopautobio""")
    async def stopautobiocmd(self, message):
        """Stop autobio cmd."""

        if self.bio_enabled is False:
            return await utils.answer(message, self.strings("bio_not_enabled", message))
        self.bio_enabled = False
        
        await self.allmodules.log("stop_autobio")
        await utils.answer(message, self.strings("disabled_bio", message))
        await self.client(
            functions.account.UpdateProfileRequest(about=self.raw_bio.format(time=""))
        )
    
    @loader.command(ru_doc="""Автоматически изменяет имя вашей учетной записи с учетом текущего времени, использования: .autoname 'сообщение, время как {time}'""")
    async def autonamecmd(self, message):
        """Automatically changes your Telegram name with current time, usage:
        .autoname '<message, time as {time}>'"""

        msg = utils.get_args(message)
        if len(msg) != 1:
            return await utils.answer(message, self.strings("invalid_args", message))
        raw_name = msg[0]
        if "{time}" not in raw_name:
            return await utils.answer(message, self.strings("missing_time", message))

        self.name_enabled = True
        self.raw_name = raw_name
        await self.allmodules.log("start_autoname")
        await utils.answer(message, self.strings("enabled_name", message))

        while self.name_enabled:
            offset = datetime.timedelta(hours=self.config["timezone"])
            tz = datetime.timezone(offset)
            time1 = datetime.datetime.now(tz)
            current_time = time1.strftime("%H:%M")
            name = raw_name.format(time=current_time)
            await self.client(functions.account.UpdateProfileRequest(first_name=name))
            await asyncio.sleep(60)

    @loader.command(ru_doc="""Что-бы остановить время в имени учетной записи введи .stopautoname""")
    async def stopautonamecmd(self, message):
        """just write .stopautoname"""
        
        if self.name_enabled is False:
            return await utils.answer(
                message, self.strings("name_not_enabled", message)
            )
        
        self.name_enabled = False
        await self.allmodules.log("stop_autoname")
        await utils.answer(message, self.strings("disabled_name", message))
        await self.client(
            functions.account.UpdateProfileRequest(
                first_name=self.raw_name.format(time="")
            )
        )
    
    @loader.command(ru_docs="""Доки ru/en""")
    async def aguide(self, message):
        "Just guide ru/en"
        args = utils.get_args_raw(message)
        args = args if args in {"en", "ru"} else "en"

        time = "{time}"
        nick = f'<a href="tg://user?id={self._me.id}">{utils.escape_html(get_display_name(self._me))}</a>'
        pref = f"{utils.escape_html(self.get_prefix())}"

        await utils.answer(
            message, 
            f"<emoji document_id=5789581976176430614>💸</emoji> For example:\n\n<emoji document_id=5789667570579672963>💸</emoji> AutoName: <code>{pref}autoname '{nick} | {time}'</code>\n"
            f"<emoji document_id=5789667570579672963>💸</emoji> AutoBio: <code>{pref}autobio 'smth | {time}'</code>\n"
        if args == "en"
        else (
            f"<emoji document_id=5789581976176430614>💸</emoji> Например:\n\n<emoji document_id=5789667570579672963>💸</emoji> Авто Ник: <code>{pref}autoname '{nick} | {time}'</code>\n"
            f"<emoji document_id=5789667570579672963>💸</emoji> Авто Био: <code>{pref}autobio 'что-то | {time}'</code>\n"
        ),
    )
