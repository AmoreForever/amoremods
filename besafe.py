# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# If you don't like the module don't use it

# meta developer: @hikamorumods
# meta banner: https://github.com/AmoreForever/assets/blob/master/besafe.jpg?raw=true

import logging
import requests
import ast
import re
from .. import loader, utils

logger = logging.getLogger(__name__)

__version__ = (1, 0, 0)


@loader.tds
class BeSafe(loader.Module):
    """
    Check module before loading
    """
    
    strings = {
        "name": "BeSafe",
        "no_args_or_reply": "<emoji document_id=5456652110143693064>🤷‍♂️</emoji> <b>[BeSafe]</b> No link or reply to file",
        "safe": "<emoji document_id=5203929938024999176>🛡</emoji> <b>Module is safe</b>",
        "suspicious": "<emoji document_id=5325771498718241219>🔎</emoji> Module is suspicious\n\n<emoji document_id=6334443713485342501>⛩</emoji> <b>Suspicious imports:</b>\n",
        'sus_keywords': "\n<emoji document_id=6334405093139416847>🔑</emoji> <b>Suspicous keywords:</b>"
    }
    strings_ru = {
        "no_args_or_reply": "<emoji document_id=5456652110143693064>🤷‍♂️</emoji> <b>[BeSafe]</b> Нет ссылки или реплея на модуль",
        "safe": "<emoji document_id=5203929938024999176>🛡</emoji> <b>Модуль безопасен</b>",
        "suspicious": "<emoji documentx_id=5325771498718241219>🔎</emoji> Модуль подозрительный\n\n<emoji document_id=6334443713485342501>⛩</emoji> <b>Подозрительные импорты:</b>\n",
        'sus_keywords': "\n<emoji document_id=6334405093139416847>🔑</emoji> <b>Подозрительные ключевые слова:</b>"
    }
    
    def extract_imports(self, code):
        code = code.lstrip('\ufeff') # крч удаление символа BOM, если он есть
        
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            if "invalid non-printable character" not in str(e):
                raise
            code = code.encode('utf-8-sig').decode('utf-8')
            tree = ast.parse(code)
        imports = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(name.name for name in node.names)
            elif isinstance(node, ast.ImportFrom):
                module_name = node.module
                imports.extend(f"{module_name}.{name.name}" for name in node.names)
        return imports
        
        
    
    suspicious_imports = [
        'glob',
        'os',
        'sys',
        'telethon.tl.TLRequest',
        'requests',
    ]
    suspicious_keywords = [
        r'0x418d4e0b',
        r'0xf5b399ac',
        r'w+z+mm+"A"+nk+u+h+lk',
        r'b"\x0bN\x8dA"'
        r'session',
        r'TestingHikka_BOT' # временно будет тут 
    ]
    
    def extract_keywords(self, code):
        words = []
        for word in self.suspicious_keywords:
            if r := re.findall(word, code):
                words.append(r[0])
        return words
    
        
    
    @loader.command()
    async def bs(self, message):
        """
        BeSafe - <reply to module> or <link to module>
        """
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        
        if args:
            r = await utils.run_sync(requests.get, args)
            string = r.text
        elif reply:
            code = (await self._client.download_file(reply.media, bytes)).decode("utf-8")
            string = code
        else:
            await utils.answer(message, self.strings["no_args_or_reply"])
            
        imports = self.extract_imports(string)
        sus_imports = [f"▫️ <code>{imp}</code>" for imp in self.suspicious_imports if imp in imports]
        sus_keywords = []
        
        if sus_imports:
            kw = self.extract_keywords(string)
            sus_keywords = [f"▫️ <code>{k}</code>" for k in self.suspicious_keywords if k in kw]
    
        if sus_imports or sus_keywords:
            sus_list = sus_imports + [self.strings["sus_keywords"]] + sus_keywords
            text = self.strings["suspicious"] + '\n'.join(sus_list)
        else:
            text = self.strings["safe"]
            
        await utils.answer(message, text)
    
        