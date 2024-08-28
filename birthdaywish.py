# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods

import re
import asyncio
import random
from aiohttp import web
from .. import utils, loader


class WebCreator:
    def __init__(self, name, tg_link, preview_name):
        self.url = None
        self.app = web.Application()
        self.app.router.add_get("/", self.index)
        self.name = name
        self.tg_link = tg_link
        self.preview_name = preview_name

    async def index(self, request):
        html_content = f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <title>For {self.name}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1"></script>
</head>

<style>
    body {{
        margin: 0;
        text-align: center;
        background: #1d1d1d;
        font: 22px 'Indie Flower', cursive, "Helvetica Neue", Helvetica, Arial, sans-serif;
        color: #fff;
        overflow-x: hidden;
    }}

    #content {{
        position: relative;
        max-width: 470px;
        margin: 0 auto;
        line-height: 150%;
        padding: 20px;
        z-index: 1;
    }}

    h1 {{
        font-size: 2.5rem;
        color: #f7d066;
        margin-top: 50px;
    }}

    p {{
        font-size: 1.2rem;
        margin-top: 20px;
    }}

    span {{
        color: #f7467e;
    }}

    @media (max-width: 767px) {{
        #content {{
            max-width: 100%;
            padding: 10px;
        }}
    }}
</style>

<body>
    <div id="content">
        <h1>Happy Birthday, {self.name}!</h1>
        <p>Dear {self.name},<br>
            On this special day, I wish you all the very best, all the joy you can ever have, and may you be blessed
            abundantly today, tomorrow, and the days to come! May you have a fantastic birthday and many more to come...
            HAPPY BIRTHDAY!!!!<br>
            <span>With love, <a href="{self.tg_link}">{self.preview_name}</a></span>
        </p>
    </div>

    <script>
        function launchConfetti() {{
            const duration = 2 * 1000;
            const end = Date.now() + duration;

            (function frame() {{
                confetti({{
                    particleCount: 5,
                    angle: 60,
                    spread: 55,
                    origin: {{ x: 0 }},
                    colors: ['#f7d066', '#f7467e', '#fff']
                }});
                confetti({{
                    particleCount: 5,
                    angle: 120,
                    spread: 55,
                    origin: {{ x: 1 }},
                    colors: ['#f7d066', '#f7467e', '#fff']
                }});

                if (Date.now() < end) {{
                    requestAnimationFrame(frame);
                }}
            }})();
        }}

        window.onload = launchConfetti;
    </script>
</body>

</html>
"""

        return web.Response(text=html_content, content_type="text/html")

    async def open_tunnel(self, port):
        ssh_command = f"ssh -o StrictHostKeyChecking=no -R 80:localhost:{port} nokey@localhost.run"
        process = await asyncio.create_subprocess_shell(
            ssh_command,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        url = await self._extract_tunnel_url(process.stdout)
        self.url = url or f"https://localhost:{port}"
        return self.url

    async def _extract_tunnel_url(self, stdout):
        event = asyncio.Event()
        url = None

        async def read_output():
            nonlocal url
            while True:
                line = await stdout.readline()
                if not line:
                    break
                decoded_line = line.decode()
                match = re.search(r"tunneled.*?(https:\/\/.+)", decoded_line)
                if match:
                    url = match[1]
                    break
            event.set()

        await read_output()
        await event.wait()
        return url


@loader.tds
class BirthdayWish(loader.Module):
    """Share warmth with your loved ones and give them this website to make their birthdays even more special and joyful."""

    strings = {
        "name": "BirthdayWish",
        "provide_name": "<emoji document_id=5456652110143693064>🤷‍♂️</emoji> <b>Please provide a name</b>",
        "web_url": "<emoji document_id=5334643333488713810>🌐</emoji> <b>URL: {} | Expires in <code>{}</code> seconds</b>",
        "expired": "<emoji document_id=5981043230160981261>⏱</emoji> <b>Url Expired</b>",
    }

    strings_ru = {
        "provide_name": "<emoji document_id=5456652110143693064>🤷‍♂️</emoji> <b>Пожалуйста, укажите имя</b>",
        "web_url": "<emoji document_id=5334643333488713810>🌐</emoji> <b>URL: {} | Истекает через <code>{}</code> секунд</b>",
        "expired": "<emoji document_id=5981043230160981261>⏱</emoji> <b>Url истек</b>",
    }

    def __init__(self):
        self.wishes = {}

    async def tunnel_handler(self, port):

        creator = WebCreator(
            name=self.name, tg_link=self.tg_link, preview_name=self.preview_name
        )

        runner = web.AppRunner(creator.app)
        await runner.setup()

        global site
        site = web.TCPSite(runner, "127.0.0.1", port)
        await site.start()

        url = await creator.open_tunnel(port)
        return url, runner

    async def wishcmd(self, message):
        """Create Birthday web wishes args: <name> <time:seconds default(20)>"""

        args = utils.get_args_raw(message).split(" ")

        if args[0] == "":
            return await utils.answer(message, self.strings("provide_name"))

        text = args[0]

        expiration_time = int(args[1]) if len(args) > 1 else 20

        me = await message.client.get_me()
        
        self.tg_link = f"https://t.me/{me.username}" or "https://t.me/Unknown"
        self.preview_name = me.first_name
        self.name = text

        port = random.randint(1000, 9999)
        
        url, runner = await self.tunnel_handler(port)
        await utils.answer(
            message, self.strings("web_url").format(url, expiration_time)
        )

        await asyncio.sleep(expiration_time)

        await site.stop()
        await runner.cleanup()

        await utils.answer(message, self.strings("expired"))
