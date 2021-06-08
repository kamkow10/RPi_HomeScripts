import keyboard
from time import *


if __name__ == '__main__':
    while True:
        try:
            keyboard.add_hotkey('space', lambda: print('space'))
        except KeyboardInterrupt:
            break
    print('end')
