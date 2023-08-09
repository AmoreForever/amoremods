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
from asyncio.exceptions import TimeoutError
from hikkatl.tl.types import Message
from hikkatl.errors.common import AlreadyInConversationError

from .. import utils, loader

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
        }
    
    strings_ru = {
        "wait": "<emoji document_id=5346192260029489215>💵</emoji> <b>Конвертирую...</b>",
        "no_args": "<emoji document_id=5343820329980535275>🖕</emoji> <b>Где аргументы?</b>",
        "unsupported": "<emoji document_id=5307761055873638139>🚫</emoji> <b>Валюта не поддерживается!</b>",
        "converted": "<emoji document_id=6037400506823871682>💸</emoji> <b>Сконвертирован <code>{}</code></b>\n\n",
        "already": "<emoji document_id=5348177037431414677>⚠️</emoji> <b>Подожди пока бот ответит!</b>",
        "wrong_currency": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji><b> Неправильная валюта</b>",
    }
    
    strings_uz = {
        "wait": "<emoji document_id=5346192260029489215>💵</emoji> <b>Valyuta konvertatsiyasi...</b>",
        "no_args": "<emoji document_id=5343820329980535275>🖕</emoji> <b>Argumetlar qayerda?</b>",
        "unsupported": "<emoji document_id=5307761055873638139>🚫</emoji> <b>Valyuta qo'llab-quvvatlanmaydi!</b>",
        "converted": "<emoji document_id=6037400506823871682>💸</emoji> <b>Konvertatsiya qilindi <code>{}</code></b>\n\n",
        "already": "<emoji document_id=5348177037431414677>⚠️</emoji> <b>Bot javob berishini kuting!</b>",
        "wrong_currency": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji><b> Noto'g'ri valyuta</b>",
    }
    
    strings_de = { # i'm really sorry for translations, i'm not good at it
        "wait": "<emoji document_id=5346192260029489215>💵</emoji> <b>Konvertiere...</b>",
        "no_args": "<emoji document_id=5343820329980535275>🖕</emoji> <b>Wo sind die Argumente?</b>",
        "unsupported": "<emoji document_id=5307761055873638139>🚫</emoji> <b>Nicht unterstützte Währung!</b>",
        "converted": "<emoji document_id=6037400506823871682>💸</emoji> <b>Konvertiert <code>{}</code></b>\n\n",
        "already": "<emoji document_id=5348177037431414677>⚠️</emoji> <b>Warten Sie, bis der Bot antwortet!</b>",
        "wrong_currency": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji><b> Falsche Währung</b>",
    }
    
    strings_tr = { # i'm really sorry for translations, i'm not good at it
        "wait": "<emoji document_id=5346192260029489215>💵</emoji> <b>Dönüştürülüyor...</b>",
        "no_args": "<emoji document_id=5343820329980535275>🖕</emoji> <b>Argümanlar nerede?</b>",
        "unsupported": "<emoji document_id=5307761055873638139>🚫</emoji> <b>Desteklenmeyen para birimi!</b>",
        "converted": "<emoji document_id=6037400506823871682>💸</emoji> <b>Dönüştürüldü <code>{}</code></b>\n\n",
        "already": "<emoji document_id=5348177037431414677>⚠️</emoji> <b>Bot cevap verene kadar bekleyin!</b>",
        "wrong_currency": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji><b> Yanlış para birimi</b>",
    }
    
    strings_kz = { # i'm really sorry for translations, i'm not good at it
        "wait": "<emoji document_id=5346192260029489215>💵</emoji> <b>Валюта айырбасталуда...</b>",
        "no_args": "<emoji document_id=5343820329980535275>🖕</emoji> <b>Аргументтер қайда?</b>",
        "unsupported": "<emoji document_id=5307761055873638139>🚫</emoji> <b>Валюта қолдау көрсетілмейді!</b>",
        "converted": "<emoji document_id=6037400506823871682>💸</emoji> <b>Айырбасталды <code>{}</code></b>\n\n",
        "already": "<emoji document_id=5348177037431414677>⚠️</emoji> <b>Бот жауап бергенге дейін күтіңіз!</b>",
        "wrong_currency": "<emoji document_id=5345937796102104039>🤷‍♀️</emoji><b> Дұрыс валюта емес</b>",
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
        "KG": ("🇰🇬", "KGS")}
    
    currencies = [
        "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
        "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
        "BSD", "BTC", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLF",
        "CLP", "CNH", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF",
        "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP",
        "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL",
        "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK",
        "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW",
        "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD",
        "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR",
        "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD",
        "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON",
        "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP",
        "SLL", "SOS", "SRD", "SSP", "STN", "SVC", "SYP", "SZL", "THB", "TJS",
        "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD",
        "UYU", "UZS", "VEF", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XDR",
        "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL", "TON", "ETH", "BTC"
    ]
    
    async def client_ready(self, client, db):
        await utils.dnd(client, self.bot, archive=True)
    
    async def get_ton_in_rub(self, am, what: str = "uzs", cup: bool = False) -> str:
        r = get("https://coinchefs.com/{}/ton/{}/".format(what, am)) if cup else get("https://coinchefs.com/ton/{}/{}/".format(what, am))
        soup = bs(r.text, "html.parser")
        result_div = soup.find('div', class_='convert-result')
        if result_div:
            result_text_div = result_div.find('div', class_='col-xs-10 col-sm-10 text-center result-text')
            if result_text_div:
                value_element = result_text_div.b
                if value_element:
                    value = value_element.get_text(strip=True)
                    return value
                else:
                    logger.debug("Value element not found")
            else:
                logger.debug("Result text div not found")
        else:
            logger.debug("Result div not found")
        return None

    @loader.command(ru_doc="<количество> [валюта] должны быть разделены пробелом")    
    async def conv(self, message: Message):
        """<amount> [currency] should be separated by space"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["no_args"])
            return
        if args.split(" ")[1].upper() not in self.currencies:
            await utils.answer(message, self.strings["wrong_currency"])
            return
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
                text_ += self.strings["converted"].format(args) if "ton".lower() not in args.lower() else self.strings["converted"].format(li_args[0] + " TON")
                for emoji, currency in self.currency_mapping.values():
                    if match := re.findall(f"{emoji} ?(.*) {currency}", res):
                        text_ += f"<b>{self.custom_emojis.get(emoji)} {currency}:</b> <code>{match[0]}</code>\n"


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
    