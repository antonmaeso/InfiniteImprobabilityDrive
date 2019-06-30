from gpiozero import LED # using LED as for now we just want on and off
from enum import Enum

class activationPattern(Enum):
    pulse = 1
    solid = 2
    short = 3

class hid(object):
    def __init__(self,pin):
        #self.bearing#the center bearing that triggers this operator
        #self.angle#the angle EITHER SIDE of the bearing which also triggers the operator
        self.buzz = LED(pin)

    def activate(self, pattern):
        if self.buzz.is_active != True:
            if pattern == activationPattern.pulse:
                self.buzz.blink(background = True,n=5,on_time=.5,off_time=.5)
            elif pattern == activationPattern.short:
                self.buzz.blink(background = True,n=1,on_time=.5)
            else:
                self.buzz.blink(background = True,n=1)

    def isActive(self):
        return self.buzz.is_active

# motor = hid(18)
# motor.activate(activationPattern.pulse)
# motor.activate(activationPattern.solid)
# motor.activate(activationPattern.short)
# print("hello")
