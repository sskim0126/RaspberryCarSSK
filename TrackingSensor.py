# 2017.11.06
# Team member : Kim Sungsik, Kim Sujin, Kim Gyuri
# Purpose : 5-way tracking sensor module for assignment 4
# To do : 5-way tracking sensor module

import RPi.GPIO as GPIO

class trackingSensor:
    def set_tracking_mode(self):
        self.leftmostled = 16
        self.leftlessled = 18
        self.centerled = 22
        self.rightlessled = 40
        self.rightmostled = 32

        GPIO.setup(self.leftmostled, GPIO.IN)
        GPIO.setup(self.leftlessled, GPIO.IN)
        GPIO.setup(self.centerled, GPIO.IN)
        GPIO.setup(self.rightlessled, GPIO.IN)
        GPIO.setup(self.rightmostled, GPIO.IN)

    def get_isLine(self):
        # 0 : black line
        # 1 : whilt ground
        return [GPIO.input(self.leftmostled),
                GPIO.input(self.leftlessled),
                GPIO.input(self.centerled),
                GPIO.input(self.rightlessled),
                GPIO.input(self.rightmostled)]