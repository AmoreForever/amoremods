__version__ = (1, 1, 0)
#            ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#            █▀█ █░▀░█ █▄█ █▀▄ ██▄
#
#              © Copyright 2022
#
#         https://t.me/the_farkhodov
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html


# meta developer: @amoremods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Premiuminfo.jpg
# version : 1.1.0 beta


import git
import logging
from telethon.utils import get_display_name

from .. import loader, main, utils

logger = logging.getLogger(__name__)

@loader.tds
class PremiumInfoMod(loader.Module):
    """Premium emoji info by amore <3"""
    strings = {
        "name": "PremiumInfo",
        "own": (
            "<emoji document_id=6048540195995782913>👤</emoji> Owner"
        ),
        "ver": (
            "<emoji document_id=6050744746874244036>ℹ️</emoji> Version"
        ),
        "upt": (
            "<emoji document_id=5764783998945464490>⏲</emoji> Uptime"
        ),
        "pref": (
            "<emoji document_id=6041858261970324774>💬</emoji> Prefix"
        ),
        "up-to-date":(
             "<emoji document_id=5776414066008395465>📊</emoji> Actual version"
        ),
        "update_required":(
             "<emoji document_id=5776235811980709241>📊</emoji> Outdated version </b><code>.update</code><b>",
        ),
        "_cfg_cst_msg": "Custom message for info. May contain {me}, {version}, {build}, {prefix}, {platform}, {upd}, {uptime} keywords",
    }

    strings_ru = {
        "own": (
            "<emoji document_id=6048540195995782913>👤</emoji> Владелец"
        ),
        "ver": (
            "<emoji document_id=6050744746874244036>ℹ️</emoji> Версия"
        ),
        "upt": (
            "<emoji document_id=5764783998945464490>⏲</emoji> Аптайм"
        ),
        "pref": (
            "<emoji document_id=6041858261970324774>💬</emoji> Префикс"
        ),
        "up-to-date":(
             "<emoji document_id=5776414066008395465>📊</emoji> Актуальная вресия"
        ),
        "update_required":(
             "<emoji document_id=5776235811980709241>📊</emoji> Требуется обновление </b><code>.update</code><b>",
        ),
        "_cfg_cst_msg": "Для кастомизации, ты можешь юзать {me}, {version}, {build}, {prefix}, {platform}, {upd}, {uptime} keywords",

    }
    
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "Media",  
                "https://te.legra.ph/file/4b00eeb4e1b11f28d9ff3.jpg",
                lambda: "Your custom media",
        ),
            loader.ConfigValue(
                "custom_message",  
                "none",
                doc=lambda: self.strings("_cfg_cst_msg"),
        ),
    )

    async def client_ready(self, client, db):
        if not (await self._client.get_me()).premium:
            raise loader.LoadError(
                "⭐️ This module is available only to Telegram Premium subscribers"
            )
        self._db = db
        self._client = client
        self._me = await client.get_me() 


    async def pinfocmd(self, message):
        """Custom emoji info"""
        reply = await message.get_reply_message()

        media = self.config["Media"]

        ver = utils.get_git_hash() or "Unknown"
        try:
            repo = git.Repo()
            diff = repo.git.log(["HEAD..origin/master", "--oneline"])
            upd = (
                self.strings("update_required") if diff else self.strings("up-to-date")
            )
        except Exception:
            upd = ""

        me = f'<b><a href="tg://user?id={self._me.id}">{utils.escape_html(get_display_name(self._me))}</a></b>'
        version = f'<i>{".".join(list(map(str, list(main.__version__))))}</i>'
        build = f'<a href="https://github.com/hikariatama/Hikka/commit/{ver}">#{ver[:8]}</a>'
        prefix = f"«<code>{utils.escape_html(self.get_prefix())}</code>»"
        platform = utils.get_named_platform()
        uptime = utils.formatted_uptime()
        
        hikka = (
            "<b><emoji document_id=5213123182378098899>💨</emoji> Premium info</b>\n"
            + self.config["custom_message"].format(
                me=me,
                version=version,
                build=build,
                upd=upd,
                prefix=prefix,
                platform=platform,
                uptime=uptime,
            )
            if self.config["custom_message"] != "none"
            else (
                "<b><emoji document_id=5213123182378098899>💨</emoji> Premium info</b>\n"
                f"<b>{self.strings('own')}: </b>{me}\n\n"
                f"<b>{self.strings('ver')}: </b>{version} {build}\n"
                f"<b>{upd}</b>\n"
                f"<b>{self.strings('upt')}: {uptime}</b>\n\n"
                f"<b>{self.strings('pref')}: </b>{prefix}\n"
                f"{platform}\n"
            )
        )
            
        await self._client.send_file(
            message.peer_id,
            media,
            caption=hikka,
            link_preview=False,
            reply_to=reply.id if reply else None,
            )
