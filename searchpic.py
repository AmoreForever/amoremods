# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Searchpic.jpg
# meta developer: @amoremods

from .. import loader, utils
from telethon.tl.types import Message

@loader.tds
class SearchPic(loader.Module):

    strings = {"name": "SearchPic"}
            
    @loader.unrestricted
    async def spiccmd(self, message: Message):
    	"""Search picture"""
    	text = utils.get_args_raw(message)
    	await self.inline.form(
            message=message,
            text = f"🎑 Your pic found\n✍ Input argument: {text}",
            reply_markup=[
            [{"text": "Pic here", "url": f"https://yandex.uz/images/touch/search/?text={text}",}],
            [{"text": "Close", "action": "close"}],
               ],
    		**(
    			{"photo": f"https://yandex.uz/images/touch/search/?text={text}"}
    		),
        )
