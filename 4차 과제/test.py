from go_any_ksj import *
from TurnModule_ksj import *
from ultraModule_ksj import *
import RPi.GPIO as GPIO
pwm_setup()
GPIO.setwarnings(False)
try:
    while True:
        distance = getDistance()
        if distance > 17:
            curve_turn(20, 30)
        else:
            stop()


except KeyboardInterrupt:
    stop()
