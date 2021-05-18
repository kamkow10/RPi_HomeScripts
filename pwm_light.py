import RPi.GPIO as GPIO
from time import *


def GPIOPreparation():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(12, GPIO.OUT)


if __name__ == '__main__':
    GPIOPreparation()
    light = GPIO.PWM(12, 50)
    power = 0
    light.start(power)
    up = True
    while True:
        if up:
            power += 2
            if power > 100:
                up = False
                power -= 4
        else:
            power -= 2
            if power < 0:
                up = True
                power += 4
        light.ChangeDutyCycle(power)
        sleep(0.1)