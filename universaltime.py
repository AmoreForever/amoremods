#           ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#           █▀█ █░▀░█ █▄█ █▀▄ ██▄
#
#            © Copyright 2022
#
#          https://t.me/the_farkhodov
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @amoremods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Universaltime.jpg
from .. import loader, utils
import datetime
from ..inline.types import InlineCall

import logging

logger = logging.getLogger(__name__)

def check_time():
	jp_time = 9
	ch_time = 9
	mo_time = 8
	ca_time = -8
	us_time = -7
	kgz_time = 6
	uz_time = 5
	ind_time = 5.30
	az_time = 4
	ar_time = -4
	ru_time = 3
	gr_time = 2
	uk_time = 1
	
	offset = datetime.timedelta(hours=ru_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	ru = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=uz_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	uz = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=az_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	az = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=gr_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	gr = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=uk_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	uk = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=us_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	us = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=kgz_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	kgz = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=jp_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	jp = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=ind_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	ind = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=ch_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	ch = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=mo_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	mo = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=ca_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	ca = time1.strftime("%H:%M")    
	mo = time1.strftime("%H:%M")
	offset = datetime.timedelta(hours=ar_time)
	tz = datetime.timezone(offset)
	time1 = datetime.datetime.now(tz)
	ar = time1.strftime("%H:%M")  
	amore = (
			f"<emoji document_id=4920662486778119009>🌐</emoji> <b>Universal time</b>\n\n" 
			f"<emoji document_id=6323139226418284334>🇷🇺</emoji> Russia ➪ {ru}\n"
			f"<emoji document_id=6323430017179059570>🇺🇿</emoji> Uzbekistan ➪ {uz}\n"
			f"<emoji document_id=6323289850921354919>🇺🇦</emoji> Ukraine ➪ {ru}\n"
			f"<emoji document_id=6323575251498174463>🇦🇿</emoji> Azerbaijan ➪ {az}\n"
			f"<emoji document_id=6320817337033295141>🇩🇪</emoji> German ➪ {gr}\n"
			f"<emoji document_id=6323589145717376403>🇬🇧</emoji> UK ➪ {uk}\n"
			f"<emoji document_id=6323602387101550101>🇵🇱</emoji> Poland ➪ {gr}\n"
			f"<emoji document_id=6323374027985389586>🇺🇸</emoji> USA ➪ {us}\n"
			f"<emoji document_id=6323615997852910673>🇰🇬</emoji> Kyrgyzstan ➪ {kgz}\n"
			f"<emoji document_id=6323135275048371614>🇰🇿</emoji> Kazakhstan ➪ {kgz}\n"
			f"<emoji document_id=6323555846835930376>🇮🇶</emoji> Iraq ➪ {ru}\n"
			f"<emoji document_id=6323356796576597627>🇯🇵</emoji> Japan ➪ {jp}\n"
			f"<emoji document_id=6323152716910561397>🇰🇷</emoji> South KR ➪ {jp}\n"
			f"<emoji document_id=6323181871148566277>🇮🇳</emoji> India ➪ {ind}\n"
			f"<emoji document_id=6323570711717742330>🇫🇷</emoji> France ➪ {gr}\n"
			f"<emoji document_id=6323453751168337485>🇨🇳</emoji> China ➪ {ch}\n"
			f"<emoji document_id=6321003171678259486>🇹🇷</emoji> Turkey ➪ {ru}\n"
            f"<emoji document_id=6323602322677040561>🇨🇱</emoji> Mongolia ➪ {mo}\n"
            f"<emoji document_id=6323325327351219831>🇨🇦</emoji> Canada ➪ {ca}\n"
            f"<emoji document_id=6323471399188957082>🇮🇹</emoji> Italia ➪ {uk}\n"
            f"<emoji document_id=6323516260122363644>🇪🇬</emoji> Egypt ➪ {gr}\n"
            f"<emoji document_id=6323236391463421376>🇦🇲</emoji> Armenia ➪ {ar}\n\n"
            f"<emoji document_id=5188216117272780281>🍙</emoji> #whyamore"
	)
	return amore

media = "https://te.legra.ph/file/2ab9b131ceceb9b020583.mp4"

@loader.tds
class UniversalTimeMod(loader.Module):
	"""See the time of other countries"""
	
	strings = {"name": "UnivTime"}

	@loader.command(ru_docs="Смотреть мировое время")
	async def atimecmd(self, message):
		"""See time"""
		kk = check_time()
		await utils.answer(message, kk)

	@loader.command(ru_docs="Смотреть мировое время в инлайн режиме")
	async def atimeicmd(self, message):
		"""See time on inline mode"""
		kk = check_time()
		await self.inline.form(
			text=kk,
			message=message,
            gif="https://te.legra.ph/file/2ab9b131ceceb9b020583.mp4",
			reply_markup=[
				[
					{
						"text": "🍃 Refresh",
						"callback": self.refresh,
					}
				],
                [
					{
						"text": "🔻 Close",
						"action": "close",
					}
				]
			]
		)
	
	async def refresh(self, call: InlineCall): #thanks @Den4ikSuperOstryyPer4ik
		kk = check_time()
		await call.edit(
			text=kk,
			reply_markup=[
				[
					{
						"text": "🍃 Refresh",
						"callback": self.refresh,
					}
				],
                [
					{
						"text": "🔻 Close",
						"action": "close",
					}
				]
			]
		)
		await call.answer("Refreshed ✨")
