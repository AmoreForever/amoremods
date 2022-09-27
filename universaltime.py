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
import logging

logger = logging.getLogger(__name__)

@loader.tds
class UniversalTimeMod(loader.Module):
    """See the time of other countries"""

    strings = {"name": "UnivTime"}

    def __init__(self):
        self.us_time = -7
        self.uz_time = 5
        self.az_time = 4
        self.ru_time = 3
        self.gr_time = 2
        self.uk_time = 1 

    @loader.owner
    async def atimecmd(self, message):
        """See time"""
        offset = datetime.timedelta(hours=self.ru_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        ru = time1.strftime("%H:%M:%S")
        offset = datetime.timedelta(hours=self.uz_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        uz = time1.strftime("%H:%M:%S")
        offset = datetime.timedelta(hours=self.az_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        az = time1.strftime("%H:%M:%S")
        offset = datetime.timedelta(hours=self.gr_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        gr = time1.strftime("%H:%M:%S")
        offset = datetime.timedelta(hours=self.uk_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        uk = time1.strftime("%H:%M:%S")
        offset = datetime.timedelta(hours=self.us_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        us = time1.strftime("%H:%M:%S")
        await utils.answer(
            message,
            f"<emoji document_id=4920662486778119009>🌐</emoji> Universal time\n\n" 
            f"<emoji document_id=6323139226418284334>🇷🇺</emoji> Russia ➪ {ru}\n"
            f"<emoji document_id=6323430017179059570>🇺🇿</emoji> Uzbekistan ➪ {uz}\n"
            f"<emoji document_id=6323289850921354919>🇺🇦</emoji> Ukraine ➪ {ru}\n"
            f"<emoji document_id=6323575251498174463>🇦🇿</emoji> Azerbaijan ➪ {az}\n"
            f"<emoji document_id=6320817337033295141>🇩🇪</emoji> German ➪ {gr}\n"
            f"<emoji document_id=6323589145717376403>🇬🇧</emoji> UK ➪ {uk}\n"
            f"<emoji document_id=6323602387101550101>🇵🇱</emoji> Poland ➪ {gr}\n"
            f"<emoji document_id=6323374027985389586>🇺🇸</emoji> USA ➪ {us}\n"
            )
