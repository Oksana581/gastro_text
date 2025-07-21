
# main.py
import asyncio
from config import settings
from ai.content_generator import generate_post
from scraping.website_scraper import scrape_all_sites
from telegram.telegram_sender import send_post_to_telegram


async def main():
    print("🔍 Збір даних з медичних сайтів...")
    combined_text = await scrape_all_sites(settings.WEBSITE_URLS)

    if not combined_text:
        await send_post_to_telegram("🚫 Не вдалося зібрати корисну інформацію для створення посту.")
        return

    print("🤖 Генерація посту...")
    post_text, image_url, alt_text = await generate_post(combined_text)

    if not post_text:
        await send_post_to_telegram("🚫 Не вдалося згенерувати пост.")
        return

    print("📤 Відправка в Telegram...")
    await send_post_to_telegram(post_text, image_url, alt_text)
    print("✅ Готово!")


if __name__ == "__main__":
    if not settings.GOOGLE_API_KEY or not settings.TELEGRAM_BOT_TOKEN or not settings.TELEGRAM_CHANNEL_ID:
        print("❌ Не встановлено необхідні змінні оточення у .env")
    else:
        asyncio.run(main())
