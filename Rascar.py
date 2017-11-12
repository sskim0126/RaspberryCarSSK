# 2017.11.12
# Team member : Kim Sungsik, Kim Sujin, Kim Gyuri
# Purpose : modules for assignment 4
# To do : go, stop, swing turn, setup

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

        GPIO.setup(self.MotorLeft_A, GPIO.OUT)
        GPIO.setup(self.MotorLeft_B, GPIO.OUT)
        GPIO.setup(self.MotorLeft_PWM, GPIO.OUT)

        GPIO.setup(self.MotorRight_A, GPIO.OUT)
        GPIO.setup(self.MotorRight_B, GPIO.OUT)
        GPIO.setup(self.MotorRight_PWM, GPIO.OUT)

        self.LeftPwm = GPIO.PWM(self.MotorLeft_PWM, 100)
        self.RightPwm = GPIO.PWM(self.MotorRight_PWM, 100)

    def pwm_setup(self):
        self.LeftPwm.start(0)
        self.RightPwm.start(0)

    def pwm_low(self):
        GPIO.output(self.MotorLeft_PWM, GPIO.LOW)
        GPIO.output(self.MotorRight_PWM, GPIO.LOW)
        self.LeftPwm.ChangeDutyCycle(0)
        self.RightPwm.ChangeDutyCycle(0)
        GPIO.cleanup()

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


class goModule:
    def go_forward_any(self, speed):
        while True:
            GPIO.output(self.MotorLeft_PWM, GPIO.HIGH)
            GPIO.output(self.MotorRight_PWM, GPIO.HIGH)
            self.leftmotor(self.forward0)
            self.LeftPwm.ChangeDutyCycle(speed)
            self.rightmotor(self.forward0)
            self.RightPwm.ChangeDutyCycle(speed)

    def go_backward_any(self, speed):
        while True:
            GPIO.output(self.MotorLeft_PWM, GPIO.HIGH)
            GPIO.output(self.MotorRight_PWM, GPIO.HIGH)
            self.leftmotor(self.backward0)
            self.LeftPwm.ChangeDutyCycle(speed)
            self.rightmotor(self.backward0)
            self.RightPwm.ChangeDutyCycle(speed)

    def go_forward(self, speed, running_time):
        GPIO.output(self.MotorLeft_PWM, GPIO.HIGH)
        GPIO.output(self.MotorRight_PWM, GPIO.HIGH)
        self.leftmotor(self.forward0)
        self.LeftPwm.ChangeDutyCycle(0.8 * speed)
        self.rightmotor(self.forward0)
        self.RightPwm.ChangeDutyCycle(speed)
        sleep(running_time)

    def go_backward(self, speed, running_time):
        GPIO.output(self.MotorLeft_PWM, GPIO.HIGH)
        GPIO.output(self.MotorRight_PWM, GPIO.HIGH)
        self.leftmotor(self.backward0)
        self.LeftPwm.ChangeDutyCycle(speed)
        self.rightmotor(self.backward0)
        self.RightPwm.ChangeDutyCycle(speed)
        sleep(running_time)

    def stop(self):
        GPIO.output(self.MotorLeft_PWM, GPIO.LOW)
        GPIO.output(self.MotorRight_PWM, GPIO.LOW)
        self.LeftPwm.ChangeDutyCycle(0)
        self.RightPwm.ChangeDutyCycle(0)

    def pwm_setup(self):
        self.LeftPwm.start(0)
        self.RightPwm.start(0)

    def pwm_low(self):
        GPIO.output(self.MotorLeft_PWM, GPIO.LOW)
        GPIO.output(self.MotorRight_PWM, GPIO.LOW)
        self.LeftPwm.ChangeDutyCycle(0)
        self.RightPwm.ChangeDutyCycle(0)
        GPIO.cleanup()

class turnModule:
    def left_point_turn(self, speed, running_time):
        self.leftmotor(self.backward0)
        GPIO.output(self.MotorLeft_PWM, GPIO.HIGH)
        self.rightmotor(self.forward0)
        GPIO.output(self.MotorRight_PWM, GPIO.HIGH)
        self.LeftPwm.ChangeDutyCycle(speed)
        self.RightPwm.ChangeDutyCycle(speed)
        sleep(running_time)

    def right_point_turn(self, speed, running_time):
        self.leftmotor(self.forward0)
        GPIO.output(self.MotorLeft_PWM, GPIO.HIGH)
        self.rightmotor(self.backward0)
        GPIO.output(self.MotorRight_PWM, GPIO.HIGH)
        self.LeftPwm.ChangeDutyCycle(speed)
        self.RightPwm.ChangeDutyCycle(speed)
        self.time.sleep(running_time)

    def left_swing_turn(self, speed, running_time):
        GPIO.output(self.MotorLeft_PWM, GPIO.LOW)
        self.rightmotor(self.forward0)
        GPIO.output(self.MotorRight_PWM, GPIO.HIGH)
        self.LeftPwm.ChangeDutyCycle(0)
        self.RightPwm.ChangeDutyCycle(speed)
        sleep(running_time)

    def right_swing_turn(self, speed, running_time):
        self.leftmotor(self.forward0)
        GPIO.output(self.MotorLeft_PWM, GPIO.HIGH)
        GPIO.output(self.MotorRight_PWM, GPIO.LOW)
        self.LeftPwm.ChangeDutyCycle(speed)
        self.RightPwm.ChangeDutyCycle(0)
        sleep(running_time)

    def curve_turn(self, left_speed, right_speed, running_time):
        self.leftmotor(self.forward0)
        GPIO.output(self.MotorLeft_PWM, GPIO.HIGH)
        self.rightmotor(self.backward0)
        GPIO.output(self.MotorRight_PWM, GPIO.HIGH)
        self.LeftPwm.ChangeDutyCycle(left_speed)
        self.RightPwm.ChangeDutyCycle(right_speed)
        self.time.sleep(running_time)
