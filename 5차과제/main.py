# 2017.11.29
# Team member : Kim Sungsik, Kim Sujin, Kim Gyuri
# Purpose : main code for assignment
# To do : line tracing, avoid obstacle

import RPi.GPIO as GPIO
from TurnModule_ksj import *
from TrackingSensor import *
from go_any_ksj import *

if __name__ == "__main__":
    pwm_setup()
    GPIO.setwarnings(False)
    try:
        while True:
            is_line = get_is_line()
            print(is_line)
            if is_line[4] == 0:
                stop(0.3)
                go_forward(40, 0.3)
                stop(0.3)
                rightPointTurn(40, 0.3)
                while is_line[2] != 0:
                    is_line = get_is_line()
                    rightPointTurn(40, 0.1)
            else:
                if is_line[1] == 0:
                    go_forward(40, 0.3)
                    if is_line == [1, 1, 1, 1, 1]:
                        stop(0.3)
                        leftPointTurn(40, 0.3)
                        while is_line[2] != 0:
                            is_line = get_is_line()
                            leftPointTurn(40, 0.1)
                elif is_line == [1, 1, 1, 1, 1]:
                    stop(0.3)
                    go_forward(40, 0.2)
                    while is_line[2] != 0:
                        rightPointTurn(40, 0.01)
                elif is_line == [1, 0, 1, 1, 1]:
                    curve_turn(30, 40)
                elif is_line == [1, 0, 0, 1, 1]:
                    curve_turn(35, 40)
                elif is_line == [1, 1, 1, 0, 1]:
                    curve_turn(40, 30)
                elif is_line == [1, 1, 0, 0, 1]:
                    curve_turn(40, 35)
                else:
                    go_forward_any(40)




    except KeyboardInterrupt:
        pwm_low()
