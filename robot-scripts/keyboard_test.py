import keyboard
from time import *


if __name__ == '__main__':
    while True:
        try:
            keyboard.add_hotkey('space', print('space'))
            keyboard.wait()
            sleep(1)
        except KeyboardInterrupt:
            break
    print('end')
