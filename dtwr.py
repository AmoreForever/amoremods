# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/DTWR.jpg

from .. import loader, utils
from telethon.tl.types import Message


@loader.tds
class DTWRMod(loader.Module):
    """Module Don't tag wihout reason"""

    strings = {
        "name": "DTWR",
        "text": "Your custom text",
        "username": "Input you username without '@'",
    }

    strings_ru = {
        "text": "Кастомный текст",
        "username": "Введи свой юзернэйм без '@'",
    }

    strings_uz = {
        "text": "Kastom text",
        "username": "Usernameingizni kiriting, '@' siz"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "Username",
                "username",
                doc=lambda: self.strings("username"),
            ),
            loader.ConfigValue(
                "custom_text",
                "😫 Please don't tag me without reason",
                doc=lambda: self.strings("text"),
            ),
        )

    @loader.command(ru_docs="Конфиг этого модуля")
    async def cfgdtwrcmd(self, message):
        """This module config"""
        name = self.strings("name")
        await self.allmodules.commands["config"](
            await utils.answer(message, f"{self.get_prefix()}config {name}")
        )

    @loader.tag("only_messages", "only_groups", "in")
    async def watcher(self, message: Message):

        reply = await message.get_reply_message()

        tag = self.config['Username']
        if tag.startswith('@') is False:
            tag = f"@{tag}"

        if reply:
            return False
        if message.text.lower() == tag:
            await message.reply(self.config["custom_text"])
            await self._client.send_read_acknowledge(
                message.chat_id,
                clear_mentions=True,
            )
