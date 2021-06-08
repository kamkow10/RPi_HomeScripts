import keyboard
from time import *


if __name__ == '__main__':
    while True:
        try:
            keyboard.on_press({print('space')})
            sleep(1)
        except KeyboardInterrupt:
            break
    print('end')
