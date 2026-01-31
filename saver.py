import os
import requests
from pathlib import Path

def create_project_folder(folder_name):
    downloads = Path.home() / "Downloads"
    project_folder = downloads / folder_name
    project_folder.mkdir(exist_ok=True)
    return project_folder

def save_text(data, folder, filename):
    path = folder / filename
    with open(path, "w", encoding="utf-8") as f:
        if isinstance(data, list):
            f.write("\n".join(data))
        else:
            f.write(str(data))

def save_images(image_urls, folder):
    img_folder = folder / "images"
    img_folder.mkdir(exist_ok=True)

    for i, url in enumerate(image_urls, start=1):
        try:
            r = requests.get(url, timeout=10)
            ext = url.split(".")[-1].split("?")[0]
            if ext not in ["jpg", "png", "jpeg", "webp"]:
                ext = "jpg"

            with open(img_folder / f"img_{i}.{ext}", "wb") as f:
                f.write(r.content)
        except:
            continue
