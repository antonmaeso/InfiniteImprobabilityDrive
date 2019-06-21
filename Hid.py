from gpiozero import LED # using LED as for now we just want on and off
from enum import Enum

class activationPattern(Enum):
    pulse = 1
    solid = 2

class hid(object):
    def __init__(self,pin):
        #self.bearing#the center bearing that triggers this operator
        #self.angle#the angle EITHER SIDE of the bearing which also triggers the operator
        self.buzz = LED(pin)

    def activate(self, pattern):
        if pattern == activationPattern.pulse:
            self.buzz.blink(background=True, n=5,on_time=0.5,off_time=0.5)
        else:
            self.buzz.blink(background=True,n=1)
