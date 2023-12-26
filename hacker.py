# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Hacker.jpg
__version__ = (1, 0, 1)


from .. import loader, utils
import requests
from PIL import Image,ImageFont,ImageDraw 
import io
from textwrap import wrap

@loader.tds
class HackerMod(loader.Module):
	"""Create hacker message stickers"""
	strings = {
		'name': 'Hacker',
        'what': 'Reply to text or write text <emoji document_id="5467928559664242360">❗️</emoji>',
        'processing': 'Processing <emoji document_id="6334710044407368265">🚀</emoji>'
		}
                     
	@loader.owner
	async def hackercmd(self, message):
		"""Reply to text or write text"""
		
		ufr = requests.get("https://x0.at/Rv0Q.ttf")
		f = ufr.content

		reply = await message.get_reply_message()
		if args := utils.get_args_raw(message):
			txt = utils.get_args_raw(message)
		elif reply:
			txt = reply.raw_text
		else:
			await message.edit(self.strings('what', message))
			return
		await message.edit(self.strings("processing"))
		pic = requests.get("https://x0.at/ZTis.jpg")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")

		W, H = img.size
		txt = txt.replace("\n", "𓃐")
		text = "\n".join(wrap(txt, 19))
		t = text + "\n"
		t = t.replace("𓃐","\n")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 32, encoding='UTF-8')
		w, h = draw.multiline_textsize(t, font=font)
		imtext = Image.new("RGBA", (w+10, h+10), (255, 250, 250, 1))
		draw = ImageDraw.Draw(imtext)
		draw.multiline_text((10, 10),t,(255, 255, 255),font=font, align='left')
		imtext.thumbnail((339, 181))
		w, h = 339, 181
		img.paste(imtext, (10,10), imtext)
		out = io.BytesIO()
		out.name = "amore.webp"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()
