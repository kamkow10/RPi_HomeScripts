import keyboard
from time import *


if __name__ == '__main__':
    while True:
        try:
            if keyboard.is_pressed('q'):
                print('You Pressed A Key!')
                break
            sleep(0.01)
        except KeyboardInterrupt:
            break
    print('end')
