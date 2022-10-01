# ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
# █▀█ █░▀░█ █▄█ █▀▄ ██▄
#
#             © Copyright 2022
#
#          https://t.me/the_farkhodov
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://te.legra.ph/file/388e1b26a46a8c439e479.png
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Createlinks.jpg
# meta developer: @amoremods
 
from .. import loader, utils

@loader.tds
class AmorelinksMod(loader.Module):
    """Create links"""

    strings = {
        "name": "AmoreLinks",
        "youtube": "🫂 <b>YouTube link special for you.</b>\n\n",
        "google": "🫂 <b>Google link special for you.</b>\n\n",
        "github": "🫂 <b>Github link special for you.</b>\n\n",
        "pornhub": "🫂 <b>Pornhub link special for you.</b>\n\n",
        "telegram": "🫂 <b>Telegram link special for you.</b>\n\n",
        "4pda": "🫂 <b>4pda link special for you.</b>\n\n",
    }

    strings_ru = {
        "youtube": "🫂 <b>Ссылка на Youtube специально для тебя</b>\n\n",
        "google": "🫂 <b>Ссылка на Google специально для тебя</b>\n\n",
        "github": "🫂 <b>Ссылка на Github специально для тебя</b>\n\n",
        "pornhub": "🫂 <b>Ссылка на Pornhub специально для тебя</b>\n\n",
        "telegram": "🫂 <b>Ссылка на Telegram специально для тебя</b>\n\n",
        "4pda": "🫂 <b>Ссылка на 4Pda специально для тебя</b>\n\n",
    }


    async def ytcmd(self, message):
        """<text> create YouTube link"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Input word: <code>{text}</code></b>"

        await self.inline.form(
                    self.strings("youtube", message) + s,
                    reply_markup=[                        
                        [{"text": "♨️ Link", "url": f"https://m.youtube.com/results?sp=mAEA&search_query={text}"}],
                        [{"text": "🔻 Close", "action": f"close"}],
                        
                    ],
                    message=message,
                )
                

    async def gugcmd(self, message):
        """<text> create Google link"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Input word: <code>{text}</code></b>"
        
        await self.inline.form(
                    self.strings("google", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Link", "url": f"https://www.google.com/search?q={text}"}],
                        [{"text": "🔻 Close", "action": f"close"}],
                    ],
                    message=message,
                )
                
    async def ghcmd(self, message):
        """<text> create Github link"""
        text = utils.get_args_raw(message) 
        s = s = f"<b>✏ Input word: <code>{text}</code></b>"
        
        await self.inline.form(
                    self.strings("github", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Link", "url": f"https://github.com/search?q={text}"}],
                        [{"text": "🔻 Close", "action": f"close"}],
                    ],
                    message=message,
                )
           
    async def phcmd(self, message):
        """<text> create PornHub link"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Input word: <code>{text}</code></b>"

        await self.inline.form(
                    self.strings("pornhub", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Link", "url": f"https://rt.pornhub.com/video/search?search={text}"}],
                        [{"text": "🔻 Close", "action": f"close"}],
                    ],
                    message=message,
                )
                
    async def tgcmd(self, message):
        """<text> create Telegram link"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Input word: <code>{text}</code></b>"
        
        await self.inline.form(
                    self.strings("telegram", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Link", "url": f"tg://search?query={text}"}],
                        [{"text": "🔻 Close", "action": f"close"}],
                    ],
                    message=message,
                )
 
    async def pdacmd(self, message):
        """<text> create 4pda link"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Input word: <code>{text}</code></b>"

        await self.inline.form(
                    self.strings("4pda", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Link", "url": f"https://4pda.to/forum/index.php?act=search&source=all&forums=316&subforums=1&query={text}"}],
                        [{"text": "🔻 Close", "action": f"close"}],
                    ],
                    message=message,
                )             
