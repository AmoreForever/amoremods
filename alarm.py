# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru


# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Alarm.jpg

import re
import pytz
import random
import logging
import asyncio
from datetime import datetime

from .. import utils, loader

logger = logging.getLogger(__name__)

day_to_weekday = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
    "пн": 0,
    "вт": 1,
    "ср": 2,
    "чт": 3,
    "пт": 4,
    "сб": 5,
    "вс": 6,
}


@loader.tds
class AlarmMod(loader.Module):
    """Alarm module for remind you about something"""

    strings = {
        "name": "Alarm",
        "set": "<emoji document_id=5870729937215819584>⏰</emoji> <b>Alarm set for <code>{}</code>!</b>",
        "unset": "<emoji document_id=5213107179329953547>⏰</emoji> <b>Alarm for <code>{}</code> unset!</b>",
        "unset_all": "<emoji document_id=5213107179329953547>⏰</emoji> <b>All alarms unset!</b>",
        "list_item": (
            "<emoji document_id=6334603778326529773>⏰</emoji> <b>Alarm for <code>{}</code>!</b> <code>#{}</code>"
            "\n<emoji document_id=6334699757960693635>🕔</emoji> <b>Time:</b> <code>{}</code>"
            "\n<emoji document_id=6334388660594542334>🔊</emoji> <b>Message:</b> <code>{}</code>"
        ),
        "no_alarms": "<emoji document_id=5208549407280078951>🙅‍♂️</emoji> <b>No alarms!</b>",
        "off_button": "✋ Off",
        "notification": "⏰ <b>Alarm!</b>\n\n<code>{}</code>",
        "turned_off": "✔️ <b>Alarm turned off!</b>",
        "incorrect_time": "<emoji document_id=5371015453013450536>🖕</emoji> <b>Incorrect time!</b>",
        "where_args": "<emoji document_id=5371015453013450536>🖕</emoji> <b>Where arguments?</b>",
        "incorrect_args": "<emoji document_id=5371015453013450536>🖕</emoji> <b>Incorrect arguments! Write like this:</b> <code>.setalarm mon 12:00 text</code>",
        "interval_doc": "Interval of sending notifications in seconds",
        "time_zone_doc": "Time zone for alarms (for example, Europe/Moscow)",
    }
    strings_ru = {
        "set": "<emoji document_id=5870729937215819584>⏰</emoji> <b>Напоминание установлено на <code>{}</code>!</b>",
        "unset": "<emoji document_id=5213107179329953547>⏰</emoji> <b>Напоминание для <code>{}</code> отменено!</b>",
        "unset_all": "<emoji document_id=5213107179329953547>⏰</emoji> <b>Все напоминания отменены!</b>",
        "list_item": (
            "<emoji document_id=6334603778326529773>⏰</emoji> <b>Напоминание для <code>{}</code>!</b> <code>#{}</code>"
            "\n<emoji document_id=6334699757960693635>🕔</emoji> <b>Время:</b> <code>{}</code>"
            "\n<emoji document_id=6334388660594542334>🔊</emoji> <b>Сообщение:</b> <code>{}</code>"
        ),
        "no_alarms": "<emoji document_id=5208549407280078951>🙅‍♂️</emoji> <b>Нет напоминаний!</b>",
        "off_button": "✋ Выключить",
        "notification": "⏰ <b>Напоминание!</b>\n\n<code>{}</code>",
        "turned_off": "✔️ <b>Напоминание выключено!</b>",
        "incorrect_time": "<emoji document_id=5371015453013450536>🖕</emoji> <b>Неправильное время!</b>",
        "where_args": "<emoji document_id=5371015453013450536>🖕</emoji> <b>Где аргументы?</b>",
        "incorrect_args": "<emoji document_id=5371015453013450536>🖕</emoji> <b>Неправильные аргументы! Пиши так:</b> <code>.setalarm пн 12:00 текст</code>",
        "interval_doc": "Интервал отправления напоминаний в секундах",
        "time_zone_doc": "Часовой пояс для напоминаний (например, Europe/Moscow)",
    }
    
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "interval",
                5,
                lambda: self.strings("interval_doc"),
                validator=loader.validators.Integer(minimum=1, maximum=60),
            ),
            loader.ConfigValue(
                "time_zone",
                "Europe/Moscow",
                lambda: self.strings("time_zone_doc"),
                validator=loader.validators.RegExp(
                    r"^[\w/]+$",
                )
                ),
        )
    @loader.command(ru_doc="<день недели> <время> <сообщение> - установить напоминание")
    async def setalarm(self, message):
        """<day of the week> <time> <message> - set alarm"""

        args = utils.get_args_raw(message)
        if not args:
            return await utils.answer(message, self.strings("where_args"))
        try:
            re_args = re.match(r"^(.+) (\d{1,2}):(\d{1,2}) (.*)$", args)
            day = re_args.group(1).lower()
            hour = int(re_args.group(2))
            minute = int(re_args.group(3))
            text = re_args.group(4)
        except AttributeError:
            return await utils.answer(message, self.strings("incorrect_args"))
    
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            return await utils.answer(message, self.strings("incorrect_time"))
        if day not in day_to_weekday.keys():
            text = f"<b>Wrong day of the week!</b>\n<b>Available days:</b> <code>{', '.join(day_to_weekday.keys())}</code>"
            return await utils.answer(message, text)

        id_ = random.randint(100, 999)
        self.set(
            "alarms",
            {
                **self.get("alarms", {}),
                day: {
                    "hour": hour,
                    "minute": minute,
                    "text": text,
                    "id": id_,
                    "status": "on",
                },
            },
        )
        await utils.answer(message, self.strings("set").format(day))

    @loader.command(ru_doc="получить список напоминаний")
    async def alarms(self, message):
        """get alarms list"""

        alarms = self.get("alarms", {})
        if not alarms:
            return await utils.answer(message, self.strings("no_alarms"))

        text = ""
        for day, alarm in alarms.items():
            text += self.strings("list_item").format(
                day,
                f"{alarm['id']}",
                f"{alarm['hour']}:{alarm['minute']}",
                alarm["text"],
            )
            text += "\n\n"
        await utils.answer(message, text)

    @loader.command(ru_doc="<id> - отменить напоминание")
    async def unsetalarm(self, message):
        """<id> - unset alarm"""

        args = utils.get_args_raw(message)
        if not args:
            return await utils.answer(message, self.strings("where_time"))
        if args.startswith("#"):
            args = args[1:]

        alarms = self.get("alarms", {})
        for day, alarm in alarms.items():
            if str(alarm["id"]) == args:
                alarms.pop(day)
                self.set("alarms", alarms)
                return await utils.answer(
                    message, self.strings("unset").format(day)
                )
        await utils.answer(message, self.strings("unset").format(args))

    @loader.command(ru_doc="отменить все напоминания")
    async def unsetallalarms(self, message):
        """unset all alarms"""

        self.set("alarms", {})
        await utils.answer(message, self.strings("unset_all"))

    @loader.loop(interval=2, autostart=True)
    async def check_alarms(self):
        alarms = self.get("alarms", {})
        if not alarms:
            return
        now = datetime.now(tz=pytz.timezone(self.config["time_zone"]))
        day = now.weekday()
        hour = now.hour
        minute = now.minute
        for day_, alarm in alarms.items():
            if (
                day_to_weekday[day_] == day
                and alarm["hour"] == hour
                and alarm["minute"] == minute
            ):
                while alarm["status"] == "on":
                    self._markup = self.inline.generate_markup(
                        {
                            "text": self.strings("off_button"),
                            "callback": self.off_alarm,
                            "args": (alarm["id"],),
                        }
                    )
                    await self.inline.bot.send_message(
                        self.tg_id,
                        self.strings("notification").format(alarm["text"]),
                        reply_markup=self._markup,
                    )
                    await asyncio.sleep(self.config["interval"])
                break

    async def off_alarm(self, call, id_):
        alarms = self.get("alarms", {})
        for day, alarm in alarms.items():
            if alarm["id"] == id_:
                alarm["status"] = "off"
                self.set("alarms", alarms)
                await call.edit(self.strings("turned_off"))
                return False
        await call.answer("Не найдено!")