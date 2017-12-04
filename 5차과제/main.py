# 2017.11.06
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
                stop()
                sleep(0.3)
                go_forward(40, 0.3)
                stop()
                sleep(0.3)
                rightPointTurn(40, 0.3)
                while is_line[2] != 0:
                    is_line = get_is_line()
                    rightPointTurn(40, 0.01)
            else:
                if is_line[1] == 0:
                    go_forward(40, 0.3)
                    if is_line == [1, 1, 1, 1, 1]:
                        stop()
                        sleep(0.3)
                        leftPointTurn(40, 0.3)
                        while is_line[2] != 0:
                            leftPointTurn(40, 0.01)
                elif is_line == [1, 1, 1, 1, 1]:
                    stop()
                    sleep(0.3)
                    go_forward(40, 0.2)
                    while is_line[2] != 0:
                        rightPointTurn(40, 0.01)
                elif is_line == [1, 0, 1, 1, 1]:
                    curve_turn(15, 30)
                    sleep(0.05)
                elif is_line == [1, 0, 0, 1, 1]:
                    curve_turn(20, 30)
                    sleep(0.05)
                elif is_line == [1, 1, 1, 0, 1]:
                    curve_turn(30, 15)
                    sleep(0.05)
                elif is_line == [1, 1, 0, 0, 1]:
                    curve_turn(30, 20)
                    sleep(0.05)
                else:
                    go_forward_any(40)
                    sleep(0.05)




    except KeyboardInterrupt:
        pwm_low()
