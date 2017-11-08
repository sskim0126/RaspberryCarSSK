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
        self.forward0 = True
        self.forward1 = False
        self.backward0 = False
        self.backward1 = True
        # set left motor pins
        self.MotorLeft_A = 12
        self.MotorLeft_B = 11
        self.MotorLeft_PWM = 35
        # set right motor pins
        self.MotorRight_A = 15
        self.MotorRight_B = 13
        self.MotorRight_PWM = 37

    def leftmotor(self, x):
        if x == True:
            GPIO.output(self.MotorLeft_A, GPIO.HIGH)
            GPIO.output(self.MotorLeft_B, GPIO.LOW)
        elif x == False:
            GPIO.output(self.MotorLeft_A, GPIO.LOW)
            GPIO.output(self.MotorLeft_B, GPIO.HIGH)
        else:
            print('Config Error')

    def rightmotor(self, x):
        if x == True:
            GPIO.output(self.MotorRight_A, GPIO.HIGH)
            GPIO.output(self.MotorRight_B, GPIO.LOW)
        elif x == False:
            GPIO.output(self.MotorRight_A, GPIO.LOW)
            GPIO.output(self.MotorRight_B, GPIO.HIGH)
        else:
            print('Config Error')

    def go_forward_any(self, speed):
        while True:
            GPIO.output(self.MotorLeft_PWM, GPIO.HIGH)
            GPIO.output(self.MotorRight_PWM, GPIO.HIGH)
            self.leftmotor(self.forward0)
            self.rightmotor(self.forward0)

class goModule:
    pass

class trackingSensor:
    pass

class ultarSensor:
    pass