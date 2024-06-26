# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# requires: bs4 cloudscraper loguru tqdm lxml

# meta developer: @hikamorumods


import os
import pathlib
import shutil

import string
import random
import logging

from tqdm import tqdm
from dataclasses import dataclass

from bs4 import BeautifulSoup
from cloudscraper import create_scraper, CloudScraper
from telethon.tl.types import DocumentAttributeVideo

from aiogram.types import CallbackQuery

from .. import loader, utils


logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
}


@dataclass
class Season:
    title: str
    episodes_urls: list[str]


def download_video(url: str, path, scraper: CloudScraper):
    with scraper.get(url, stream=True) as r:
        total_length = int(r.headers.get("Content-Length"))
        with tqdm.wrapattr(r.raw, "read", total=total_length, desc="") as raw:
            with open(path, "wb") as file:
                shutil.copyfileobj(raw, file)


def remove_symbols(filename: str) -> str:
    if not filename:
        return filename

    forbidden = '\\/*:?|"<>'
    for symbol in forbidden:
        filename.replace(symbol, "")
    return filename


class JutSuD:
    def loader(self, anime_url, season_from, episode_from, season_to, episode_to):
        scraper = create_scraper(
            delay=1,
            browser={
                "custom": "ScraperBot/1.0",
            },
        )

        response = scraper.get(anime_url)
        soup = BeautifulSoup(response.text, "lxml")

        anime_title = soup.find("h1", {"class": "anime_padding_for_title"}).text
        anime_title = (
            anime_title.replace("Смотреть", "")
            .replace("все серии", "")
            .replace("и сезоны", "")
            .strip()
        )

        seasons = [
            Season(
                title=season_title.text,
                episodes_urls=[],
            )
            for season_title in soup.find_all("h2", class_=["the-anime-season"])
        ]

        if not seasons:
            seasons.append(
                Season(
                    title=anime_title,
                    episodes_urls=[],
                )
            )

        episodes_soup = soup.find_all(
            "a",
            class_=[
                "short-btn black video the_hildi",
                "short-btn green video the_hildi",
            ],
        )

        current_season_index = -1
        current_episode_class = None

        for ep in episodes_soup:
            if ep["class"] != current_episode_class:
                current_episode_class = ep["class"]

                current_season_index += 1

            url = "https://jut.su" + ep["href"]
            seasons[current_season_index].episodes_urls.append(url)

        for i, season in enumerate(seasons):
            season_number = i + 1

            if season_number < season_from or season_number > season_to:
                continue

            for j, episode_url in enumerate(season.episodes_urls):
                episode_number = j + 1

                if (season_number == season_from and episode_number < episode_from) or (
                    (season_number == season_to or season_number == len(seasons))
                    and episode_number > episode_to
                ):
                    continue

                response = scraper.get(episode_url)
                soup = BeautifulSoup(response.content, "lxml")

                try:
                    episode_title = (
                        soup.find("div", {"class": "video_plate_title"}).find("h2").text
                    )

                except AttributeError:
                    episode_title = soup.find("span", {"itemprop": "name"}).text
                    episode_title = (
                        episode_title.replace("Смотреть", "")
                        .replace(anime_title, "")
                        .strip()
                    )

                video_url = soup.find("source")["src"]

                name_video = random.choices("".join(string.ascii_letters), k=10)
                video_path = pathlib.Path(f"{''.join(name_video)}.mp4")
                episode_slug = f"{season.title} - {episode_title} [#{episode_number}]"
                try:
                    download_video(url=video_url, path=video_path, scraper=scraper)
                    return video_path, episode_slug
                except Exception as e:
                    logger.exception(e)
                    return False, False

    def get_info(self, url):
        scraper = create_scraper()
        response = scraper.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "lxml")

        anime_title = soup.find("h1", {"class": "anime_padding_for_title"}).text

        anime_title = (
            anime_title.replace("Смотреть", "")
            .replace("все серии", "")
            .replace("и сезоны", "")
            .strip()
        )

        seasons = [
            Season(
                title=season_title,
                episodes_urls=[],
            )
            for season_title in soup.find_all("h2", class_=["the-anime-season"])
        ]

        if not seasons:
            seasons.append(
                Season(
                    title=anime_title,
                    episodes_urls=[],
                )
            )

        episodes_soup = soup.find_all(
            "a",
            class_=[
                "short-btn black video the_hildi",
                "short-btn green video the_hildi",
            ],
        )
        return anime_title, seasons, episodes_soup


@loader.tds
class Jutsu(loader.Module):
    """Download and get info about anime from jut.su"""

    strings = {
        "name": "Jutsu",
        "info": (
            "📺 <b>Anime info</b>\n\n"
            "<b>Title:</b> {}\n"
            "<b>Seasons:</b> {}\n"
            "<b>Total episodes:</b> {}\n"
            "<b>Link:</b> {}"
        ),
        "download_button": "📥 Download",
        "done": "✅ Download completed!",
        "choose_season": "📺 <b>Choose season</b>",
        "choose_episode": "🪶 <b>Choose episode</b>",
        "wrong_url": "❌ Wrong url!",
        "no_args": "❌ No args!",
        "download": "📥 Downloading episode {}... (speed depends on your internet connection)",
        "close": "❌ Close",
    }

    strings_ru = {
        "info": (
            "📺 <b>Информация о аниме</b>\n\n"
            "<b>Название:</b> {}\n"
            "<b>Сезонов:</b> {}\n"
            "<b>Всего серий:</b> {}\n"
            "<b>Ссылка:</b> {}"
        ),
        "download_button": "📥 Скачать",
        "done": "✅ Скачивание завершено!",
        "choose_season": "📺 <b>Выберите сезон</b>",
        "choose_episode": "🪶 <b>Выберите серию</b>",
        "wrong_url": "❌ Неверная ссылка!",
        "no_args": "❌ Нет аргументов!",
        "download": "📥 Скачиваем серию {}... (скорость скачивание зависит от вашего интернета)",
        "close": "❌ Закрыть",
    }
    
    async def client_ready(self, client, db):
        asset_ch, _ = await utils.asset_channel(
            self._client,
            "JutSu downloads",
            "Downloaded anime from JutSu will be sent here. (Hikamoru back?)",
            avatar="https://i.pinimg.com/564x/0a/da/0b/0ada0bb575146736679f5ea7a78971b8.jpg",
        )
        self.chid = int(f"-100{asset_ch.id}")
        

    async def download_(self, call, url, seasons, episodes_soup):
        seasons = [season for season in range(1, len(seasons) + 1)]

        kb = []

        for mod_row in utils.chunks(seasons, 3):
            row = [
                {
                    "text": f"• {season} •",
                    "callback": self.season_,
                    "args": (season, episodes_soup, url),
                }
                for season in mod_row
            ]

            kb += [row]

        await call.edit(self.strings["choose_season"], reply_markup=kb)

    async def season_(self, call, season, eps, url):
        episodes = [episode for episode in range(1, len(eps) + 1)]

        kb = []

        for mod_row in utils.chunks(episodes, 3):
            row = [
                {
                    "text": f"• {episode} •",
                    "callback": self.episod_,
                    "args": (episode, season, url),
                }
                for episode in mod_row
            ]

            kb += [row]

        await call.edit(self.strings["choose_episode"], reply_markup=kb)

    async def episod_(self, call: CallbackQuery, episode, episode_number, url):
        await call.edit(self.strings["download"].format(episode_number))

        try:
            name, title = JutSuD().loader(
            url, episode_number, episode, episode_number, episode
            )
        except TypeError:
            await call.edit("There is not such a episode (This bug with button will be fixed soon)")

        await self.client.send_file(
            self.chid,
            open(name, "rb"),
            caption=self.strings["done"] + f"\n\n{title}",
            filetype="video",
            attributes=(DocumentAttributeVideo(0, 0, 0),),
        )

        await call.edit(self.strings["done"])

        os.remove(name)

    async def close_(self, call):
        await call.delete()

    @loader.command()
    async def jutsud(self, message):
        """Download anime from jutsu - [url]"""

        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(message, self.strings["no_args"])
            return

        if not args.startswith("https://jut.su"):
            await utils.answer(message, self.strings["wrong_url"])
            return

        anime_title, seasons, episodes_soup = JutSuD().get_info(args)

        await utils.answer(
            message,
            self.strings["info"].format(
                anime_title, len(seasons), len(episodes_soup), args
            ),
            reply_markup=[
                [
                    {
                        "text": self.strings["download_button"],
                        "callback": self.download_,
                        "kwargs": {
                            "url": args,
                            "seasons": seasons,
                            "episodes_soup": episodes_soup,
                        },
                    },
                    {
                        "text": self.strings["close"],
                        "callback": self.close_,
                    },
                ]
            ],
        )