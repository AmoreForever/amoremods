# █ █ ▀ █▄▀ ▄▀█ █▀█ ▀    ▄▀█ ▀█▀ ▄▀█ █▀▄▀█ ▄▀█
# █▀█ █ █ █ █▀█ █▀▄ █ ▄  █▀█  █  █▀█ █ ▀ █ █▀█
#
#              © Copyright 2022
#
#          https://t.me/hikariatama
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://imgur.com/GiibLWW
# meta banner: https://imgur.com/OGkmhtc
# meta developer: @sngscamer | @hikariatama 


import difflib
import inspect
import logging

from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import Message
from ..inline.types import InlineCall
from .. import loader, security, utils

logger = logging.getLogger(__name__)


@loader.tds
class AmoreHelpMod(loader.Module):
    """Help module, made specifically for Hikka with <3"""

    strings = {
        "name": "AmoreHelp",
        "bad_module": "<b>🚫 <b>Module</b> <code>{}</code> <b>not found</b>",
        "single_mod_header": "🌑 <b>{}</b>:",
        "single_cmd": "\n▫️ <code>{}{}</code> {}",
        "undoc_cmd": "🦥 No docs",
        "all_header": "🌐 <b>{} mods available, {} hidden:</b>",
        "mod_tmpl": "\n{} <code>{}</code>",
        "first_cmd_tmpl": ": ( {}",
        "cmd_tmpl": " | {}",
        "no_mod": "🚫 <b>Specify module to hide</b>",
        "hidden_shown": "🌘 <b>{} modules hidden, {} modules shown:</b>\n{}\n{}",
        "ihandler": "\n🎹 <code>{}</code> {}",
        "undoc_ihandler": "🦥 No docs",
        "partial_load": "⚠️ <b>Userbot is not fully loaded, so not all modules are shown</b>",
        "not_exact": "⚠️ <b>No exact match occured, so the closest result is shown instead</b>",
    }

    strings_ru = {
        "bad_module": "<b>🚫 <b>Модуль</b> <code>{}</code> <b>не найден</b>",
        "single_mod_header": "🌑 <b>{}</b>:",
        "single_cmd": "\n▫️ <code>{}{}</code> {}",
        "undoc_cmd": "🦥 Нет описания",
        "all_header": "⭐ <b>{} модулей доступно, {} скрыто:</b>",
        "mod_tmpl": "\n{} <code>{}</code>",
        "first_cmd_tmpl": ": [ {}",
        "cmd_tmpl": " | {}",
        "no_mod": "🚫 <b>Укажи модуль(-и), которые нужно скрыть</b>",
        "hidden_shown": "🌐 <b>{} модулей скрыто, {} модулей показано:</b>\n{}\n{}",
        "ihandler": "\n🎹 <code>{}</code> {}",
        "undoc_ihandler": "🦥 Нет описания",
        "_cmd_doc_helphide": "<модуль(-и)> - Скрывает модуль(-и) из помощи\n*Разделяй имена модулей пробелами",
        "_cmd_doc_help": "[модуль] [-f] - Показывает помощь",
        "_cmd_doc_support": "Вступает в чат помощи Hikka",
        "_cls_doc": "Модуль помощи, сделанный специально для Hikka <3",
        "partial_load": "⚠️ <b>Юзербот еще не загрузился полностью, поэтому показаны не все модули</b>",
        "not_exact": "⚠️ <b>Точного совпадения не нашлось, поэтому было выбрано наиболее подходящее</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "core_emoji",
                "▪️",
                lambda: "Core module bullet",
                validator=loader.validators.String(length=1),
            ),
            loader.ConfigValue(
                "hikka_emoji",
                "🧑‍🎤",
                lambda: "Hikka-only module bullet",
                validator=loader.validators.String(length=1),
            ),
            loader.ConfigValue(
                "plain_emoji",
                "▫️",
                lambda: "Plain module bullet",
                validator=loader.validators.String(length=1),
            ),
            loader.ConfigValue(
                "empty_emoji",
                "👁‍🗨",
                lambda: "Empty modules bullet",
                validator=loader.validators.String(length=1),
            ),
        )

    async def modhelp(self, message: Message, args: str):
        exact = True

        try:
            module = next(
                mod
                for mod in self.allmodules.modules
                if mod.strings("name").lower() == args.lower()
            )
        except Exception:
            module = None

        if not module:
            args = args.lower()
            args = args[1:] if args.startswith(self.get_prefix()) else args
            if args in self.allmodules.commands:
                module = self.allmodules.commands[args].__self__

        if not module:
            module_name = next(  # skipcq: PTC-W0063
                reversed(
                    sorted(
                        [module.strings["name"] for module in self.allmodules.modules],
                        key=lambda x: difflib.SequenceMatcher(
                            None,
                            args.lower(),
                            x,
                        ).ratio(),
                    )
                )
            )

            module = next(  # skipcq: PTC-W0063
                module
                for module in self.allmodules.modules
                if module.strings["name"] == module_name
            )

            exact = False

        try:
            name = module.strings("name")
        except KeyError:
            name = getattr(module, "name", "ERROR")

        reply = self.strings("single_mod_header").format(utils.escape_html(name))
        if module.__doc__:
            reply += "<i>\nℹ️ " + utils.escape_html(inspect.getdoc(module)) + "\n</i>"

        commands = {
            name: func
            for name, func in module.commands.items()
            if await self.allmodules.check_security(message, func)
        }

        if hasattr(module, "inline_handlers"):
            for name, fun in module.inline_handlers.items():
                reply += self.strings("ihandler").format(
                    f"@{self.inline.bot_username} {name}",
                    (
                        utils.escape_html(inspect.getdoc(fun))
                        if fun.__doc__
                        else self.strings("undoc_ihandler")
                    ),
                )

        for name, fun in commands.items():
            reply += self.strings("single_cmd").format(
                self.get_prefix(),
                name,
                (
                    utils.escape_html(inspect.getdoc(fun))
                    if fun.__doc__
                    else self.strings("undoc_cmd")
                ),
            )

        await utils.answer(
            message, f"{reply}\n\n{self.strings('not_exact') if not exact else ''}"
        )
        

    @loader.owner
    async def ihelpcmd(self, message: Message):
        """[module] [-f] - Show help"""
        args = utils.get_args_raw(message)
        force = False
        if "-f" in args:
            args = args.replace(" -f", "").replace("-f", "")
            force = True

        if args:
            await self.modhelp(message, args)
            return

        count = 0
        for i in self.allmodules.modules:
            try:
                if i.commands or i.inline_handlers:
                    count += 1
            except Exception:
                pass

        hidden = self.get("hide", [])

        reply = self.strings("all_header").format(
            count,
            len(hidden) if not force else 0,
        )
        shown_warn = False

        plain_ = []
        core_ = []
        inline_ = []
        no_commands_ = []

        for mod in self.allmodules.modules:
            if not hasattr(mod, "commands"):
                logger.debug(f"Module {mod.__class__.__name__} is not inited yet")
                continue

            if mod.strings["name"] in self.get("hide", []) and not force:
                continue

            tmp = ""

            try:
                name = mod.strings["name"]
            except KeyError:
                name = getattr(mod, "name", "ERROR")

            inline = (
                hasattr(mod, "callback_handlers")
                and mod.callback_handlers
                or hasattr(mod, "inline_handlers")
                and mod.inline_handlers
            )

            if not inline:
                for cmd_ in mod.commands.values():
                    try:
                        inline = "await self.inline.form(" in inspect.getsource(
                            cmd_.__code__
                        )
                    except Exception:
                        pass

            core = mod.__origin__ == "<core>"

            if core:
                emoji = self.config["core_emoji"]
            elif inline:
                emoji = self.config["hikka_emoji"]
            else:
                emoji = self.config["plain_emoji"]

            if (
                not getattr(mod, "commands", None)
                and not getattr(mod, "inline_handlers", None)
                and not getattr(mod, "callback_handlers", None)
            ):
                no_commands_ += [
                    self.strings("mod_tmpl").format(self.config["empty_emoji"], name)
                ]
                continue

            tmp += self.strings("mod_tmpl").format(emoji, name)
            first = True

            commands = [
                name
                for name, func in mod.commands.items()
                if await self.allmodules.check_security(message, func) or force
            ]

            for cmd in commands:
                if first:
                    tmp += self.strings("first_cmd_tmpl").format(cmd)
                    first = False
                else:
                    tmp += self.strings("cmd_tmpl").format(cmd)

            icommands = [
                name
                for name, func in mod.inline_handlers.items()
                if await self.inline.check_inline_security(
                    func=func,
                    user=message.sender_id,
                )
                or force
            ]

            for cmd in icommands:
                if first:
                    tmp += self.strings("first_cmd_tmpl").format(f"🎹 {cmd}")
                    first = False
                else:
                    tmp += self.strings("cmd_tmpl").format(f"🎹 {cmd}")

            if commands or icommands:
                tmp += " ]"
                if core:
                    core_ += [tmp]
                elif inline:
                    inline_ += [tmp]
                else:
                    plain_ += [tmp]
            elif not shown_warn and (mod.commands or mod.inline_handlers):
                reply = f"<i>You have permissions to execute only these commands</i>\n{reply}"
                shown_warn = True

        plain_.sort(key=lambda x: x.split()[1])
        core_.sort(key=lambda x: x.split()[1])
        inline_.sort(key=lambda x: x.split()[1])
        no_commands_.sort(key=lambda x: x.split()[1])
        no_commands_ = "\n".join(no_commands_) if force else ""

        partial_load = (
            f"\n\n{self.strings('partial_load')}"
            if not self.lookup("Loader")._fully_loaded
            else ""
        )

        await self.inline.form(  text = f"{reply}\n{''.join(core_)}{''.join(plain_)}{''.join(inline_)}{no_commands_}{partial_load}\n\n<i>🧳 Modern help menu </i>", reply_markup=[  [{"text": "🧑‍🔧 Support", "callback": self.amore,}, {"text": "🌳 Mods", "url": "https://t.me/amoremods"}],   [{"text": "🔻 Close", "action": "close"}],   ],  message=message,   )
                
    async def amore(self, call: InlineCall) -> None:           
           await call.edit(
			text=f'<b>🌳 Need help? Feel free to join our support chat. We help everyone.</b>',
			reply_markup=[
				[
					{
						"text": "🧑‍🔧 Support",
						"url": "https://t.me/hikka_talks",
					},
				],
				[{"text": "закрыть","action": "close"}],
			],
		)
  
  
