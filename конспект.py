#     ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#     █▀█ █░▀░█ █▄█ █▀▄ ██▄
#          
#             © Copyright 2022
#
#          https://t.me/the_farkhodov 
#
#🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html


# scope: hikka_only
# scope: hikka_min 1.3.1
# meta developer: @amoremods
# meta banner: https://imgur.com/EzGrs6h


from telethon import events
from .. import utils, loader
import re, asyncio, os

cute = 5475546549
meta = " Made by @amoremods❤"


@loader.tds
class AbstractMod(loader.Module):
	"""Напишет красивый конспект на листке"""
	
	strings = {"name": "Конспект",
                   "developer": "@sngscamer",
                       }
	
	async def client_ready(self, client, db):
		self.db = db
	
	@loader.owner
	async def konspcmd(self, message):
		""" .konsp text"""

		text = utils.get_args_raw(message) 
		async with message.client.conversation(cute) as conv:
			await utils.answer(message, '✍ Пишу конспекст...')
			response = conv.wait_event(events.NewMessage(incoming=True, from_users=cute, chats=cute))
			amore = await message.client.send_message(cute, "📖 Konspekt yozish")
			await utils.answer(message, 'Секунду...')
			amore = await message.client.send_message(cute, text)
			response = await response
			await message.client.send_file(message.to_id, response.media, caption=meta)
			await response.delete()
			amore.delete()
			await message.delete()
			await self.client.delete_dialog(cute)
