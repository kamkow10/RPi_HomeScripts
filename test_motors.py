import RPi.GPIO as GPIO
from time import *

LEFT_MOTOR_PIN_1 = 20
LEFT_MOTOR_PIN_2 = 21
RIGHT_MOTOR_PIN_1 = 5
RIGHT_MOTOR_PIN_2 = 6
LOG_NUMBER = 1


def pauseLog(text):
    global LOG_NUMBER
    print('%d: %s' % (LOG_NUMBER, text))
    LOG_NUMBER += 1
    sleep(3)


def GPIOPreparation():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LEFT_MOTOR_PIN_1, GPIO.OUT)
    GPIO.output(LEFT_MOTOR_PIN_1, GPIO.LOW)
    pauseLog('setting')
    GPIO.setup(LEFT_MOTOR_PIN_2, GPIO.OUT)
    GPIO.output(LEFT_MOTOR_PIN_2, GPIO.LOW)
    pauseLog('setting')
    GPIO.setup(RIGHT_MOTOR_PIN_1, GPIO.OUT)
    GPIO.output(RIGHT_MOTOR_PIN_1, GPIO.LOW)
    pauseLog('setting')
    GPIO.setup(RIGHT_MOTOR_PIN_2, GPIO.OUT)
    GPIO.output(RIGHT_MOTOR_PIN_2, GPIO.LOW)
    pauseLog('setting')


def moveForward():
    GPIO.output(LEFT_MOTOR_PIN_1, GPIO.HIGH)
    GPIO.output(LEFT_MOTOR_PIN_2, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_PIN_1, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_PIN_2, GPIO.LOW)


def moveStop():
    GPIO.output(LEFT_MOTOR_PIN_1, GPIO.LOW)
    GPIO.output(LEFT_MOTOR_PIN_2, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_PIN_1, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_PIN_2, GPIO.LOW)


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
        while True:
            moveForward()
            sleep(5)
            moveStop()
            sleep(5)
    except KeyboardInterrupt:
        print('Program end')
    GPIO.cleanup()