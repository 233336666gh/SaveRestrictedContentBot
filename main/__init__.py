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
SESSION = "BQE4PhQAY6k5E1MwBWbl9k7BzJwBP04BJ5AhJ0TN22Y17MWof1KpwdmiqDtfGVfQNvhEEGeFncC50dW2LmpXBXcEaUrrfwjPNOX49wgIJ-dOqNr71eaXYW6V9SoKmzfO4glCb2cdxFWhKqFl9yRkPNuVys9Wri6yhX5I02IC5_6Skmh6E454c1z8SDk-rYhGFUsn27OOnPLAMIAxR1CuVIZeDqkHxTqfGiLqYx4t7K43tFk4w0uFh-_CEm5-L0-yo2whYo2XjYwikULRYzVJRUWjKAoD-WLsP_ykIJ_xN6CyBSG6O35WRyN1HMC_YhAG5KZKUCkelkdj3Lj3G3eejW1SCq4DrAAAAAHCPjcsAQ"
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
