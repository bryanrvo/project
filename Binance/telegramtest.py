import json 
import requests
import time

import os
if os.name == 'nt':
    import sys
    # append current python modules' folder path
    # example: need to import module.py present in '/path/to/python/module/not/in/syspath'
    sys.path.append('C:\\Users\\bryan\\Documents')

from APIcode import TOKEN
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    

def main():
    last_textchat = (None, None)
    while True:
        text, chat = get_last_chat_id_and_text(get_updates())
        text = 'hoi'
        send_message(text, chat)
        time.sleep(0.5)


if __name__ == '__main__':
    main()