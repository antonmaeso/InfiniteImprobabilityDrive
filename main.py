import Compass as Co
import datetime as dt
import time
from CompassCalibration import compassCalibration as cc
from Hid import hid as motor
from Hid import activationPattern as ap

#perform hard calibration at start 
#cc.HardIronCalibration()
#hardCalibration = [cc.magXmin,cc.magXmax,cc.magYmin,cc.magYmax,cc.magZmin,cc.magZmax]

timeToEnd = dt.datetime.now() + dt.timedelta(seconds=60)

currentTime = dt.datetime.now()
northMotor = motor(18)
#southMotor = motor()
while currentTime < timeToEnd:
    if buzzer.isActive() != True:
        heading = Co.bearing([-85.9,47,-97.4,30.3,-200.9,-74.2])
    
        print("Heading: "+"{0:.4f}".format(heading), end = "\r")
        if (heading > 340) or (heading < 20):
            northMotor.activate(ap.solid)
        # elif (heading > 160) or (heading < 200)
        #     southMotor.activate(ap.solid)

    
        currentTime = dt.datetime.now()