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
        "input": "<b><emoji document_id=5787196143318339389>✍️</emoji> Input word:</b>",
    }


    async def ytcmd(self, message):
        """<text> create YouTube link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"

        await utils.answer(
        message,
        f"{s}\n"
        f"<emoji document_id=5463206079913533096>📹</emoji><a href='https://m.youtube.com/results?sp=mAEA&search_query={text}'> Watch on Youtube</a>"
    )

    async def gugcmd(self, message):
        """<text> create Google link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"

        await utils.answer(
        message,
        f"{s}\n"
        f"<emoji document_id=5463409240456567767>🕸</emoji><a href='https://www.google.com/search?q={text}'> See on Google</a>"
    )
                
    async def ghcmd(self, message):
        """<text> create Github link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"
        
        await utils.answer(
        message,
        f"{s}\n"
        f"<emoji document_id=5465637267626271756>💻</emoji><a href='https://github.com/search?q={text}'> See on GitHub</a>"
    )
        
           
    async def phcmd(self, message):
        """<text> create PornHub link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"

        await utils.answer(
        message,
        f"{s}\n"
        f"<emoji document_id=5285214543448907623>🍓</emoji><a href='https://rt.pornhub.com/video/search?search={text}'> Watch on PornHub</a>"
    )
                
    async def tgcmd(self, message):
        """<text> create Telegram link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"
        
        await utils.answer(
        message,
        f"{s}\n"
        f"<emoji document_id=5465204283383224325>💬</emoji><a href='tg://search?query={text}'> Search on Telegram</a>"
    )
 
    async def pdacmd(self, message):
        """<text> create 4pda link"""
        text = utils.get_args_raw(message) 
        s = self.strings("input") + f" <code>{text}</code>"

        await utils.answer(
        message,
        f"{s}\n"
        f"<emoji document_id=5783082376397590030>📱</emoji><a href='https://4pda.to/forum/index.php?act=search&source=all&forums=316&subforums=1&query={text}'> See on GitHub</a>"
    )            