from telethon import TelegramClient, events
import config
from handlers import getpay

# Inisialisasi Userbot
bot = TelegramClient("userbot", config.API_ID, config.API_HASH)

print("Userbot getpay sedang berjalan...")

bot.run_until_disconnected()