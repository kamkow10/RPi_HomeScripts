import RPi.GPIO as GPIO
from time import *


def GPIOPreparation():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, 0)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, 0)
    GPIO.setup(20, GPIO.OUT)
    GPIO.output(20, 0)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, 0)


if __name__ == '__main__':
    GPIOPreparation()

    for i in range(3):
        GPIO.output(12, 1)
        GPIO.output(16, 0)
        GPIO.output(20, 1)
        GPIO.output(21, 0)
        sleep(1)
        GPIO.output(12, 0)
        GPIO.output(16, 1)
        GPIO.output(20, 0)
        GPIO.output(21, 1)
        sleep(1)

    GPIO.output(12, 0)
    GPIO.output(16, 0)
    GPIO.output(20, 0)
    GPIO.output(21, 0)

    for i in range(3):
        GPIO.output(12, 1)
        sleep(0.5)
        GPIO.output(16, 1)
        sleep(0.5)
        GPIO.output(20, 1)
        sleep(0.5)
        GPIO.output(21, 1)
        sleep(0.5)
        GPIO.output(12, 0)
        sleep(0.5)
        GPIO.output(16, 0)
        sleep(0.5)
        GPIO.output(20, 0)
        sleep(0.5)
        GPIO.output(21, 0)
        sleep(0.5)


    light1 = GPIO.PWM(12, 50)
    light2 = GPIO.PWM(16, 50)
    light3 = GPIO.PWM(20, 50)
    light4 = GPIO.PWM(21, 50)
    power = 0
    light.start(power)
    oddUp = True
    step = 1
    while True:
        if oddUp:
            power += step
            if power > 100:
                oddUp = False
                power -= step * 2
        else:
            power -= step
            if power < 0:
                oddUp = True
                power += step * 2
        light1.ChangeDutyCycle(power)
        light2.ChangeDutyCycle(100 - power)
        light3.ChangeDutyCycle(power)
        light4.ChangeDutyCycle(100 - power)
        sleep(0.01)