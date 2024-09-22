# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru


# required: aiohttp
# meta banner: https://github.com/AmoreForever/shizuassets/blob/master/wakatime.jpg?raw=true

# meta developer: @hikamorumods

import asyncio
import aiohttp

from .. import utils, loader


@loader.tds
class Wakatime(loader.Module):
    """Show your Wakatime stats"""

    strings = {
        "name": "Wakatime",
        "set_waka": "Set your Wakatime token",
        "no_token": "🚫 <b>You don't have a token</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "WAKATIME_TOKEN",
            None,
            lambda: self.strings["set_waka"],
        )

    @loader.command()
    async def waka(self, message):
        """See your stat"""
        token = self.config["WAKATIME_TOKEN"]

        if token is None:
            return await utils.answer(message, self.strings("no_token"))

        async with aiohttp.ClientSession() as session:
            endpoints = [
                "status_bar/today",
                "stats/all_time",
                "stats/all_time",
                "all_time_since_today",
            ]
            tasks = [
                session.get(
                    f"https://wakatime.com/api/v1/users/current/{endpoint}?api_key={token}"
                )
                for endpoint in endpoints
            ]
            responses = await asyncio.gather(*tasks)
            results = await asyncio.gather(*[response.json() for response in responses])

            result_t, result, result_s, result_w = results

            all_time = result_w["data"]["text"]
            username = result["data"]["username"]
            languages = result["data"]["languages"]
            today = result_t["data"]["categories"]
            os = result["data"]["operating_systems"]
            editor = result["data"]["editors"]

            OS = ", ".join(f"<code>{stat['name']}</code>" for stat in os if stat["text"] != "0 secs")
            EDITOR = ", ".join(f"<code>{stat['name']}</code>" for stat in editor if stat["text"] != "0 secs")
            LANG = "\n".join(f"▫️ <b>{stat['name']}</b>: <i>{stat['text']}</i>" for stat in languages if stat["text"] != "0 secs")
            TODAY = "\n".join(stat["text"] for stat in today if stat["text"] != "0 secs")
            
            await utils.answer(
                message,
                f"👤 <b>Username:</b> <code>{username}</code>\n🖥 <b>OS:</b> {OS}\n🌀 <b>Editor:</b> {EDITOR}\n⏳ <b>All time</b>: <code>{all_time}</code>\n💼 <b>Today</b>: <code>{TODAY}</code>\n\n🧬 LANGUAGES\n\n{LANG}\n",
                reply_markup=[
                    [
                        {
                            "text": "🔄 Update",
                            "callback": self.update_waka,
                        }
                    ]
                ],
            )

    async def update_waka(self, call):
        await call.edit("🔄 <b>Updating...</b>")
        token = self.config["WAKATIME_TOKEN"]
        if token is None:
            return await call.edit(self.strings("no_token"))

        async with aiohttp.ClientSession() as session:
            endpoints = [
                "status_bar/today",
                "stats/all_time",
                "stats/all_time",
                "all_time_since_today",
            ]
            tasks = [
                session.get(
                    f"https://wakatime.com/api/v1/users/current/{endpoint}?api_key={token}"
                )
                for endpoint in endpoints
            ]
            responses = await asyncio.gather(*tasks)
            results = await asyncio.gather(*[response.json() for response in responses])

            result_t, result, result_s, result_w = results

            all_time = result_w["data"]["text"]
            username = result["data"]["username"]
            languages = result["data"]["languages"]
            today = result_t["data"]["categories"]
            os = result["data"]["operating_systems"]
            editor = result["data"]["editors"]

            OS = ", ".join(f"<code>{stat['name']}</code>" for stat in os if stat["text"] != "0 secs")
            EDITOR = ", ".join(f"<code>{stat['name']}</code>" for stat in editor if stat["text"] != "0 secs")
            LANG = "\n".join(f"▫️ <b>{stat['name']}</b>: <i>{stat['text']}</i>" for stat in languages if stat["text"] != "0 secs")
            TODAY = "\n".join(stat["text"] for stat in today if stat["text"] != "0 secs")
            
            await call.edit(
                f"👤 <b>Username:</b> <code>{username}</code>\n🖥 <b>OS:</b> {OS}\n🌀 <b>Editor:</b> {EDITOR}\n⏳ <b>All time</b>: <code>{all_time}</code>\n💼 <b>Today</b>: <code>{TODAY}</code>\n\n🧬 LANGUAGES\n\n{LANG}\n",
                reply_markup=[
                    [
                        {
                            "text": "🔄 Update",
                            "callback": self.update_waka,
                        }
                    ]
                ],
            )
