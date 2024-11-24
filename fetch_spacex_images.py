import argparse
import requests
import download


def fetch_spacex_last_launch(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"

    response = requests.get(url)
    response.raise_for_status()
    spacex_links = response.json()["links"]["flickr"]["original"]

    for number, link in enumerate(spacex_links):
        download.download(f"images/spacex{number}.jpg", link)


def main():
    parser = argparse.ArgumentParser(description="Fetch images from spacex")
    parser.add_argument(
        "--launch_id", help="Spacex launch ID", default="5eb87d47ffd86e000604b38a"
    )
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)


if __name__ == "__main__":
    main()
