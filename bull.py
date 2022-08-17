#▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#█▀█ █░▀░█ █▄█ █▀▄ ██▄
#          
#             © Copyright 2022
#
#          https://t.me/the_farkhodov 
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html


# meta pic: https://te.legra.ph/file/bd971a30d710ecdb29ac7.jpg
# meta banner: https://te.legra.ph/file/5f1b98c4a5c0877d7837c.jpg
# meta developer: @amoremods

import random
from ..inline.types import InlineQuery
from .. import loader, utils


@loader.tds
class BullMod(loader.Module):
    """Bull пиз#а собеседнику"""
    
    strings = {'name': 'BullMod'  }

    @loader.inline_everyone
    async def bull_inline_handler(self, query: InlineQuery):
        """Забулить кого-то жесткими матами про мать"""

        bull = random.choice(["ТЫ ПОНИМАЕШЬ ЧТО Я ПИЗДАК В ТЕОЙ МАТРЕИ НА СВОЙ УЙ КАК МАКАРОНИНУ НАМОТАЛ БЛЯДЬ И НАЧАЛ РАСКРУЧИВАТЬ ЕЁ, ПОСЛЕ ЧЕГО ВЫКИНУЛ В КОСМОС, ЧТОБ ЕЁ ТАМ ИНОПЛАНЕТЯНЫ ХУЯМИ РВАЛИ?)", "ТЫ ПОНИМАЕШЬ ЧТО Я ТВОЮ МАТЬ ОТПРАВИЛ СО СВОЕГО ЪХУЯ В НЕБО, ЧТОБ ОНА СВОИМ ПИЗДАКОМ ПРИНИМАЛА МИТЕОРИТНУЮ АТАКУ?)", "ЕСЛИ ТЫ СЕЙЧАС ТАК И БУДЕШЬ ПРОДОЛЖАТЬ ПРОТИВОРЕЧИТЬ МОЕМУ ХУЮ, КАК ИМ КАК БЛЯДЬ НА НЛО ЗАХВОЧУ ТВОЁ ОЧКО И НАЧНУ ОПЫТЫ ПРОВОДИТЬ", "ТЫ ПОНИМАЕШЬЧ ТО ВТОЯ МАТЬ МОЙ ХУЙ ЗАВЕРНУЛА В ПАКЕТИК ПОТОМУ ЧТО У ЭТОЙ БОМЖИХИ НЕБЫЛО ДЕНЕГ НА ПРЕЗИКИ, И ПОКЕТИК ПОРВАЛСЯ, И РОДИЛОСЬ ТАКОЕ ХУЙЛО КАК ТЫ", "TЫ ПОНИМАЕШЬ ЧТО Я ТВОЮ МАТЬ СЛУЧАЙНО СВОИМ ХУЁМ СМЁЛ НАХУЙ СО СВОЕГО ПУТИ, И ОНА УЛЕТЕЛА НА РАДИУС ОБСТРЕЛА МОЕЙ ЗАЛУПЫ", "АМЕБА ЕБАНАЯ СУКА) МАМАШКУ ТВОЮ ДЫРЯВИЛ ЧЕТ ) НАХУЙ ТВОЯ МАМАША КРИЧИТ КОГДА Я НАЧИНАЮ ЕБАТЬ ЕЕ)", "АМЕБА ИЛИ ТЫ ОЛЕНЬ?) СЛЫШЬ ЕСЛИ ТЫ ПРОЛЬЕШЬ НА МОЙ ХУЙ СЛЕЗЫ , ТО ТЫ НЕ РАССЧИТЫВАЙ НА ТО , ЧТО ПОТОМ К ТЕБЕ ПРИДЕТ ФЕЯ И ПООБЕЩАЕТ ТЕБЕ ДОЛГУЮ И СЧАСТЛИВУЮ ЖИЗНЬ)", "ОЛЕНЬ ТЫ ЕБАНЫЙ) МАТЬ ТВОЮ ЕБУ ЧЕТ ) ДАВАЙ ТЫ ЩАС ВОЗЬМЕШЬ МОЙ ХУЙ КАК ПЕРО И СЛОВНО КАК ПИСАТЕЛЬ СЕРЕБРЯНОГО ВЕКА НАПИШЕШЬ КАКОЙ НИБУДЬ РОМАН КОТОРЫЙ БУДЕТ ПО РАЗМЕРУ ПРИМЕРНО КАК МАСТЕР И МАРГАРИТА )", "твоя мамка блядоебская кобыла и лезби", "у тебя мать сраная шлюха"])

        return {
            "title": "Пошутить про маму",
            "thumb": "https://te.legra.ph/file/b2a6c8d20e0034a534ac4.jpg",
            "description": "Отправить...",
            "message": f"<i>{bull}</i>"
                     }
