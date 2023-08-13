# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://github.com/AmoreForever/assets/blob/master/Aeconv.jpg?raw=true
# meta pic: https://cdn-icons-png.flaticon.com/512/5670/5670084.png

import re
import logging

from bs4 import BeautifulSoup as bs
from requests import get
from asyncio import sleep
from asyncio.exceptions import TimeoutError
from hikkatl.tl.types import Message
from hikkatl.errors.common import AlreadyInConversationError

from .. import utils, loader
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)

@loader.tds
class Aeconv(loader.Module):
    """Easy and fast valute converter"""
    
    bot = "@exchange_rates_vsk_bot"
    strings = {
        "name": "Aeconv",
        "wait": "<emoji document_id=5346192260029489215>💵</emoji> <b>Converting...</b>",
        "no_args": "<emoji document_id=5343820329980535275>🖕</emoji> <b>Where are the arguments?</b>",
        "unsupported": "<emoji document_id=5307761055873638139>🚫</emoji> <b>Unsupported currency!</b>",
        "converted": "<emoji document_id=6037400506823871682>💸</emoji> <b>Converted <code>{}</code></b>\n\n",
        "already": "<emoji document_id=5348177037431414677>⚠️</emoji> <b>Wait until the bot responds!</b>",
        "wrong_currency": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji><b> Wrong currency</b>",
        "choose_currency": "📉 <b> Choose currency</b>",
        "processing": "🕔 <b>Processing...</b>",
        "done": "✅ <b>Done!</b>",
        "already_in_conv": "⚠️ <b>Already in conversation!</b>",
        }
    
    strings_ru = {
        "wait": "<emoji document_id=5346192260029489215>💵</emoji> <b>Конвертирую...</b>",
        "no_args": "<emoji document_id=5343820329980535275>🖕</emoji> <b>Где аргументы?</b>",
        "unsupported": "<emoji document_id=5307761055873638139>🚫</emoji> <b>Валюта не поддерживается!</b>",
        "converted": "<emoji document_id=6037400506823871682>💸</emoji> <b>Сконвертирован <code>{}</code></b>\n\n",
        "already": "<emoji document_id=5348177037431414677>⚠️</emoji> <b>Подожди пока бот ответит!</b>",
        "wrong_currency": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji><b> Неправильная валюта</b>",
        "choose_currency": "📉 <b> Выберите валюту</b>",
        "processing": "🕔 Обрабатываю...",
        "done": "<code>[Aeconv]</code> ✅ <b> Готово!</b>",
        "already_in_conv": "⚠️ <b>Жди пока закончится процесс!</b>",
    }
    
    strings_uz = {
        "wait": "<emoji document_id=5346192260029489215>💵</emoji> <b>Valyuta konvertatsiyasi...</b>",
        "no_args": "<emoji document_id=5343820329980535275>🖕</emoji> <b>Argumetlar qayerda?</b>",
        "unsupported": "<emoji document_id=5307761055873638139>🚫</emoji> <b>Valyuta qo'llab-quvvatlanmaydi!</b>",
        "converted": "<emoji document_id=6037400506823871682>💸</emoji> <b>Konvertatsiya qilindi <code>{}</code></b>\n\n",
        "already": "<emoji document_id=5348177037431414677>⚠️</emoji> <b>Bot javob berishini kuting!</b>",
        "wrong_currency": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji><b> Noto'g'ri valyuta</b>",
        "choose_currency": "📉 <b> Valyutani tanlang</b>",
        "processing": "🕔 Qayta ishlayapman...",
        "done": "<code>[Aeconv]</code> ✅ <b>Tayyor!</b>",
        "already_in_conv": "⚠️ <b>Protsess tugaguncha kuting!</b>",
    }
    
    strings_de = { # i'm really sorry for translations, i'm not good at it
        "wait": "<emoji document_id=5346192260029489215>💵</emoji> <b>Konvertiere...</b>",
        "no_args": "<emoji document_id=5343820329980535275>🖕</emoji> <b>Wo sind die Argumente?</b>",
        "unsupported": "<emoji document_id=5307761055873638139>🚫</emoji> <b>Nicht unterstützte Währung!</b>",
        "converted": "<emoji document_id=6037400506823871682>💸</emoji> <b>Konvertiert <code>{}</code></b>\n\n",
        "already": "<emoji document_id=5348177037431414677>⚠️</emoji> <b>Warten Sie, bis der Bot antwortet!</b>",
        "wrong_currency": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji><b> Falsche Währung</b>",
        "choose_currency": "📉 <b> Währung auswählen</b>",
        "processing": "🕔 Verarbeitung...",
        "done": "<code>[Aeconv]</code> ✅ <b>Fertig!</b>",
        "already_in_conv": "⚠️ <b>Warten Sie, bis der Prozess beendet ist!</b>",
        
    }
    
    strings_tr = { # i'm really sorry for translations, i'm not good at it
        "wait": "<emoji document_id=5346192260029489215>💵</emoji> <b>Dönüştürülüyor...</b>",
        "no_args": "<emoji document_id=5343820329980535275>🖕</emoji> <b>Argümanlar nerede?</b>",
        "unsupported": "<emoji document_id=5307761055873638139>🚫</emoji> <b>Desteklenmeyen para birimi!</b>",
        "converted": "<emoji document_id=6037400506823871682>💸</emoji> <b>Dönüştürüldü <code>{}</code></b>\n\n",
        "already": "<emoji document_id=5348177037431414677>⚠️</emoji> <b>Bot cevap verene kadar bekleyin!</b>",
        "wrong_currency": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji><b> Yanlış para birimi</b>",
        "choose_currency": "📉 <b> Para birimini seçin</b>",
        "processing": "🕔 İşleniyor...",
        "done": "<code>[Aeconv]</code> ✅ <b>Tamam!</b>",
        "already_in_conv": "⚠️ <b>İşlem bitene kadar bekleyin!</b>",
    }
    
    strings_kk   = { # i'm really sorry for translations, i'm not good at it
        "wait": "<emoji document_id=5346192260029489215>💵</emoji> <b>Валюта айырбасталуда...</b>",
        "no_args": "<emoji document_id=5343820329980535275>🖕</emoji> <b>Аргументтер қайда?</b>",
        "unsupported": "<emoji document_id=5307761055873638139>🚫</emoji> <b>Валюта қолдау көрсетілмейді!</b>",
        "converted": "<emoji document_id=6037400506823871682>💸</emoji> <b>Айырбасталды <code>{}</code></b>\n\n",
        "already": "<emoji document_id=5348177037431414677>⚠️</emoji> <b>Бот жауап бергенге дейін күтіңіз!</b>",
        "wrong_currency": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji><b> Дұрыс валюта емес</b>",
        "choose_currency": "📉 <b> Валютаны таңдаңыз</b>",
        "processing": "🕔 Қайта өңдеу...",
        "done": "<code>[Aeconv]</code>  ✅ <b>Тайық!</b>",
        "already_in_conv": "⚠️ <b>Процесс аяқталғанда дейін күтіңіз!</b>",
    }
    
    custom_emojis = {
        "🇬🇧": "<emoji document_id=6323589145717376403>🇬🇧</emoji>",
        "🇺🇿": "<emoji document_id=6323430017179059570>🇺🇿</emoji>",
        "🇺🇸": "<emoji document_id=6323374027985389586>🇺🇸</emoji>",
        "🇷🇺": "<emoji document_id=6323139226418284334>🇷🇺</emoji>",
        "🇰🇿": "<emoji document_id=6323135275048371614>🇰🇿</emoji>",
        "🇪🇺": "<emoji document_id=6323217102765295143>🇪🇺</emoji>",
        "🇺🇦": "<emoji document_id=6323289850921354919>🇺🇦</emoji>",
        "🇹🇷": "<emoji document_id=6321003171678259486>🇹🇷</emoji>",
        "🇵🇱": "<emoji document_id=6323602387101550101>🇵🇱</emoji>",
        "🇰🇬": "<emoji document_id=6323615997852910673>🇰🇬</emoji>",
        "bit": "<emoji document_id=6034931909945985955>💰</emoji>",
        "eth": "<emoji document_id=5280647120607521572>🔹</emoji>",
        "ton": "<emoji document_id=5863980370340351884>💰</emoji>"
    }
    
    currency_mapping = {
        "EU": ("🇪🇺", "EUR"),
        "GB": ("🇬🇧", "GBP"),
        "UZ": ("🇺🇿", "UZS"),
        "US": ("🇺🇸", "USD"),
        "RU": ("🇷🇺", "RUB"),
        "KZ": ("🇰🇿", "KZT"),
        "UA": ("🇺🇦", "UAH"),
        "PL": ("🇵🇱", "PLN"),
        "TR": ("🇹🇷", "TRY"),
        "KG": ("🇰🇬", "KGS")
        }
    
    currencies = [
        "EUR", "GBP", "UZS", "USD", "RUB", "KZT", "UAH", "PLN", "TRY", "KGS", "TON", "ETH", "BTC"
    ]
    
    currency_flags = {
        "EUR": "🇪🇺",
        "GBP": "🇬🇧",
        "UZS": "🇺🇿",
        "USD": "🇺🇸",
        "RUB": "🇷🇺",
        "KZT": "🇰🇿",
        "UAH": "🇺🇦",
        "PLN": "🇵🇱",
        "TRY": "🇹🇷",
        "KGS": "🇰🇬"
    }
    
    letters_stashing = {
        "E": "cur_df",
        "G": "cur_gh", 
        "P": "cur_nq",
        "R": "cur_rs",
        "S": "cur_rs",
        "T": "cur_tu",
        "U": "cur_tu",
    }
    
    def currencies_markup(self, argument: str = "") -> list:
        return utils.chunks(
            [
                {
                    "text": f"{self.currency_flags[cur]} {cur}",
                    "callback": self.callback_4_currency,
                    "args": (cur,),
                }
                for cur in [
                    i
                    for i in self.currency_flags.keys()
                    if i.startswith(argument.upper())
                ]
                if cur.startswith(argument.upper())
            ],
            5,
        )
    
    async def client_ready(self, client, db):
        await utils.dnd(client, self.bot, archive=True)
    
    async def get_ton_in_rub(self, am, what: str = "uzs", cup: bool = False) -> str:
        r = (
            get(f"https://coinchefs.com/{what}/ton/{am}/")
            if cup
            else get(f"https://coinchefs.com/ton/{what}/{am}/")
        )
        soup = bs(r.text, "html.parser")
        if result_div := soup.find('div', class_='convert-result'):
            if result_text_div := result_div.find(
                'div', class_='col-xs-10 col-sm-10 text-center result-text'
            ):
                if value_element := result_text_div.b:
                    return value_element.get_text(strip=True)
                else:
                    logger.debug("Value element not found")
            else:
                logger.debug("Result text div not found")
        else:
            logger.debug("Result div not found")
        return None

    async def callback_4_currency(self, call: InlineCall, currency: str):
        try:
            first_letter = currency[0]
            await call.answer(self.strings["processing"], show_alert=True)
            await call.delete()
            async with self.client.conversation(self.bot) as conv:
                m = await conv.send_message("/settings")
                r = await conv.get_response()
                await r.click(data=b'cur_menu')
                await r.click(data=b'cur_curmenu')
                await r.click(data=self.letters_stashing[first_letter])
                await r.click(data=f"cur_{currency.upper()}")
                await r.delete()
                await m.delete()
            await self.inline.bot.send_message(self.tg_id, self.strings["done"])
        except AlreadyInConversationError:
            await call.answer(self.strings["already_in_conv"], show_alert=True)
        
    @loader.command(ru_doc="<количество> [валюта] должны быть разделены пробелом")
    async def conv(self, message: Message):
        """<amount> [currency] should be separated by space"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["no_args"])
            return
        # if args.split(" ")[1].upper() not in self.currencies:
        #     await utils.answer(message, self.strings["wrong_currency"])
        #     return
        await utils.answer(message, self.strings["wait"])
        if "ton".lower() in args.lower():
            li_args = args.split(" ")
            ex_ = await self.get_ton_in_rub(li_args[0])
        try:
            async with message.client.conversation(self.bot) as conv:
                msg = await conv.send_message(args) if "ton".lower() not in args.lower() else await conv.send_message(ex_)
                r = await conv.get_response()
                res = r.text
                text_ = ""
                text_ += (
                    self.strings["converted"].format(args)
                    if "ton".lower() not in args.lower()
                    else self.strings["converted"].format(f"{li_args[0]} TON")
                )
                for emoji, currency, *_ in self.currency_mapping.values():
                    if match := re.findall(f"{emoji} ?(.*) {currency}", res):
                        text_ += (
                            f"<b>{self.custom_emojis.get(emoji)} {currency}:</b> "
                            f"<code>{match[0]}</code>\n"
                        )

                if match := re.findall(r"(.*) BTC", res):
                    text_ += f"\n<b>{self.custom_emojis['bit']} BTC:</b> <code>{match[0]}</code>\n"
                if match := re.findall(r"(.*) ETH", res):
                    text_ += f"<b>{self.custom_emojis['eth']} ETH:</b> <code>{match[0]}</code>\n"

                if ex_ := await self.get_ton_in_rub(args.split(" ")[0], args.split(" ")[1].lower(), True):
                    text_ += f"<b>{self.custom_emojis['ton']} TON:</b> <code>{ex_.split(' = ')[1]}</code>\n"
                await utils.answer(message, text_)
                await msg.delete()
                await r.delete()
        except AlreadyInConversationError:
            await utils.answer(message, self.strings["already"])
        except TimeoutError:
            await utils.answer(message, self.strings["unsupported"])
        except IndexError:
            await utils.answer(message, self.strings["no_args"])
            
            
    @loader.command(ru_doc="[валюта] | без аргументов покажет список валют для включения/выключения")
    async def controlvalute(self, message: Message):
        """[currency] | without arguments will show list of currencies for enable/disable"""
        if args := utils.get_args_raw(message):
            await utils.answer(message, self.strings["choose_currency"], reply_markup=self.currencies_markup(args))
        else:
            return await utils.answer(message, self.strings["choose_currency"], reply_markup=self.currencies_markup())
                    
            
        