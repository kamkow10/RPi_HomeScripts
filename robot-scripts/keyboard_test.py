import keyboard
from time import *


if __name__ == '__main__':
    keyboard.add_hotkey('space', lambda: print('space'))
    print('end')
