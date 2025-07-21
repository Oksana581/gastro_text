
from telegram import Bot
from telegram.constants import ParseMode
from config import settings

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)


async def send_post_to_telegram(message, image_url=None, alt_text=None):
    try:
        if image_url:
            await bot.send_photo(
                chat_id=settings.TELEGRAM_CHANNEL_ID,
                photo=image_url,
                caption=message,
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await bot.send_message(
                chat_id=settings.TELEGRAM_CHANNEL_ID,
                text=message,
                parse_mode=ParseMode.MARKDOWN
            )
        print("✅ Повідомлення надіслано в Telegram")
    except Exception as e:
        print(f"❌ Помилка надсилання в Telegram: {e}")