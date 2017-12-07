# 2017.11.06
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
                sleep(0.3)
                go_forward(40, 0.5)
                stop()
                sleep(0.3)
                right_point_turn(40, 0.3)
                while is_line[2] != 0:
                    is_line = get_is_line()
                    right_point_turn(40, 0.01)
            else:
                if is_line[1] == 0:
                    go_forward(40, 0.5)
                    is_line = get_is_line()
                    # 좌회전 코드
                    if is_line == [1, 1, 1, 1, 1]:
                        stop()
                        sleep(0.3)
                        left_point_turn(40, 0.3)
                        while is_line[2] != 0:
                            is_line = get_is_line()
                            left_point_turn(40, 0.01)
                # 유턴 코드
                elif is_line == [1, 1, 1, 1, 1]:
                    stop()
                    sleep(0.3)
                    go_forward(40, 0.2)
                    while is_line[2] != 0:
                        right_point_turn(40, 0.01)
                # line tracing
                if is_line == [1, 0, 1, 1, 1]:
                    curve_turn(15, 40)
                elif is_line == [1, 0, 0, 1, 1]:
                    curve_turn(20, 40)
                elif is_line == [1, 1, 1, 0, 1]:
                    curve_turn(40, 15)
                elif is_line == [1, 1, 0, 0, 1]:
                    curve_turn(40, 20)
                else:
                    go_forward_any(40)




    except KeyboardInterrupt:
        pwm_low()
