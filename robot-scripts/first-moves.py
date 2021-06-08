import RPi.GPIO as GPIO
from time import *

LEFT_MOTOR_PIN_1 = 12   # 3A
LEFT_MOTOR_PIN_2 = 16   # 4A
RIGHT_MOTOR_PIN_1 = 20   # 1A
RIGHT_MOTOR_PIN_2 = 21   # 2A


def GPIOPreparation():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEFT_MOTOR_PIN_1, GPIO.OUT)
    GPIO.output(LEFT_MOTOR_PIN_1, 0)
    GPIO.setup(LEFT_MOTOR_PIN_2, GPIO.OUT)
    GPIO.output(LEFT_MOTOR_PIN_2, 0)
    GPIO.setup(RIGHT_MOTOR_PIN_1, GPIO.OUT)
    GPIO.output(RIGHT_MOTOR_PIN_1, 0)
    GPIO.setup(RIGHT_MOTOR_PIN_2, GPIO.OUT)
    GPIO.output(RIGHT_MOTOR_PIN_2, 0)


def moveForward():
    GPIO.output(LEFT_MOTOR_PIN_1, 1)
    GPIO.output(LEFT_MOTOR_PIN_2, 0)
    GPIO.output(RIGHT_MOTOR_PIN_1, 1)
    GPIO.output(RIGHT_MOTOR_PIN_2, 0)


def moveBack():
    GPIO.output(LEFT_MOTOR_PIN_1, 0)
    GPIO.output(LEFT_MOTOR_PIN_2, 1)
    GPIO.output(RIGHT_MOTOR_PIN_1, 0)
    GPIO.output(RIGHT_MOTOR_PIN_2, 1)


def moveStop():
    GPIO.output(LEFT_MOTOR_PIN_1, 0)
    GPIO.output(LEFT_MOTOR_PIN_2, 0)
    GPIO.output(RIGHT_MOTOR_PIN_1, 0)
    GPIO.output(RIGHT_MOTOR_PIN_2, 0)


def moveForwardRight():
    GPIO.output(LEFT_MOTOR_PIN_1, 1)
    GPIO.output(LEFT_MOTOR_PIN_2, 0)


def moveForwardLeft():
    GPIO.output(RIGHT_MOTOR_PIN_1, 1)
    GPIO.output(RIGHT_MOTOR_PIN_2, 0)


def moveBackRight():
    GPIO.output(LEFT_MOTOR_PIN_1, 0)
    GPIO.output(LEFT_MOTOR_PIN_2, 1)


def moveBackLeft():
    GPIO.output(RIGHT_MOTOR_PIN_1, 0)
    GPIO.output(RIGHT_MOTOR_PIN_2, 1)


def startCountdown():
    print('1')
    sleep(1)
    print('2')
    sleep(1)
    print('3')


if __name__ == '__main__':
    try:
        GPIOPreparation()
        startCountdown()

        print('forward left motor')
        moveForwardRight()
        sleep(3)
        print('back left motor')
        moveBackRight()
        sleep(3)
        print('stop')
        moveStop()
        sleep(3)

        print('forward right motor')
        moveForwardLeft()
        sleep(3)
        print('back right motor')
        moveBackLeft()
        sleep(3)
        print('stop')
        moveStop()
        sleep(3)

        print('forward all')
        moveForward()
        sleep(3)
        print('back all')
        moveBack()
        sleep(3)
        print('stop')
        moveStop()
        sleep(3)

        print('end')
    except KeyboardInterrupt:
        print('Program end')
    GPIO.cleanup()