#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 20463124
API_HASH = "350a22b1737da55b4a173685f135235a"
BOT_TOKEN = "7553824556:AAEwzFzBNBA6bUSA9nl3gtCvtC59uafU17Y"
SESSION = "BQE4PhQAMYKSfkQ03zjbAYALcJS7mjNo1g7yko-e725UfvR-8fxZmNMkqXNFukLCYjOegtUIpqDGAtpyzznosWg25S91mOzbEHWmmtvnaPK-vxEy4dG3xR6nG2X2aWF72vt0TEpwvYz7EICXOURdep0YoooT5sKQqRz0VytPO0F-31dFl4bQ45mk9TGLff-BWT0Rq1Q64S37EljMbZVP5eJWoYzm9f4kpNRc-dewzSvO_K3jTMBYKKIOd4vVOvU6DFfsTqLqS2sKqyX0x2nLeEcCfTss4G_cbmNLlXXrSse6o2BNyGg3lyioR69R0iWos-KSn8o2mdsDzM5VxlgNXp9Rq1QXWAAAAAHCPjcsAQ"
FORCESUB = "xiaoxitiqu233"
AUTH = 1599971012

# bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
bot = TelegramClient('bot', API_ID, API_HASH)
bot.start(bot_token=BOT_TOKEN)
userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
