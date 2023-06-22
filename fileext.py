# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/fileext.jpg


from .. import loader, utils
from telethon.tl.types import Message
from bs4 import BeautifulSoup
import requests


async def search_extention(ext):
    sample_url = "https://www.fileext.com/file-extension/{}.html"
    response_api = requests.get(sample_url.format(ext))
    if not response_api.ok:
        return (
            f"Error fetching details for {ext}. Status code: {response_api.status_code}"
        )
    soup = BeautifulSoup(response_api.content, "html.parser")
    return soup.find_all("td", {"colspan": "3"})[-1].text


@loader.tds
class FileExtMod(loader.Module):
    """Get file extention details"""

    strings = {
        "name": "FileExt",
        "no_args": "<emoji document_id=5456652110143693064>🤷‍♂️</emoji> <b>No args passed</b>",
        "response": "<emoji document_id=5467732133629926938>🔍</emoji> <b>File Extension</b>: <code>{}</code>\n<emoji document_id=5467919175160705819>🔍</emoji> <b>Description</b>: <code>{}</code>",
    }

    @loader.command()
    async def fileext(self, message: Message):
        """Get file extention details"""
        if args := utils.get_args_raw(message):
            await utils.answer(
                message,
                self.strings("response").format(args, await search_extention(args)),
            )
        else:
            await utils.answer(message, self.strings("no_args"))
