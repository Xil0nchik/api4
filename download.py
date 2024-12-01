import requests
import os


def download(filename, url):
    os.makedirs("images", exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as file:
        file.write(response.content)
