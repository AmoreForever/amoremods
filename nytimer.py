# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Nytimer.jpg

from .. import loader, utils
import datetime
from time import strftime


@loader.tds
class NYMod(loader.Module):
    """Check how much is left until the new year"""

    strings = {'name': 'NewYearTimer'}

    async def nycmd(self, message):
        """Check date"""
        now = datetime.datetime.today()
        ng = datetime.datetime(int(strftime('%Y')) + 1, 1, 1)
        d = ng - now
        mm, ss = divmod(d.seconds, 60)
        hh, mm = divmod(mm, 60)
        soon = '<b><emoji document_id=6334530007968253960>☃️</emoji> Until the <u>New Year</u>: {} d. {} h. {} m. {} s.</b>\n<b><emoji document_id=5393226077520798225>🥰</emoji> Wait for the new year together <u>Family</u></b>'.format(
            d.days, hh, mm, ss)
        await utils.answer(message, soon)
