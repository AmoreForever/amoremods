# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://github.com/AmoreForever/assets/blob/master/Figlet.jpg?raw=true



import pyfiglet
import functools
from .. import loader, utils


class Figlet(loader.Module):
    """Creates Figlet Text"""

    strings = {"name": "Figlet"}
    style_to_font = {
        "slant": "slant",
        "3d": "3-d",
        "5line": "5lineoblique",
        "alpha": "alphabet",
        "banner": "banner3-D",
        "doh": "doh",
        "iso": "isometric1",
        "letter": "letters",
        "allig": "alligator",
        "dotm": "dotmatrix",
        "bubble": "bubble",
        "bulb": "bulbhead",
        "digi": "digital"
    }

    @loader.command()
    async def listfig(self, message):
        """List of figlet styles"""
        keys_list = " , ".join(list(self.style_to_font.keys()))
        await utils.answer(message, f"🚩 Available styles: {keys_list}")

    @loader.command()
    async def figlet(self, message):
        """Create figlet text, <style> | <args>"""
        args = utils.get_args_raw(message).split(" | ")
        if len(args) < 2:
            await utils.answer(message, "Not enough arguments")
            return

        font = self.style_to_font.get(args[0], None)
        if font is None:
            await utils.answer(message, "There is no such style")
            return

        if not args[1]:
            await utils.answer(message, "Text argument is empty")
            return

        result = await self.figlet_format_cached(args[1], font)
        await utils.answer(message, f"<code>{result}<code>")

    @staticmethod
    @functools.lru_cache(maxsize=None)
    async def figlet_format_cached(text, font):
        return pyfiglet.figlet_format(text, font=font)
