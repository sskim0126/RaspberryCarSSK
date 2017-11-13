# 2017.11.06
# Team member : Kim Sungsik, Kim Sujin, Kim Gyuri
# Purpose : ultra sensor module for assignment 4
# To do : ultra sensor module

import RPi.GPIO as GPIO
import time

trig = 33
echo = 31

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def get_distance(self):
    GPIO.output(self.trig, False)
    time.sleep(0.5)
    GPIO.output(self.trig, True)
    time.sleep(0.00001)
    GPIO.output(self.trig, False)
    while GPIO.input(self.echo) == 0:
        pulse_start = time.time()
    while GPIO.input(self.echo) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)
    return distance