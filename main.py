# 2017.11.06
# Team member : Kim Sungsik, Kim Sujin, Kim Gyuri
# Purpose : main code for assignment
# To do : line tracing, avoid obstacle

import RPi.GPIO as GPIO
from ultraModule_ksj import getDistance
from TurnModule_ksj import *
from TrackingSensor import *
from go_any_ksj import *

if __name__ == "__main__":
    pwm_setup()
    GPIO.setwarnings(False)
    obstacle = 1
    try:
        while True:
            before_dis = -1
            while True:
                distance = getDistance()
                print(distance)
                if distance != before_dis:
                    break
            if distance > 17:
                is_line = get_is_line()
                print(is_line)
                if is_line == [0, 0, 0, 0, 0]:
                    stop()
                elif is_line == [1,1,0,1,1]:
                    go_forward_any(5)
                elif is_line == [1,1,1,1,1]:
                    leftSwingTurn(40, 0.05)
                elif is_line[1] == 0 and is_line[0] == 1:
                    curve_turn(35, 40)
                elif is_line[1] == 0 and is_line[0] == 0:
                    curve_turn(20, 40)
                elif is_line[1] == 1 and is_line[0] == 0:
                    curve_turn(10, 40)
                elif is_line[3] == 0 and is_line[4] == 1:
                    curve_turn(40, 35)
                elif is_line[3] == 0 and is_line[4] == 0:
                    curve_turn(40, 20)
                elif is_line[3] == 1 and is_line[4] == 0:
                    curve_turn(40, 10)
            else:
                stop()
                sleep(1)
                if obstacle == 1:
                    rightPointTurn(50, 0.5)
                    stop()
                    sleep(1)
                    go_forward(50, 0.4)
                    stop()
                    sleep(1)
                    leftPointTurn(50, 0.5)
                    stop()
                    sleep(1)
                    go_forward(50, 1.2)
                    stop()
                    sleep(1)
                    leftPointTurn(50, 0.5)
                    stop()
                    sleep(1)
                    obstacle += 1
                    while True:
                        is_line = get_is_line()
                        if is_line == [1, 1, 1, 1, 1]:
                            go_forward_any(1)
                        else:
                            break
                elif obstacle == 2:
                    rightPointTurn(50, 0.5)
                    stop()
                    sleep(1)
                    go_forward(50, 0.4)
                    stop()
                    sleep(1)
                    leftPointTurn(50, 0.5)
                    stop()
                    sleep(1)
                    go_forward(50, 1.2)
                    stop()
                    sleep(1)
                    leftPointTurn(50, 0.5)
                    stop()
                    sleep(1)
                    obstacle += 1
                    while True:
                        is_line = get_is_line()
                        if is_line == [1, 1, 1, 1, 1]:
                            go_forward_any(1)
                        else:
                            break




    except KeyboardInterrupt:
        pwm_low()

