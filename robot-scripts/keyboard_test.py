import keyboard
from time import *


if __name__ == '__main__':
    keyboard.on_press({print('space')})
    while True:
        try:
            sleep(1)
        except KeyboardInterrupt:
            break
    print('end')
