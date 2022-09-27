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
        self.jp_time = 9
        self.ch_time = 9
        self.us_time = -7
        self.kgz_time = 6
        self.uz_time = 5
        self.ind_time = 5.30
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
        offset = datetime.timedelta(hours=self.kgz_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        kgz = time1.strftime("%H:%M:%S")
        offset = datetime.timedelta(hours=self.jp_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        jp = time1.strftime("%H:%M:%S")
        offset = datetime.timedelta(hours=self.ind_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        ind = time1.strftime("%H:%M:%S")
        offset = datetime.timedelta(hours=self.ch_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        ch = time1.strftime("%H:%M:%S")

        amore =(
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
            f"<emoji document_id=6321003171678259486>🇹🇷</emoji> Turkey ➪ {ru}"
      )

        await message.edit(amore)
    
    @loader.owner
    async def atimeicmd(self, message):
        """See time on inline mode"""
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
        offset = datetime.timedelta(hours=self.kgz_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        kgz = time1.strftime("%H:%M:%S")
        offset = datetime.timedelta(hours=self.jp_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        jp = time1.strftime("%H:%M:%S")
        offset = datetime.timedelta(hours=self.ind_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        ind = time1.strftime("%H:%M:%S")
        offset = datetime.timedelta(hours=self.ch_time)
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        ch = time1.strftime("%H:%M:%S")

        amorei =(
            f"<emoji document_id=4920662486778119009>🌐</emoji> <b>Universal time</b>\n\n" 
            f"<emoji document_id=6323139226418284334>🇷🇺</emoji> Russia {ru}\n"
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
            f"<emoji document_id=6321003171678259486>🇹🇷</emoji> Turkey ➪ {ru}"
      )

        await self.inline.form(
            text=amorei,
            message=message,
            gif="https://siasky.net/LACn-4TBB9xoeeKkAcdGEccbiAX6gFGIiErQIFDVJbF0Qw",
        )
