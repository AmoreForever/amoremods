# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/phstiker.jpg
# requires: phlogo

import os
from .. import loader, utils
from phlogo import generate
 
@loader.tds
class PhLogo(loader.Module):
    """Make Pornhub logo sticker"""
    
    strings = {
		"name": "Phlogo",
        "only_two": "Something's wrong. Try giving two words only like `Hello world`",
        "none_args": "Give some text bruh, e.g.: `Hello world`"
	}
    
    strings_ru = {
        "only_two": "Что-то не так. Попробуйте указать только два аргумента, например «Hello world».",
        "none_args": "Дай какой-нибудь текст, например: `Hello world`."
    }
    
    strings_uz = {
        "only_two": "Xatolik bor. `Hello world` kabi faqat ikkita matn keltirishga harakat qiling.",
        "none_args": "Bir oz matn bering, masalan: `Salom dunyo`."
    }
    
    @loader.command()
    async def phl(self, message):
        "Makes PHub style logo sticker."
        args = utils.get_args_raw(message).split(' ')
        reply = await message.get_reply_message()
        if args == " ":
            await utils.answer(message, self.strings('none_args'))
            return
        try:
            p = args[0]
            h = args[1]
        except:
            await utils.answer(message, self.strings('only_two'))
            return
        result = generate(f"{p}",f"{h}")
        result.save("ph.webp")
        path = os.getcwd()
        stc = f"{path}/ph.webp"
        await message.delete()
        await self._client.send_file(
            message.peer_id,
            stc,
            caption=f"{p} {h}",
            link_preview=False,
            reply_to=reply.id if reply else None,
        )
        os.remove(stc)
