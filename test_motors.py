import RPi.GPIO as GPIO
from time import *

LEFT_MOTOR_PIN_1 = 20
LEFT_MOTOR_PIN_2 = 21
RIGHT_MOTOR_PIN_1 = 5
RIGHT_MOTOR_PIN_2 = 6


def GPIOPreparation():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LEFT_MOTOR_PIN_1, GPIO.OUT)
    GPIO.setup(LEFT_MOTOR_PIN_2, GPIO.OUT)
    GPIO.setup(RIGHT_MOTOR_PIN_1, GPIO.OUT)
    GPIO.setup(RIGHT_MOTOR_PIN_2, GPIO.OUT)
    GPIO.output(LEFT_MOTOR_PIN_1, 0)
    GPIO.output(LEFT_MOTOR_PIN_2, 0)
    GPIO.output(RIGHT_MOTOR_PIN_1, 0)
    GPIO.output(RIGHT_MOTOR_PIN_2, 0)


def moveForward():
    GPIO.output(LEFT_MOTOR_PIN_1, 1)
    GPIO.output(LEFT_MOTOR_PIN_2, 0)
    GPIO.output(RIGHT_MOTOR_PIN_1, 1)
    GPIO.output(RIGHT_MOTOR_PIN_2, 0)


def moveStop():
    GPIO.output(LEFT_MOTOR_PIN_1, 0)
    GPIO.output(LEFT_MOTOR_PIN_2, 0)
    GPIO.output(RIGHT_MOTOR_PIN_1, 0)
    GPIO.output(RIGHT_MOTOR_PIN_2, 0)


def startCountdown():
    print('1')
    sleep(1)
    print('2')
    sleep(1)
    print('3')


if __name__ == '__main__':
    startCountdown()
    GPIOPreparation()
    try:
        while True:
            moveForward()
            sleep(5)
            moveStop()
            sleep(5)
    except KeyboardInterrupt:
        print('Program end')
    GPIO.cleanup()