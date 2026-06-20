import requests
import os
import time
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

START_URL = "https://en.wikipedia.org/wiki/Special:Random"
SAVE_FOLDER = "crawler_data"
MAX_SIZE = 4 * 1024 * 1024  # 4MB

os.makedirs(SAVE_FOLDER, exist_ok=True)

visited = set()

def file_size():
    total = 0
    for root, dirs, files in os.walk(SAVE_FOLDER):
        for f in files:
            total += os.path.getsize(os.path.join(root, f))
    return total

def save_html(html, index):
    path = f"{SAVE_FOLDER}/page_{index}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[+] Saved {path}")

def get_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for a in soup.find_all("a", href=True):
        url = urljoin(base_url, a["href"])
        parsed = urlparse(url)

        # نفلتر فقط روابط ويكيبيديا
        if "wikipedia.org" in parsed.netloc:
            links.append(url)

    return links

def crawl():
    current_url = START_URL
    index = 0

    print("Crawler started 🚀")

    while True:
        if file_size() >= MAX_SIZE:
            print("\n⚠️ 4MB reached. Stopping crawler.")
            break

        if current_url in visited:
            current_url = START_URL
            continue

        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            r = requests.get(current_url, headers=headers, timeout=10)

            if r.status_code != 200:
                continue

            html = r.text
            visited.add(current_url)

            save_html(html, index)
            index += 1

            links = get_links(html, current_url)

            if links:
                current_url = random.choice(links)

            time.sleep(1)  # احترام السيرفر

        except Exception as e:
            print("Error:", e)
            current_url = START_URL

if __name__ == "__main__":
    crawl()
