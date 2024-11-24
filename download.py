import requests
import os


def download(filename, url):
    try:
        os.makedirs("images")
    except FileExistsError:
        pass
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as file:
        file.write(response.content)
