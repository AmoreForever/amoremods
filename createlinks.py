#           ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#           █▀█ █░▀░█ █▄█ █▀▄ ██▄
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
        "youtube": "🫂 <u><b>YouTube</u> link special for you.</b>\n\n",
        "google": "🫂 <u><b>Google</u> link special for you.</b>\n\n",
        "github": "🫂 <u><b>Github</u> link special for you.</b>\n\n",
        "pornhub": "🫂 <u><b>Pornhub</u> link special for you.</b>\n\n",
        "telegram": "🫂 <u><b>Telegram</u> link special for you.</b>\n\n",
        "4pda": "🫂 <u><b>4pda</u> link special for you.</b>\n\n",
        "input": "<b>🫧 Input word:</b>",
        "link": "🔮 Link"
    }

    strings_ru = {
        "youtube": "🫂 <b>Ссылка на <u>Youtube</u> специально для тебя</b>\n\n",
        "google": "🫂 <b>Ссылка на <u>Google</u> специально для тебя</b>\n\n",
        "github": "🫂 <b>Ссылка на <u>Github</u> специально для тебя</b>\n\n",
        "pornhub": "🫂 <b>Ссылка на <u>Pornhub</u> специально для тебя</b>\n\n",
        "telegram": "🫂 <b>Ссылка на <u>Telegram</u> специально для тебя</b>\n\n",
        "4pda": "🫂 <b>Ссылка на <u>4Pda</u> специально для тебя</b>\n\n",
        "input": "<b>🫧 Введенный запрос:</b>",
        "link": "🔮 Ссылка"
    }


    async def ytcmd(self, message):
        """<text> create YouTube link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"

        await self.inline.form(
                    self.strings("youtube", message) + s,
                    reply_markup=[                        
                        [{"text": self.strings("link"), "url": f"https://m.youtube.com/results?sp=mAEA&search_query={text}"}]
                        
                    ],
                    message=message,
                )
                

    async def gugcmd(self, message):
        """<text> create Google link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"
        
        await self.inline.form(
                    self.strings("google", message) + s,
                    reply_markup=[
                        [{"text": self.strings("link"), "url": f"https://www.google.com/search?q={text}"}]
                    ],
                    message=message,
                )
                
    async def ghcmd(self, message):
        """<text> create Github link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"
        
        await self.inline.form(
                    self.strings("github", message) + s,
                    reply_markup=[
                        [{"text": self.strings("link"), "url": f"https://github.com/search?q={text}"}]
                    ],
                    message=message,
                )
           
    async def phcmd(self, message):
        """<text> create PornHub link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"

        await self.inline.form(
                    self.strings("pornhub", message) + s,
                    reply_markup=[
                        [{"text": self.strings("link"), "url": f"https://rt.pornhub.com/video/search?search={text}"}]
                    ],
                    message=message,
                )
                
    async def tgcmd(self, message):
        """<text> create Telegram link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"
        
        await self.inline.form(
                    self.strings("telegram", message) + s,
                    reply_markup=[
                        [{"text": self.strings("link"), "url": f"tg://search?query={text}"}]
                    ],
                    message=message,
                )
 
    async def pdacmd(self, message):
        """<text> create 4pda link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"

        await self.inline.form(
                    self.strings("4pda", message) + s,
                    reply_markup=[
                        [{"text": self.strings("link"), "url": f"https://4pda.to/forum/index.php?act=search&source=all&forums=316&subforums=1&query={text}"}]
                    ],
                    message=message,
                )             