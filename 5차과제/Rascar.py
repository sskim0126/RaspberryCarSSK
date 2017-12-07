# 20171112
# Team member : Kim Sungsik, Kim Sujin, Kim Gyuri
# Purpose : modules for assignment 4
# To do : go, stop, swing turn, setup

import RPi.GPIO as GPIO

from time import sleep

# set GPIO warnings as false
GPIO.setwarnings(False)
# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

forward0 = True
forward1 = False
backward0 = False
backward1 = True
# set left motor pins
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35
# set right motor pins
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
RightPwm = GPIO.PWM(MotorRight_PWM, 100)

def pwm_setup():
    LeftPwm.start(0)
    RightPwm.start(0)
def pwm_low():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()

def leftmotor(x):
    if x == True:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    elif x == False:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    else:
        print('Config Error')

def rightmotor(x):
    if x == True:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    elif x == False:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    else:
        print('Config Error')


def go_forward_any(speed):
    leftmotor(forward1)
    rightmotor(forward0)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)


def go_backward_any(speed):
    leftmotor(backward1)
    LeftPwm.ChangeDutyCycle(speed)
    rightmotor(backward0)
    RightPwm.ChangeDutyCycle(speed)

def go_forward(speed, running_time=-1):
    leftmotor(forward1)
    LeftPwm.ChangeDutyCycle(speed)
    rightmotor(forward0)
    RightPwm.ChangeDutyCycle(speed)
    if not running_time == -1:
        sleep(running_time)

def go_backward(speed, running_time):
    leftmotor(backward1)
    LeftPwm.ChangeDutyCycle(speed)
    rightmotor(backward0)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)

def stop():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)

def pwm_setup():
    LeftPwm.start(0)
    RightPwm.start(0)

def pwm_low():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()

def left_point_turn(speed, running_time):
    leftmotor(backward1)
    rightmotor(forward0)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)

def right_point_turn(speed, running_time):
    leftmotor(forward1)
    rightmotor(backward0)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)

def left_swing_turn(speed, running_time):
    rightmotor(forward0)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)

def right_swing_turn(speed, running_time):
    leftmotor(forward1)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(0)
    sleep(running_time)

def curve_turn(left_speed, right_speed):
    leftmotor(forward1)
    rightmotor(forward0)
    LeftPwm.ChangeDutyCycle(left_speed)
    RightPwm.ChangeDutyCycle(right_speed)

