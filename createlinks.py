#▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#█▀█ █░▀░█ █▄█ █▀▄ ██▄
#          
# © Copyright 2022
#
# https://t.me/the_farkhodov 
#
# meta developer: @amoremods 


from .. import loader, utils, main, security



@loader.tds
class AmorelinksMod(loader.Module):
    """Create links"""

    strings = {
        "name": "AmoreLinks",
        "youtube": "🫂 <b>YouTube link special for you.</b>\n\n",
        "google": "🫂 <b>Google link special for you.</b>\n\n",
        "github": "🫂 <b>Github link special for you.</b>\n\n",
        "pornhub": "🫂 <b>Pornhub link special for you.</b>\n\n",
    }

    async def ytcmd(self, message):
        """<text> create YouTube link"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Input word: <code>{text}</code></b>"
        if await self.allmodules.check_security(
            message,
            security.OWNER | security.SUDO,
        ):
            
            try:
                await self.inline.form(
                    self.strings("youtube", message) + s,
                    reply_markup=[                        
                        [{"text": "♨️ Link", "url": f"https://m.youtube.com/results?sp=mAEA&search_query={text}"}],
                        [{"text": "🔻 Close", "action": f"close"}],
                        
                    ],
                    message=message,
                )
            except Exception:
                await utils.answer(message, self.strings("join", message))
                

    async def gugcmd(self, message):
        """<text> create Google link"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Input word: <code>{text}</code></b>"
        if await self.allmodules.check_security(
            message,
            security.OWNER | security.SUDO,
        ):
            
            try:
                await self.inline.form(
                    self.strings("google", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Link", "url": f"https://www.google.com/search?q={text}"}],
                        [{"text": "🔻 Close", "action": f"close"}],
                    ],
                    message=message,
                )
            except Exception:
                await utils.answer(message, self.strings("join", message))
                
    async def ghcmd(self, message):
        """<text> create Github link"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Input word: <code>{text}</code></b>"
        if await self.allmodules.check_security(
            message,
            security.OWNER | security.SUDO,
        ):
            
            try:
                await self.inline.form(
                    self.strings("github", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Link", "url": f"https://github.com/search?q={text}"}],
                        [{"text": "🔻 Close", "action": f"close"}],
                    ],
                    message=message,
                )
            except Exception:
                await utils.answer(message, self.strings("join", message))
           
    async def phcmd(self, message):
        """<text> create PornHub link"""
        text = utils.get_args_raw(message) 
        s = f"<b>✏ Input word: <code>{text}</code></b>"
        if await self.allmodules.check_security(
            message,
            security.OWNER | security.SUDO,
        ):
            
            try:
                await self.inline.form(
                    self.strings("pornhub", message) + s,
                    reply_markup=[
                        [{"text": "🛰 Link", "url": f"https://rt.pornhub.com/video/search?search={text}"}],
                        [{"text": "🔻 Close", "action": f"close"}],
                    ],
                    message=message,
                )
            except Exception:
                await utils.answer(message, self.strings("join", message))
                
