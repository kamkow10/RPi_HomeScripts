import RPi.GPIO as GPIO
from time import *

LEFT_MOTOR_PIN_1 = 20   # 1A
LEFT_MOTOR_PIN_2 = 21   # 2A
RIGHT_MOTOR_PIN_1 = 6   # 4A
RIGHT_MOTOR_PIN_2 = 5   # 3A
LOG_NUMBER = 1


def pauseLog(text):
    global LOG_NUMBER
    print('%d: %s' % (LOG_NUMBER, text))
    LOG_NUMBER += 1
    sleep(3)


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
        moveForward()
        sleep(3)
        moveBack()
        sleep(3)
        moveStop()
        sleep(3)
        moveForward()
        sleep(3)
    except KeyboardInterrupt:
        print('Program end')
    GPIO.cleanup()