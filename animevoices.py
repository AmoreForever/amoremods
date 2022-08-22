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
# scope: hikka_min 1.3.3
# meta developer: @amoremods
# meta banner: https://te.legra.ph/file/f8b57640aa11207eabd5a.jpg

from .. import loader


@loader.tds  
class AnimeVoicesMod(loader.Module): 
 """🎤 Popular Anime Voices""" 
  
 strings = {"name": "AnimeVoices"} 
   
   
 async def smexkcmd(self, message): 
  """Смех Канеки""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/25", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def smexycmd(self, message): 
  """Смех Ягами""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/26", voice_note=True, reply_to=reply.id if reply else None) 
  return 
   
 async def znaycmd(self, message): 
  """Знай свое место ничтожество""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/27", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def madaracmd(self, message): 
  """Учиха Мадара""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/28", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def sharingancmd(self, message): 
  """Итачи Шаринган""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/29", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def imsasukecmd(self, message): 
  """Учиха Саске""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/30", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def paincmd(self, message): 
  """Познайте боль""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/74", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def rascmd(self, message): 
  """Расширение территории""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/81", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def tenseicmd(self, message): 
  """Shinra tensei""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/82", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def dazaicmd(self, message): 
  """Дазаи""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/83", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def gaycmd(self, message): 
  """I'm gay""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/84", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def bankaicmd(self, message): 
  """Bankai""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/85", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def satecmd(self, message): 
  """Sate sate sate""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/86", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def yoaimocmd(self, message): 
  """Yoaimo""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/87", voice_note=True, reply_to=reply.id if reply else None) 
  return
