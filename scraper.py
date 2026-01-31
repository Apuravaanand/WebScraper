import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_data(url, choice):
    res = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(res.text, "html.parser")

    data = []

    if choice == "Title":
        if soup.title:
            data.append(soup.title.text.strip())

    elif choice == "Headings":
        for tag in soup.find_all(["h1", "h2", "h3"]):
            data.append(tag.text.strip())

    elif choice == "Links":
        for a in soup.find_all("a", href=True):
            if a["href"].startswith("http"):
                data.append(a["href"])

    elif choice == "Images":
        for img in soup.find_all("img"):
            src = img.get("src")
            if src and src.startswith("http") and not src.endswith(".svg"):
                data.append(src)

    elif choice == "All":
        return {
            "Title": scrape_data(url, "Title"),
            "Headings": scrape_data(url, "Headings"),
            "Links": scrape_data(url, "Links"),
            "Images": scrape_data(url, "Images")
        }

    return list(set(data))
