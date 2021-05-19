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


def move_forward():
    GPIO.output(LEFT_MOTOR_PIN_1, 1)
    GPIO.output(LEFT_MOTOR_PIN_2, 0)
    GPIO.output(RIGHT_MOTOR_PIN_1, 1)
    GPIO.output(RIGHT_MOTOR_PIN_2, 0)


def move_stop():
    GPIO.output(LEFT_MOTOR_PIN_1, 0)
    GPIO.output(LEFT_MOTOR_PIN_2, 0)
    GPIO.output(RIGHT_MOTOR_PIN_1, 0)
    GPIO.output(RIGHT_MOTOR_PIN_2, 0)


if __name__ == '__main__':
    GPIOPreparation()
    light_on = False
    GPIO.output(12, light_on)
    try:
        while True:
            move_forward()
            sleep(5)
            move_stop()
            sleep(5)
    except KeyboardInterrupt:
        print('Program end')
    GPIO.cleanup()