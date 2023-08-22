# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# scope: ffmpeg
# requires: pydub speechrecognition python-ffmpeg

# meta developer: @hikamorumods
# meta banner: https://github.com/AmoreForever/assets/blob/master/Speech.jpg?raw=true

import os
import logging
import speech_recognition as sr
from pydub import AudioSegment
from .. import loader, utils

logger = logging.getLogger(__name__)
recognizer = sr.Recognizer()

@loader.tds
class SpeechMod(loader.Module):
    """Simple speech recognition module."""
    
    strings = {
        "name": "Speech",
        "only_voice": "<emoji document_id=5877477244938489129>🚫</emoji> <b>Reply to a voice message!</b>",
        "downloading": "<emoji document_id=5213251580425414358>🔽</emoji> <b>Downloading...</b>",
        "recognizing": "<emoji document_id=5472199711366584503>👂</emoji> <b>Recognizing...</b>",
        "not_recognized": "<emoji document_id=5877477244938489129>🚫</emoji> <b>Not recognized</b>",
        "request_error": "<emoji document_id=5877477244938489129>🚫</emoji> <b>Request error occured.\n{}</b>",
        "recognized": "<emoji document_id=5267468588985363056>🚛</emoji> <b>Recognized:</b> <code>{}</code>",
    }
    
    strings_ru = {
        "only_voice": "<emoji document_id=5877477244938489129>🚫</emoji> <b>Ответь на голосовое сообщение!</b>",
        "downloading": "<emoji document_id=5213251580425414358>🔽</emoji> <b>Загрузка...</b>",
        "recognizing": "<emoji document_id=5472199711366584503>👂</emoji> <b>Распознавание...</b>",
        "not_recognized": "<emoji document_id=5877477244938489129>🚫</emoji> <b>Не распознано</b>",
        "request_error": "<emoji document_id=5877477244938489129>🚫</emoji> <b>Произошла ошибка запроса.\n{}</b>",
        "recognized": "<emoji document_id=5267468588985363056>🚛</emoji> <b>Распознано:</b> <code>{}</code>",
    }
    
    strings_uz = {
        "only_voice": "<emoji document_id=5877477244938489129>🚫</emoji> <b>Ovozli xabarga javob bering!</b>",
        "downloading": "<emoji document_id=5213251580425414358>🔽</emoji> <b>Yuklanmoqda...</b>",
        "recognizing": "<emoji document_id=5472199711366584503>👂</emoji> <b>Eshitilmoqda...</b>",
        "not_recognized": "<emoji document_id=5877477244938489129>🚫</emoji> <b>Tanilmadi</b>",
        "request_error": "<emoji document_id=5877477244938489129>🚫</emoji> <b>So'rovda xatolik yuz berdi.\n{}</b>",
        "recognized": "<emoji document_id=5267468588985363056>🚛</emoji> <b>Text:</b> <code>{}</code>",
    }
    
    
    
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "language",
                "ru-RU",
                lambda: "Language for recognition.",
                validator=loader.validators.RegExp(r"^[a-z]{2}-[A-Z]{2}$"),
            ),
        )

    @loader.command()
    async def spech(self, message):
        """Recognize voice message. Usage: .spech <reply to voice message>"""
        reply = await message.get_reply_message()
        if not reply or not reply.voice:
            await utils.answer(message, self.strings("only_voice"))
            return
        await utils.answer(message, self.strings("downloading"))
        voice = await message.client.download_media(reply.voice)
        wav_voice = voice.replace(voice.split(".")[-1], "wav")
        ogg_audio = AudioSegment.from_ogg(voice)
        ogg_audio.export(wav_voice, format="wav")
        audio = sr.AudioFile(wav_voice)
        with audio as source:
            try:
                audio = recognizer.record(source)
                await utils.answer(message, self.strings("recognizing"))
                recognized = recognizer.recognize_google(audio, language=self.config["language"])
            except sr.UnknownValueError:
                await utils.answer(message, self.strings("not_recognized"))
                return
            except sr.RequestError as e:
                await utils.answer(message, self.strings("request_error").format(e))
                return
        await utils.answer(message, self.strings("recognized").format(recognized))
        os.remove(voice)
        os.remove(wav_voice)
        
