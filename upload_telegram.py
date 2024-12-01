import telegram
import os
import random
from dotenv import load_dotenv
import time


def send_images(chat_id, bot_token):
    bot = telegram.Bot(token=bot_token)
    while True:
        files = os.listdir("images")
        random.shuffle(files)
        for file in files:
            file_path = os.path.join("images", file)
            with open(file_path, "rb") as image:
                bot.send_photo(chat_id=chat_id, photo=image)
            time.sleep(10)


def main():
    load_dotenv()
    chat_id = os.environ["TG_CHAT_ID"]
    bot_token = os.environ["TG_BOT_TOKEN"]
    send_images(chat_id, bot_token)


if __name__ == "__main__":
    main()
