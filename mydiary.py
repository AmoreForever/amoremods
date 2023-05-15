__version__ = (1, 0, 0)
#            ▀█▀  █ █ █▀█  █▀▄▀█  ▄▀█ █▀
#             █  █▀█ █▄█ █ ▀  █ █▀█ ▄█  
#                https://t.me/netuzb
#
# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru



# meta pic: https://te.legra.ph/file/4c1b4581de961df145a70.png
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Mydiary.jpg

# meta developer: @hikamoru & @wilsonmods
# scope: hikka_min 1.4.0


from .. import loader, utils
from telethon.tl.types import Message

from ..inline.types import InlineQuery
from ..inline.types import InlineCall

emoji_close = "🔻 "
emoji_back = "↙️ "
emoji_open = "💌 "
emoji_about = "🚨 "

@loader.tds
class PagesMod(loader.Module):
    """Diary page"""

    strings = {
        "name": "Diary",
        "_about_module": "What does this module do? - here you can write about your day and write notes",
        "_cfg_inline_banner": "Set `True` in order to disable an inline media banner.",
        "_cfdiary_open_text": "enter a diary name or information about it",
        "_cfdiary_second_text": "here you can write on dairy «text2»",
        "_cfdiary_three_text": "here you can write on dairy «text3»",
        "_cfdiary_four_text": "here you can write on dairy «text4»",
        "_cfdiary_first_text": "here you can write on dairy «text1»",
        "_cfdiary_second_text": "here you can write on dairy «text2»",
        "_cfdiary_three_text": "here you can write on dairy «text3»",
        "_cfdiary_four_text": "here you can write on dairy «text4»",
        "_cfg_button_1_": "here you can change button name «day1»",
        "_cfg_button_2_": "here you can change button name «day2»",
        "_cfg_button_3_": "here you can change button name «day3»",
        "_cfg_button_4_": "here you can change button name «day4»",        
        "x": emoji_close + "Close",
        "back": emoji_back + "Back",
        } 
        
    strings_ru = {
        "_about_module": "Что делает этот модуль? - Ты ты можешь писать свои заметки или что делал сегодня",
        "_cfg_inline_banner": "Установите `True`, чтобы отключить встроенный медиа-баннер",
        "_cfdiary_open_text": "Введите название дневника или информацию о нем",
        "_cfdiary_first_text": "здесь ты можешь написать написать дневник на «text1»",
        "_cfdiary_second_text": "здесь ты можешь написать написать дневник на «text2»",
        "_cfdiary_three_text": "здесь ты можешь написать написать дневник на «text3»",
        "_cfdiary_four_text": "здесь ты можешь написать написать дневник на «text4»",
        "_cfg_button_1_": "здесь ты можешь поменять название кнопки «day1»",
        "_cfg_button_2_": "здесь ты можешь поменять название кнопки «day2»",
        "_cfg_button_3_": "здесь ты можешь поменять название кнопки «day3»",
        "_cfg_button_4_": "здесь ты можешь поменять название кнопки «day4»",
        "x": emoji_close + "Закрыть",
        "back": emoji_back + "Назад",
        }
        
    strings_uz = {
        "_about_module": "Modul vazifasi nima?\n- Siz modul orqali bugungi kun rejangiz yoki eslatmani saqlab qoʻyishingiz mumkin.",
        "_cfg_inline_banner": "Media-bannerni yopish uchun `True` rejimini yoqing",
        "_cfdiary_open_text": "Kundalik nomini yoki unga bogʻliq maʼlumotni yozing",
        "_cfdiary_first_text": "Bu yerda siz «text_numb_1» sozlashingiz mumkin",
        "_cfdiary_second_text": "Bu yerda siz «text_numb_2» sozlashingiz mumkin",
        "_cfdiary_three_text": "Bu yerda siz «text_numb_3» sozlashingiz mumkin",
        "_cfdiary_four_text": "Bu yerda siz «text_numb_4» sozlashingiz mumkin",
        "_cfg_button_1_": "Bu yerda siz «button_numb_1» tugmasini sozlashingiz mumkin",
        "_cfg_button_2_": "Bu yerda siz «button_numb_2» tugmasini sozlashingiz mumkin",
        "_cfg_button_3_": "Bu yerda siz «button_numb_3» tugmasini sozlashingiz mumkin",
        "_cfg_button_4_": "Bu yerda siz «button_numb_4» tugmasini sozlashingiz mumkin",
        "x": emoji_close + "Yopish",
        "back": emoji_back + "Orqaga",
        }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "open_text",
                "Here is a caption for my diary",
                doc=lambda: self.strings('_cfdiary_open_text'),
            ),
            loader.ConfigValue(
                "off_inline_banner",
                False,
                lambda: self.strings("_cfg_inline_banner"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "button_numb_1",
                "Day 1",
                doc=lambda: self.strings('_cfg_button_1_'),
            ),
            loader.ConfigValue(
                "button_numb_2",
                "Day 2",
                doc=lambda: self.strings('_cfg_button_2_'),
            ),            
            loader.ConfigValue(
                "button_numb_3",
                "Day 3",
                doc=lambda: self.strings('_cfg_button_3_'),
            ),            
            loader.ConfigValue(
                "button_numb_4",
                "Day 4",
                doc=lambda: self.strings('_cfg_button_4_'),
            ),                        
            loader.ConfigValue(
                "text_numb_1",
                "Today i played football with my friends then i fall,",
                doc=lambda: self.strings('_cfdiary_first_text'),
            ),
            loader.ConfigValue(
                "text_numb_2",
                "Today i walked with my friends and i saw my best friend who was drawer",
                doc=lambda: self.strings('_cfdiary_second_text'),
            ),
            loader.ConfigValue(
                "text_numb_3",
                "What are you did today?",
                doc=lambda: self.strings('_cfdiary_three_text'),        
            ),
            loader.ConfigValue(
                "text_numb_4",
                "What are you did today?",
                doc=lambda: self.strings('_cfdiary_four_text'),
            ),           
            loader.ConfigValue(
                "banner_numb_1",
                "https://imgur.com/NqNGNOb",
                lambda: f"here you can write on dairy photo1",
            ),
            loader.ConfigValue(
                "banner_numb_2",
                "https://ibb.co/ZJ9hnfL",
                lambda: f"here you can write on dairy photo2",
            ),
            loader.ConfigValue(
                "banner_numb_3",
                "https://imgur.com/kITkUry",
                lambda: f"here you can write on dairy photo3",
            ),
            loader.ConfigValue(
                "banner_numb_4",
                "https://imgur.com/TOzh9u1",
                lambda: f"here you can write on dairy photo3",
            ),
          )
    
    async def cfdiarycmd(self, message):
             """> Set up buttons for the module"""
             name = self.strings("name")
             await self.allmodules.commands["config"](
             await utils.answer(message, 
             f"{self.get_prefix()}config {name}")
             )
    
    async def mydiarycmd(self, message: Message):
            """> Main the diary section"""
            await self.inline.form(
            text = self.config["open_text"],
            message=message, 
            reply_markup=[
            [{
                "text": f"{emoji_open}Open diary", 
                "callback": self.page_one
            }],
            [{
                "text": f"{emoji_about}About modules", 
                "callback": self._about_us
            }]], 
                **{"photo": "https://te.legra.ph/file/64bb29a68030e118dfa21.jpg"},
         )
    
    async def mydiary_inline_handler(self, query: InlineQuery):
        """> Main the diary section"""
        btn_a = [{
                    "text": f"{emoji_open}Open diary", 
                    "callback": self.page_one
                 }],
        btn_b = [{
                    "text": f"{emoji_about}About modules", 
                    "callback": self._about_us
                 }],
        msg_type = "message" if self.config["off_inline_banner"] else "caption"
        return {
            "title": "open diary",
            "description": "open my own diary page",
            msg_type: self.config['open_text'],
            "photo": "https://te.legra.ph/file/64bb29a68030e118dfa21.jpg",
            "thumb": (
                "https://te.legra.ph/file/4c1b4581de961df145a70.png"
            ),
            "reply_markup": btn_a + btn_b,
        }
    
    async def _back(self, call: InlineCall):
        await call.edit(
        text = self.config["open_text"],
            reply_markup=[
            [{
                "text": f"{emoji_open}Open diary", 
                "callback": self.page_one
            }],
            [{
                "text": f"{emoji_about}About modules", 
                "callback": self._about_us
            }]
             ], 
                **{"photo": "https://te.legra.ph/file/64bb29a68030e118dfa21.jpg"},
         )
        
    async def _about_us(self, call: InlineCall):
        await call.edit(
            text = self.strings('_about_module'),
       reply_markup=[          
           [
             {
                 "text": self.strings("back"), 
                 "callback": self._back
             },
             {
                "text": self.strings("x"),
                "action": "close"
            },                   
           ]
           ],
       )
    
    async def page_one(self, call: InlineCall):
        await call.edit(
            text = self.config["text_numb_1"],
       reply_markup=[
           [{"text": self.config["button_numb_1"], "callback": self.page_one}, {"text": self.config["button_numb_2"], "callback": self.page_two}],
           [{"text": self.config["button_numb_3"], "callback": self.page_three}, {"text": self.config["button_numb_4"], "callback": self.page_four}],
           [{
                 "text": self.strings("x"), 
                 "action": "close"
           }]],
           **{"photo": self.config["banner_numb_1"]},
       )
       
    async def page_two(self, call: InlineCall):
        await call.edit(
            text = self.config["text_numb_2"],
       reply_markup=[
           [{"text": self.config["button_numb_1"], "callback": self.page_one}, {"text": self.config["button_numb_2"], "callback": self.page_two}],
           [{"text": self.config["button_numb_3"], "callback": self.page_three}, {"text": self.config["button_numb_4"], "callback": self.page_four}],
           [{
                 "text": self.strings("x"), 
                 "action": "close"
           }]],
           **{"photo": self.config["banner_numb_2"]},
       )

    async def page_three(self, call: InlineCall):
        await call.edit(
            text = self.config["text_numb_3"],
       reply_markup=[
           [{"text": self.config["button_numb_1"], "callback": self.page_one}, {"text": self.config["button_numb_2"], "callback": self.page_two}],
           [{"text": self.config["button_numb_3"], "callback": self.page_three}, {"text": self.config["button_numb_4"], "callback": self.page_four}],
           [{
                 "text": self.strings("x"), 
                 "action": "close"
           }]],
           **{"photo": self.config["banner_numb_3"]},
       )       
      
    async def page_four(self, call: InlineCall):
        await call.edit(
            text = self.config["text_numb_4"],
       reply_markup=[
           [{"text": self.config["button_numb_1"], "callback": self.page_one}, {"text": self.config["button_numb_2"], "callback": self.page_two}],
           [{"text": self.config["button_numb_3"], "callback": self.page_three}, {"text": self.config["button_numb_4"], "callback": self.page_four}],
           [{
                 "text": self.strings("x"), 
                 "action": "close"
           }]],
           **{"photo": self.config["banner_numb_4"]},
       )       
            
                  
