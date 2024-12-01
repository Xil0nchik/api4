import requests
import datetime
import os
from dotenv import load_dotenv
import download


def get_epic_images(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    count = 30
    payload = {"count": count, "api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for epic_images in response.json():
        epic_name = epic_images["image"]
        epic_date = epic_images["date"]
        epic_date = datetime.datetime.fromisoformat(epic_date).strftime("%Y/%m/%d")
        epic_link = f"https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_name}.png?api_key={api_key}"
        path = f"images/{epic_name}.png"
        download.download(path, epic_link)


def main():
    load_dotenv()
    api_key = os.environ["NASA_TOKEN"]
    get_epic_images(api_key)


if __name__ == "__main__":
    main()
