# 2017.11.06
# Team member : Kim Sungsik, Kim Sujin, Kim Gyuri
# Purpose : main code for assignment
# To do : line tracing, avoid obstacle

import RPi.GPIO as GPIO
from Rascar import *
from UltraSensor import *
from TrackingSensor import *

if __name__ == "__main__":
    pwm_setup()
    try:
        while True:
            distance = get_distance()
            print(distance)
            if distance > 17:
                is_line = get_is_line()
                print(is_line)

                if is_line[1] == 1 and is_line[3] == 1:
                    go_forward_any(50)
                elif is_line[1] == 0:
                    curve_turn(30, 50)
                elif is_line[3] == 0:
                    curve_turn(50, 30)
            else:
                stop()

    except KeyboardInterrupt:
        pwm_low()











