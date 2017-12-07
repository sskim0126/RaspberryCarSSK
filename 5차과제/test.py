from Rascar import *
from TrackingModule import *
pwm_setup()

while True:
    l = get_is_line()
    if l == [
