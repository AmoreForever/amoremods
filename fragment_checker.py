# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://github.com/AmoreForever/assets/blob/master/fragment_checker.jpg?raw=true
# requires: bs4


import requests
from bs4 import BeautifulSoup
from .. import loader, utils

class Fragment(loader.Module):
    """Show how much is the username in the Fragment.com"""
    
    strings = {"name": "FragmentChecker"}
    
    @loader.command()
    async def fcheck(self, message):
        """check username in the Fragment.com"""
        args = utils.get_args_raw(message)
        response = requests.get(f"https://fragment.com/username/{args}")

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            elements = soup.select(".table-cell-value.tm-value.icon-before.icon-ton")
        if elements:
            text = elements[0].text.strip()
            await utils.answer(message, f"<emoji document_id=5215219508670638513>💎</emoji> <b>Username Found!</b>\n<emoji document_id=5467626799556992380>✈️</emoji> <b>Username:</b> <code>{args}</code>\n<emoji document_id=5460720028288557729>🪙</emoji> <b>Cost:</b> <code>{text}</code> TON")
        if not elements:
            await utils.answer(message, f"<emoji document_id=5212926868012935693>❌</emoji> <b>Username <code>{args}</code> not found!</b>")
            
        
