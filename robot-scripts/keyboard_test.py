import keyboard


if __name__ == '__main__':
    keyboard.on_press_key('space', {print('space')})
    while True:
        try:
            sleep(1)
        except KeyboardInterrupt:
            break
    print('end')