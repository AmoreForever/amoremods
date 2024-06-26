# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# requires: bs4 aiohttp

# meta developer: @hikamorumods

import aiohttp
from bs4 import BeautifulSoup as bs

from .. import utils, loader

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


class English:

    async def definition_get(self, word: str):
        async with aiohttp.ClientSession() as session:
            headers = {"User-Agent": user_agent}
            async with session.get(
                f"https://dictionary.cambridge.org/us/dictionary/english/{word}/",
                headers=headers,
            ) as resp:
                if resp.status != 200:
                    return f"Failed to retrieve data. Status code: {resp.status}"

                soup = bs(await resp.text(), "html.parser")
                if not (div_element := soup.find("div", class_="def ddef_d db")):
                    return "Definition not found"
                text = div_element.get_text()
                example_spans = soup.find_all("span", class_="eg deg")
                examples = []
                for ex in example_spans:
                    example_text = ex.get_text()
                    examples.append(example_text)

                return {"definition": text.replace(":", ""), "examples": examples}

    async def get_word_pronunciation_uk(self, word: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://dictionary.cambridge.org/dictionary/english/{word}",
                headers={"User-Agent": user_agent},
            ) as resp:
                if resp.status == 200:
                    soup = bs(await resp.text(), "html.parser")
                    try:
                        audio_tag = soup.find_all("audio", class_="hdn")[0]
                        pron_tag = soup.find_all("span", class_="ipa dipa lpr-2 lpl-1")[
                            0
                        ]
                        audio_src = audio_tag.find("source", type="audio/mpeg")["src"]

                        return {
                            "audio": f"https://dictionary.cambridge.org/us{audio_src}",
                            "pron": pron_tag.get_text(),
                        }
                    except IndexError:
                        return False

    async def get_word_pronunciation_us(self, word: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://dictionary.cambridge.org/dictionary/english/{word}",
                headers={"User-Agent": user_agent},
            ) as resp:
                if resp.status == 200:
                    soup = bs(await resp.text(), "html.parser")
                    try:
                        audio_tag = soup.find_all("audio", class_="hdn")[1]
                        audio_src = audio_tag.find("source")["src"]
                        pron_tag = soup.find_all("span", class_="ipa dipa lpr-2 lpl-1")[
                            1
                        ]

                        return {
                            "audio": f"https://dictionary.cambridge.org{audio_src}",
                            "pron": pron_tag.get_text(),
                        }

                    except IndexError:
                        return False

    async def thesaurus_synonyms(self, word: str):
        url = f"https://thesaurus.plus/thesaurus/{word}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers={"User-Agent": user_agent}) as resp:
                if resp.status == 200:
                    soup = bs(await resp.text(), "html.parser")
                    synonyms_list = []
                    synonyms_ul = soup.find_all("ul", class_="list")[1]
                    list_terms = synonyms_ul.find_all("li", class_="list_term")
                    for term in list_terms:
                        synonym = term.find("div", class_="p-2").get_text(strip=True)
                        synonyms_list.append(synonym)
                    return synonyms_list

    async def thesaurus_antonyms(self, word: str):
        url = f"https://thesaurus.plus/thesaurus/{word}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers={"User-Agent": user_agent}) as resp:
                if resp.status == 200:
                    soup = bs(await resp.text(), "html.parser")
                    antonyms_list = []
                    antonyms_ul = soup.find_all("ul", class_="list")[0]
                    list_terms = antonyms_ul.find_all("li", class_="list_term")
                    for term in list_terms:
                        antonym = term.find("div", class_="p-2").get_text(strip=True)
                        antonyms_list.append(antonym)
                    return antonyms_list


@loader.tds
class LexiwizMod(loader.Module, English):
    """Lexical wizard - your english companion"""

    strings = {
        "name": "Lexiwiz",
        "no_word": "🤷‍♂️ <b>No word provided</b>",
        "no_definition": "😖 <b>Unfortunately, I couldn't find the definition of this word.</b>",
        "definition": "📝 <b>Word:</b> <code>{}</code>\n\n🔆 <b>Definition:</b> <code>{}</code>\n\n📦 <b>Examples:</b>\n{}",
        "Pronunciation": "{} <b>{} Pronunciation:</b> <code>{}</code>\n🔊 <a href='{}'>Listen</a>",
        "no_synonyms": "😓 <b>Sorry, I couldn't find synonyms for this word.</b>",
        "synonyms": "📝 <b>Synonyms for the word:</b> <code>{}</code>\n\n🔆 <b>Synonyms:</b> <code>{}</code>",
        "no_antonyms": "😓 <b>Sorry, I couldn't find antonyms for this word.</b>",
        "antonyms": "📝 <b>Antonyms for the word:</b> <code>{}</code>\n\n🔆 <b>Antonyms:</b> <code>{}</code>",
        
    }

    @loader.command()
    async def getdef(self, message):
        """Get definition of a word"""

        word = utils.get_args_raw(message)

        if not word:
            await utils.answer(message, self.strings("no_word"))
            return

        definition = await self.definition_get(word)

        if definition == "Definition not found":
            await utils.answer(message, self.strings("no_definition"))

        if isinstance(definition, dict):
            text = ""

            _definition = definition["definition"]
            _examples = definition["examples"]

            for index, example in enumerate(_examples):
                text += f"<b>{index}</b>. <i>{example}</i>\n"

            await utils.answer(
                message, self.strings("definition").format(word, _definition, text)
            )

        else:
            await utils.answer(
                message, self.strings("definiotion").format(word, definition, " ")
            )

    @loader.command()
    async def getpron(self, message):
        """Get pronunciation of a word"""
        word = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        if not word:
            await utils.answer(message, self.strings("no_word"))
            return

        uk = await self.get_word_pronunciation_uk(word)
        us = await self.get_word_pronunciation_us(word)

        if uk:
            await message.delete()

            await message.client.send_file(
                message.to_id,
                uk["audio"],
                caption=self.strings("Pronunciation").format(
                    "🇬🇧",
                    "UK",
                    uk["pron"],
                    uk["audio"],
                ),
                voice_note=True,
                reply_to=reply.id if reply else None,
            )

        if us:
            await message.delete()

            await message.client.send_file(
                message.to_id,
                us["audio"],
                caption=self.strings("Pronunciation").format(
                    "🇺🇸",
                    "US",
                    us["pron"],
                    us["audio"],
                ),
                voice_note=True,
                reply_to=reply.id if reply else None,
            )

    @loader.command()
    async def getsyn(self, message):
        """Get synonyms of a word"""
        word = utils.get_args_raw(message)

        if not word:
            await utils.answer(message, self.strings("no_word"))
            return

        synonyms = await self.thesaurus_synonyms(word)

        if not synonyms:
            await utils.answer(message, self.strings("no_synonyms"))
            return

        await utils.answer(
            message, self.strings("synonyms").format(word, ", ".join(synonyms))
        )

    @loader.command()
    async def getant(self, message):
        """Get antonyms of a word"""
        word = utils.get_args_raw(message)

        if not word:
            await utils.answer(message, self.strings("no_word"))
            return

        antonyms = await self.thesaurus_antonyms(word)

        if not antonyms:
            await utils.answer(message, self.strings("no_antonyms"))
            return

        await utils.answer(
            message, self.strings("antonyms").format(word, ", ".join(antonyms))
        )