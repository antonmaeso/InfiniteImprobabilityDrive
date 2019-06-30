import senOut as s
import time
from CompassCalibration import compassCalibration as cc
from math import sin, asin, atan2, cos, pi, sqrt

def bearing(cc):

    accRaw = s.AccelArray()
    magRaw = s.MagArray()

    #calibrate hard iron here
    
    magRaw[0] -= (cc[0] + cc[1]) /2
    magRaw[1] -= (cc[2] + cc[3]) /2
    magRaw[2] -= (cc[4] + cc[5]) /2

    accXnorm = accRaw[0]/sqrt(accRaw[0]* accRaw[0]+ accRaw[1] * accRaw[1] + accRaw[2] * accRaw[2])
    accYnorm =accRaw[1]/sqrt(accRaw[0] *accRaw[0] + accRaw[1] * accRaw[1] + accRaw[2] * accRaw[2])

    pitch = asin(accXnorm)
    #print("pitch: "+"{0:.4f}".format(pitch))

    roll = -asin(accYnorm/cos(pitch))
    #print("roll: "+"{0:.4f}".format(roll))

    magXcomp = magRaw[0]*cos(pitch)+(magRaw[2]+2)*sin(pitch)
    magYcomp = magRaw[0]*sin(roll)*sin(pitch)+(magRaw[1]+1)*cos(roll)-(magRaw[2]+2)*sin(roll)*cos(pitch)

    heading = 180*atan2(magYcomp,magXcomp)/pi
    if heading < 0:
        heading += 360
    #return heading
    return [pitch,roll,heading]

i = 0
cc.HardIronCalibration()
hardCalibration = [cc.magXmin,cc.magXmax,cc.magYmin,cc.magYmax,cc.magZmin,cc.magZmax]
while i<300:
    where = bearing(hardCalibration)
    #print("\r")
    print("pitch: "+"{0:.4f}".format(where[0])+ "\tRoll: "+"{0:.4f}".format(where[1])+"\tHeading: "+"{0:.4f}".format(where[2]), end = "\r")
    i += 1
    time.sleep(0.1)