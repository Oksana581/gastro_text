
import aiohttp
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0'}


async def get_website_content(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=HEADERS, timeout=15) as response:
                response.raise_for_status()
                return await response.text()
    except Exception as e:
        print(f"❌ Помилка при завантаженні {url}: {e}")
        return None


def parse_for_keywords(html_content):
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    keywords = [
        "pediatric gastroenterology", "child", "children", "infant", "toddler",
        "gastroenterology", "digestive health", "bowel", "stomach", "intestine"
    ]
    relevant = []

    for tag in soup.find_all(['p', 'h1', 'h2', 'h3']):
        text = tag.get_text().lower()
        if any(keyword in text for keyword in keywords):
            relevant.append(text.strip())

    return relevant[:50]


async def scrape_all_sites(urls):
    all_text = []
    for name, url in urls.items():
        print(f"🌐 Збір даних з {name} — {url}")
        html = await get_website_content(url)
        if html:
            fragments = parse_for_keywords(html)
            all_text.extend(fragments)
    return " ".join(all_text)