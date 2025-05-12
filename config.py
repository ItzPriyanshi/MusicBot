import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("23497256"))
API_HASH = getenv("9b55ac125b107ef2a544b520aeca0823")
BOT_TOKEN = getenv("7665256594:AAHqDwAKy0IzDTjA13-wgnNPv22CxtS8g9E")
MONGO_DB_URI = getenv("mongodb+srv://priyanshikaurji:priyanshikaurji@cluster0.kcbnt.mongodb.net/TeleBot?retryWrites=true&w=majority&appName=Cluster0", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOGGER_ID = int(getenv("-1002474197899", None))
OWNER_ID = int(getenv("6388959089", None))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("https://t.me/GlobalUpdateQueen")
SUPPORT_CHAT = getenv("https://t.me/GlobalChatGroupTG")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("41dd52e608ee4c4ba8b196b943db9f73", None)
SPOTIFY_CLIENT_SECRET = getenv("5c7b438712b04d0a9fe2eaae6072fa16", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = int(getenv("1BVtsOKEBuyUaKHiB6H-KHtLwAwUKitAYWNE35KQzEedaoniWxYIXfH4uswuUb8lPxlAYxHSW7wkTts_LEJqdAOO_QYkAbSupL84zR8fKlr1Lj2PXtc4c0fJ9Zd3mE4YD9c0Bjx2bOe0tEoWvAS35B4_TW_JYA86-IzAe_1okrFiBxL5R9L_tAziI9X-IibNnMYDa2Y5-FNnV6WRKLtz2T40FZ7t6SO9y-bTlw7b23iPUTZjaLp99-nHKM7gZUkNtUMt0NMwYkCW4JtRBSRtnYCckLYAZscWuuxe7iGGFECdO0Q3RzWxadFXMpsY6mjIYgb6e0F_qn0ypaytPng5CjKaI-yiJbTE=", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/2dve48"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/2dve48"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/2dve48"
STATS_IMG_URL = "https://files.catbox.moe/2dve48"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2dve48"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2dve48"
STREAM_IMG_URL = "https://files.catbox.moe/2dve48"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/2dve48"
YOUTUBE_IMG_URL = "https://files.catbox.moe/2dve48"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2dve48"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2dve48"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/2dve48"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
