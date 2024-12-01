import requests
import os
from dotenv import load_dotenv
import download
import urllib.parse


def get_extension(url):
    decoded_link = urllib.parse.unquote(url)
    parced_link = urllib.parse.urlparse(decoded_link)
    path, fullname = os.path.split(parced_link.path)
    filename, extension = os.path.splitext(fullname)
    return filename, extension


def get_apod_images(api_key):
    url = "https://api.nasa.gov/planetary/apod"
    count = 30
    payload = {"count": count, "api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for appod_images in response.json():
        if appod_images.get("media_type") == "image":
            nassa_link_image = appod_images["hdurl"] or appod_images["url"]
        filename, extension = get_extension(nassa_link_image)
        path = f"images/apod_{filename}{extension}"
        download.download(path, nassa_link_image)


def main():
    load_dotenv()
    api_key = os.environ["NASA_TOKEN"]
    get_apod_images(api_key)


if __name__ == "__main__":
    main()
