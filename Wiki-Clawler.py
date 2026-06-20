import requests
import os

FILE = "wiki_dataset.txt"
MAX_SIZE = 2 * 1024 * 1024  # 2MB

def size():
    if not os.path.exists(FILE):
        return 0
    return os.path.getsize(FILE)

def get_article():
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

    headers = {
        "User-Agent": "Mozilla/5.0 (Educational Bot)"
    }

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()
        title = data.get("title", "")
        text = data.get("extract", "")

        return f"\n\n=== {title} ===\n{text}\n"

    return ""

def save(text):
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(text)

def run():
    print("Wikipedia TXT Collector 🚀")
    print("Stop at 2MB → type 'again' to restart cycle")

    while True:
        if size() >= MAX_SIZE:
            print("\n⚠️ 2MB reached!")
            cmd = input(">>> ")

            if cmd.strip().lower() == "again":
                open(FILE, "w").close()
                print("🔁 New cycle started\n")
            continue

        article = get_article()

        if article:
            save(article)
            print("✔ Added article")

if __name__ == "__main__":
    run()
