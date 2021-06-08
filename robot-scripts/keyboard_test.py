import keyboard
import string
from threading import *


keys = list(string.ascii_lowercase)


def listen(key):
    while True:
        keyboard.wait(key)
        print("[+] Pressed",key)


if __name__ == '__main__':
    threads = [Thread(target=listen, kwargs={"key":key}) for key in keys]
    for thread in threads:
        thread.start()
