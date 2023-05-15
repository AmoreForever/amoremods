# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Activity.jpg
# requires: deep_translator

import requests
import deep_translator
from .. import loader, utils


def generate_activity():
    return requests.get("http://api.farkhodovme.tk/activity/en").json()['activity']


class Activity(loader.Module):
    """Generate activity if you're bored"""

    strings = {"name": "Activity", "activity": "⛩ <b>Activity:</b> <code>{}</code>", "lang": "en"}
    strings_ru = {"activity": "⛩ <b>Занятие:</b> <code>{}</code>", "lang": "ru"}
    strings_uz = {"activity": "⛩ <b>Harakat:</b> <code>{}</code>", "lang": "uz"}

    @loader.command(ru_doc="Сгенерировать занятие", uz_doc="Harakat yaratish")
    async def activity(self, message):
        """Generate activity"""
        res = (deep_translator.GoogleTranslator(source="auto", target=self.strings["lang"]).translate(generate_activity()) if self.strings["lang"] != "en" else generate_activity())
        txt = self.strings['activity'].format(res)
        await utils.answer(message, txt)