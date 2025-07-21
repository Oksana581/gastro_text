# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

WEBSITE_URLS = {
    "NASPGHAN": "https://naspghan.org ",
    "Gastro.org": "https://www.gastro.org ",
    "Medscape Gastroenterology": "https://www.medscape.com/gastroenterology "
}