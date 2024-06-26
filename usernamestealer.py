# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods

# pusechka @saint_players thanks for the idea 

import logging
import requests
from telethon.tl.types import Message
from telethon.tl.functions.channels import CreateChannelRequest, UpdateUsernameRequest
from telethon.tl.types import InputPeerChannel
from .. import loader, utils
from ..inline.types import InlineCall


logger = logging.getLogger(__name__)


@loader.tds
class UserStealer(loader.Module):
    """
    Username tracking module.
    """

    strings = {
        "name": "UsernameChecker",
        "create_channel": "📂 Create channel",
        "user_free": "⚡️ Username @{} is free, quickly take it.",
        "user_busy": "😥 Username @{} is busy. Do you want to enable tracking?",
        "yes": "🛟 Yes",
        "nope": "🧰 No",
        "free_now": "🌟 Username {} is free, do you want to create a channel?",
        "not_args": "🚫 Enter the user for check",
        "status": "🆔 Username @{} is being tracked\n🟢 Status: free",
        "status_busy": "🆔 Username @{} is being tracked\n🟡 Status: busy",
        "none": "❌ No username is being tracked.",
        "done": "🦉 Done, wait till username will be free",
        "created": "🌟 Channel created, go to username @{}",
        "tg_bug": "🐞 Telegram has bugs, if the channel is not created, try to create it manually",
        
        }
    
    strings_ru = {
        "create_channel": "📂 Создать канал",
        "user_free": "⚡️ Юзернейм @{} свободен, быстро забирай его.",
        "user_busy": "😥 Юзернейм @{} занят. Хотите включить отслеживание?",
        "yes": "🛟 Да",
        "nope": "🧰 Нет",
        "free_now": "🌟 Юзернейм {} свободен, хотите создать канал?",
        "not_args": "🚫 Укажи юзернейм для проверки",
        "status": "🆔 Юзернейм @{} отслеживается\n🟢 Статус: свободен",
        "status_busy": "🆔 Юзернейм @{} отслеживается\n🟡 Статус: занят",
        "none": "❌ Ни один юзернейм не отслеживается.",
        "done": "🦉 Готово, жди пока юзернейм освободится",
        "created": "🌟 Канал создан, переходи по юзернейму @{}",
        "tg_bug": "🐞 У телеграма баги, если канал не создан, попробуй создать его вручную",
    }

    @loader.loop(interval=30, autostart=True)
    async def _steal(self):
        user = self.db.get("usernames_to_check", "username")
        if user == "none":
            return
        else:
            r = requests.get(url=f"https://t.me/{user}")
            if (
                r.text.find(
                    'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
                )
                >= 0
            ):
                self._markup = lambda: self.inline.generate_markup(
                    [
                        {"text": self.strings("create_channel"), "callback": self.create_inline, "args": (user,),},
                        {"text": "Отмена", "callback": self.delete, },
                    ]
                )
                await self.inline.bot.send_message(
                    self._client.tg_id,
                    self.strings("user_free").format(user),
                    disable_web_page_preview=True,
                    reply_markup=self._markup()
                )

                self.db.set("usernames_to_check", "username", "none")
            else:
                pass


    @loader.command()
    async def ucheckcmd(self, message: Message):
        """> Enter the user for check (without @)"""
        args = utils.get_args_raw(message)
        r = requests.get(url=f"https://t.me/{args}")

        if args.startswith('@'):
            args = args[1:]

        if not args:
            return await utils.answer(message, self.strings("not_args"))

        if (
            r.text.find(
                'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
            )
            >= 0
        ):
            await self.inline.form(
                text=self.strings("free_now").format(args),
                reply_markup=[
                    [
                        {
                            "text": self.strings("yes"),
                            "callback": self.create,
                            "args": (args,),
                        },
                        {"text": self.strings("nope"), "action": "close"},
                    ],
                ], **{'video': 'https://te.legra.ph/file/a14a9ff4071d079272171.mp4'},
                message=message,
            )

        else:
            await self.inline.form(
                text=self.strings("user_busy").format(args),
                reply_markup=[
                    [
                        {
                            "text": self.strings("yes"),
                            "callback": self.owo,
                            "args": (args,),
                        },
                        {"text": self.strings("nope"), "action": "close"},
                    ],
                ], **{"video": "https://te.legra.ph/file/90fbbd0deabfc5e740eb3.mp4"},
                message=message,
            )

    @loader.command()
    async def myus(self, message: Message):
        """> Check status of the user being tracked"""
        proc = self.db.get("usernames_to_check", "username")
        if proc == 'none':
            await utils.answer(message, self.strings("none"))
        else:
            r = requests.get(url=f"https://t.me/{proc}")
            if (
                r.text.find(
                    'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
                )
                >= 0
            ):
                await utils.answer(message, self.strings("status").format(proc))

            else:
                await utils.answer(message, self.strings("status_busy").format(proc))

    async def owo(self, call: InlineCall, text: str):
        self.db.set("usernames_to_check", "username", text)
        await call.edit(self.strings("done"))

    async def create(self, call: InlineCall, text: str):
        channel = await self.client(
            CreateChannelRequest(f"{text}", f"{text}", megagroup=False)
        )
        channel_id = channel.__dict__["chats"][0].__dict__["id"]
        channel_hash = channel.__dict__["chats"][0].__dict__["access_hash"]
        try:
            await self.client(
                UpdateUsernameRequest(
                    InputPeerChannel(channel_id=channel_id,
                                     access_hash=channel_hash),
                    text,
                )
            )
            await call.edit(self.strings("created").format(text))
        except:
            await call.edit(
                self.strings("tg_bug"),
            )
            await self.client.delete_dialog(channel_id)
    
    async def create_inline(self, call: InlineCall, text: str):
        channel = await self.client(
            CreateChannelRequest(f"{text}", f"{text}", megagroup=False)
        )
        channel_id = channel.__dict__["chats"][0].__dict__["id"]
        channel_hash = channel.__dict__["chats"][0].__dict__["access_hash"]
        try:
            await self.client(
                UpdateUsernameRequest(
                    InputPeerChannel(channel_id=channel_id,
                                     access_hash=channel_hash),
                    text,
                )
            )
            await call.answer(self.strings("created").format(text))
            await call.delete()
        except:
            await call.answer(
                self.strings("tg_bug"),
                show_alert=True
            )
            await self.client.delete_dialog(channel_id)
            await call.delete()

    async def delete(self, call: InlineCall):
        await call.delete()
        