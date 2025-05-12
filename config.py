import re
from pyrogram import filters

API_ID = 23497256
API_HASH = "9b55ac125b107ef2a544b520aeca0823"
BOT_TOKEN = "7665256594:AAHqDwAKy0IzDTjA13-wgnNPv22CxtS8g9E"
MONGO_DB_URI = "mongodb+srv://priyanshikaurji:priyanshikaurji@cluster0.kcbnt.mongodb.net/TeleBot?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = 60
LOGGER_ID = -1002474197899
OWNER_ID = 6388959089

HEROKU_APP_NAME = None
HEROKU_API_KEY = None

UPSTREAM_REPO = "https://github.com/AnonymousX1025/AnonXMusic"
UPSTREAM_BRANCH = "master"
GIT_TOKEN = None

SUPPORT_CHANNEL = "https://t.me/GlobalUpdateQueen"
SUPPORT_CHAT = "https://t.me/GlobalChatGroupTG"

AUTO_LEAVING_ASSISTANT = False

SPOTIFY_CLIENT_ID = "41dd52e608ee4c4ba8b196b943db9f73"
SPOTIFY_CLIENT_SECRET = "5c7b438712b04d0a9fe2eaae6072fa16"

PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 104857600
TG_VIDEO_FILESIZE_LIMIT = 1073741824

STRING1 = "1BVtsOKEBuyUaKHiB6H-KHtLwAwUKitAYWNE35KQzEedaoniWxYIXfH4uswuUb8lPxlAYxHSW7wkTts_LEJqdAOO_QYkAbSupL84zR8fKlr1Lj2PXtc4c0fJ9Zd3mE4YD9c0Bjx2bOe0tEoWvAS35B4_TW_JYA86-IzAe_1okrFiBxL5R9L_tAziI9X-IibNnMYDa2Y5-FNnV6WRKLtz2T40FZ7t6SO9y-bTlw7b23iPUTZjaLp99-nHKM7gZUkNtUMt0NMwYkCW4JtRBSRtnYCckLYAZscWuuxe7iGGFECdO0Q3RzWxadFXMpsY6mjIYgb6e0F_qn0ypaytPng5CjKaI-yiJbTE="
STRING2 = None
STRING3 = None
STRING4 = None
STRING5 = None

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = "https://files.catbox.moe/2dve48"
PING_IMG_URL = "https://files.catbox.moe/2dve48"
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
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://")

if SUPPORT_CHAT:
    if not re.match(r"(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://")