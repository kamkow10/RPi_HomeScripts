import RPi.GPIO as GPIO
from time import *


def GPIOPreparation():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.FALLING)


if __name__ == '__main__':
    GPIOPreparation()
    light_on = False
    GPIO.output(12, light_on)
    try:
        while True:
            GPIO.wait_for_edge(21, GPIO.FALLING)
            light_on = not light_on
            GPIO.output(12, light_on)
            sleep(1)
    except KeyboardInterrupt:
        print('Program end')
    GPIO.cleanup()