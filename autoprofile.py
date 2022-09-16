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

#           ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#           █▀█ █░▀░█ █▄█ █▀▄ ██▄
#
#            © Copyright 2022
#
#          https://t.me/the_farkhodov
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: FTG & @amoremods
# meta banner: https://te.legra.ph/file/ab60f2b5ca190422cd9bd.jpg


import asyncio
import time
import datetime

from telethon.tl import functions

from .. import loader, utils


@loader.tds
class AutoProfileMod(loader.Module):
    """Automatic stuff for your profile :P"""

    strings = {
        "name": "AutoProfile",
        "invalid_args": "<b>Missing parameters, please read the docs❗️</b>",
        "missing_time": "<b>Time was not specified in bio❗️</b>",
        "enabled_bio": "<b>Enabled bio clock ✅</b>",
        "bio_not_enabled": "<b>Bio clock is not enabled❗️</b>",
        "disabled_bio": "<b>Disabled bio clock ✅</b>",
        "enabled_name": "<b>Enabled name clock ✅</b>",
        "name_not_enabled": "<b>Name clock is not enabled❗️</b>",
        "disabled_name": "<b>Name clock disabled ✅</b>",
        "_cfg_time": "Use timezone 1, -1, -3 etc.",
    }

    strings_ru = {
        "invalid_args": "<b>Не правильные аргуметы, прочитай доки❗️</b>",
        "missing_time": "<b>Время не было установлено в био❗️</b>",
        "enabled_bio": "<b>Био часы успешно установлены ✅</b>",
        "bio_not_enabled": "<b>Часы не установлено в био❗️</b>",
        "disabled_bio": "<b>Время в био успешно отключен ✅</b>",
        "enabled_name": "<b>Часы в ник успешно установлены ✅</b>",
        "name_not_enabled": "<b>Часы не установлены в ник❗️</b>",
        "disabled_name": "<b>Время в нике успешно отключен ✅</b>",
        "_cfg_time": "Используй таймзону 1, -1, -3 и тд.",
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