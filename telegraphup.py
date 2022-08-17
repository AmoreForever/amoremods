#        ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#        █▀█ █░▀░█ █▄█ █▀▄ ██▄
#
#                 © Copyright 2022
#
#          https://t.me/the_farkhodov
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.3.0
# meta developer: @amoremods
# meta banner: https://imgur.com/cmteax3

from .. import loader, utils
import asyncio
import requests
from telethon.tl.types import DocumentAttributeFilename


@loader.tds
class TelegraphUPMod(loader.Module):
 """Upload video/photo and gif to telegraph"""
	
	
	strings = {
           "name": "TelegraphUP",
           "here": "✨ Your file here",
           "mods": "🦓 More modules here",
           "pls_reply": "⚠️ Reply to photo or video/gif",
        }
	       
	@loader.sudo
	async def thupcmd(self, message):
			"""<reply photo or video>"""
			if message.is_reply:
				reply_message = await message.get_reply_message()
				data = await check_media(reply_message)
				if isinstance(data, bool):
					await message.edit(self.strings("pls_reply"))
					return
			else:
				await message.edit(self.strings("pls_reply"))
				return
			
				
			file = await message.client.download_media(data, bytes)
			path = requests.post('https://te.legra.ph/upload', files={'file': ('file', file, None)}).json()
			try:
				amore = 'https://te.legra.ph'+path[0]['src']
			except KeyError:
				amore = path["error"]
			await self.inline.form(
                    text=f"🦜 Your file has been successfully uploaded. \n💾 Copy link: 《 <code>{amore}</code> 》",
                    reply_markup=[
                        [{
                  "text": self.strings("here"), 
                  "url": f"{amore}",
                        }],
                     ], **{"photo": f"{amore}"},
                     message=message,
                   )
				
			
    async def check_media(reply_message):
	if reply_message and reply_message.media:
		if reply_message.photo:
			data = reply_message.photo
		elif reply_message.document:
			if DocumentAttributeFilename(file_name='AnimatedSticker.tgs') in reply_message.media.document.attributes:
				return False
			if reply_message.audio or reply_message.voice:
				return False
			data = reply_message.media.document
        else:
			return False
	else:
		return False
	if not data or data is None:
		return False
	else:
		return data
		
		
		
