# 2017.11.12
# Team member : Kim Sungsik, Kim Sujin, Kim Gyuri
# Purpose : 5-way tracking sensor module for assignment 4
# To do : 5-way tracking sensor module

import RPi.GPIO as GPIO

leftmostled = 16
leftlessled = 18
centerled = 22
rightlessled = 40
rightmostled = 32

GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled, GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)

def get_is_line():
    # 0 : black line
    # 1 : whilt ground
    return [GPIO.input(leftmostled),
            GPIO.input(leftlessled),
            GPIO.input(centerled),
            GPIO.input(rightlessled),
            GPIO.input(rightmostled)]