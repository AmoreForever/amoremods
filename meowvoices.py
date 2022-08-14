#▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#█▀█ █░▀░█ █▄█ █▀▄ ██▄
#          
#             © Copyright 2022
#
#          https://t.me/the_farkhodov 
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
#meta developer: @the_farkhodov
# scope: inline 


import logging
from .. import loader

logger = logging.getLogger(__name__)


@loader.tds
class CuteVoices(loader.Module):
    """
    🥷 Top 9 cute meow voices

    📚 Documentation: ...
    📝 Dev: @sngscamer 
    📥 Source: ...
    📦 Version: 1.0.1
    """

    strings = {
        "name": "Cute meow voices", "main":  "<i><b>◍ Cute meow voices you can found in <a href='https://t.me/hikka_neko/'>Hikka nekoboys</a></b></i>", }
    
    
    @loader.group_member
    async def cutelistcmd(self, message):
        """Cute voices"""
        await self.inline.form(
            self.strings("main"),
            reply_markup=[
                [{"text": "😻 More modules", "url": "https://t.me/Amoremods"}],               
                [
                    {"text": " ◍ Hikariatama", "callback": self.hikari},
                    {"text": "◍ Vsecoder", "callback": self.vsecod},
                    {"text": "◍ Skillz", "callback": self.skillz},
                ],
                [
                    {"text": "◍ Morisummer", "callback": self.mori},
                    {"text": "◍ Lite", "callback": self.lite},
                    {"text": "◍ Codercoffee", "callback": self.coffee},
                ],
                [
                    {"text": "◍ Len4iks", "callback": self.len},
                    {"text": "◍ Shadow hikka", "callback": self.shadow},
                    {"text": "◍ Amorelico", "callback": self.amore},                    
                ],
                [{"text": "😌 Close", "action": "close"}],
            ],
            gif="https://t.me/gifki_anime/14351",
            message=message,
        )

    async def hikari(self, *_):
        await self.client.send_message(
            self.chat_id,
            file="https://t.me/hikka_neko/4",
        )

    async def vsecod(self, *_):
        await self.client.send_message(
            self.chat_id,
            file="https://t.me/hikka_neko/6",
        )

    async def skillz(self, *_):
        await self.client.send_message(
            self.chat_id, 
           file="https://t.me/hikka_neko/14",
        )

    async def mori(self, *_):
        await self.client.send_message(
            self.chat_id,
            file="https://t.me/hikka_neko/12",
        )

    async def lite(self, *_):
        await self.client.send_message(
            self.chat_id,
            file="https://t.me/hikka_neko/104",
        )

    async def coffee(self, *_):
        await self.client.send_message(
            self.chat_id,
            file="https://t.me/hikka_neko/95",
        )

    async def len(self, *_):
        await self.client.send_message(
            self.chat_id,
            file="https://t.me/hikka_neko/80",
        )

    async def shadow(self, *_):
        await self.client.send_message(
            self.chat_id,
            file="https://t.me/hikka_neko/75",
        )

    async def amore(self, *_):
        await self.client.send_message(
            self.chat_id,
            file="https://t.me/hikka_neko/63",
        )
