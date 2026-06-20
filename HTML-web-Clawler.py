import requests
from urllib.parse import urlparse

def save_html(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        html_content = response.text

        # استخراج اسم الموقع
        parsed = urlparse(url)
        filename = parsed.netloc.replace(".", "_") + ".html"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"[+] تم حفظ HTML في: {filename}")

    except Exception as e:
        print(f"[-] خطأ: {e}")

if __name__ == "__main__":
    url = input("Put ur URL here: ")
    save_html(url)
