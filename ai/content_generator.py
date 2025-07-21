
import google.generativeai as genai
from config import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')


async def generate_post(text):
    prompt = f"""Проаналізуй наступний медичний текст, отриманий з веб-сайтів гастроентерології.
Створи короткий пост українською мовою, зрозумілий звичайним читачам без медичної освіти.
Структура:
- Заголовок
- Основний текст до 150-200 слів
- Заклик до дії
Текст:
{text[:8000]}
"""

    try:
        post = await model.generate_content_async(prompt)
        if not post.text:
            return None, None, None

        lines = post.text.split('\n')
        title = next((line.strip() for line in lines if line.strip()), text[:50])

        alt_prompt = f"Опиши коротко зображення до теми: {title}"
        alt_response = await model.generate_content_async(alt_prompt)

        image_url = "https://example.com/image_placeholder.png "
        return post.text, image_url, alt_response.text.strip()
    except Exception as e:
        print(f"❌ Помилка при генерації контенту: {e}")
        return None, None, None