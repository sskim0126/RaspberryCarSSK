# 2017.12.08
# Team member : Kim Sungsik, Kim Sujin, Kim Gyuri
# Purpose : main code for assignment
# To do : line tracing, avoid obstacle

import RPi.GPIO as GPIO
from TrackingSensor import *
from Rascar import *

if __name__ == "__main__":
    pwm_setup()
    GPIO.setwarnings(False)
    try:
        while True:
            is_line = get_is_line()
            print(is_line)
            # 우회전 코드
            if is_line[4] == 0:
                stop()
                sleep(0.5)
                go_forward(40, 0.5)
                stop()
                sleep(0.5)
                right_point_turn(40, 0.3)
                is_line = get_is_line()
                while is_line[2] != 0:
                    right_point_turn(40, 0.05)
                    stop()
                    sleep(0.1)
                    is_line = get_is_line()
            elif is_line[0] == 0:
                go_forward(40, 0.3)
                is_line = get_is_line()
            # 좌회전 코드
                if is_line == [1, 1, 1, 1, 1]:
                    stop()
                    sleep(0.5)
                    left_point_turn(40, 0.3)
                    is_line = get_is_line()
                    while is_line[2] != 0:
                        left_point_turn(40, 0.05)
                        stop()
                        sleep(0.1)
                        is_line = get_is_line()
            # 유턴 코드
            elif is_line == [1, 1, 1, 1, 1]:
                stop()
                sleep(0.5)
                go_forward(40, 0.2)
                stop()
                right_point_turn(40, 0.6)
                is_line = get_is_line()
                while is_line[2] != 0:
                    right_point_turn(40, 0.05)
                    stop()
                    sleep(0.1)
                    is_line = get_is_line()
            # line tracing
            elif is_line == [1, 0, 1, 1, 1]:
                curve_turn(15, 40)
                sleep(0.05)
            elif is_line == [1, 0, 0, 1, 1]:
                curve_turn(20, 40)
                sleep(0.05)
            elif is_line == [1, 1, 1, 0, 1]:
                curve_turn(40, 15)
                sleep(0.05)
            elif is_line == [1, 1, 0, 0, 1]:
                curve_turn(40, 20)
                sleep(0.05)
            else:
                go_forward_any(40)
                sleep(0.05)




    except KeyboardInterrupt:
        pwm_low()
