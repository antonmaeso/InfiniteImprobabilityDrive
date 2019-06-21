from gpiozero import LED as buzz # using LED as for now we just want on and off
from enum import Enum

class activationPattern(Enum):
    pulse = 1
    solid = 2

class hid(object):
    #def __init__(self):
    #  self.bearing#the center bearing that triggers this operator
    #  self.angle#the angle EITHER SIDE of the bearing which also triggers the operator

    def activate(pattern):
        if pattern.name == activationPattern.pulse
            buzz.blink(background=true, n=5,on_time=0.5,off_time=0.5)
        else 
            buzz.blink(background=true,n=1)
