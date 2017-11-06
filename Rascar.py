# 2017.11.06
# Team member : Kim Sungsik, Kim Sujin, Kim gyury
# Purpose : modules for assignment 4
# To do : go, stop, swing turn, 5-channels tracker sensor, ultra sensor, setup

import RPi.GPIO as GPIO

from time import sleep

class setup:
    def __init__(self):
        pass

    def set_gpio_mode(self):
        # set GPIO warnings as false
        GPIO.setwarnings(False)
        # set up GPIO mode as BOARD
        GPIO.setmode(GPIO.BOARD)

    def set_motor_mode(self):
        pass