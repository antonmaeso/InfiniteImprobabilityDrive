import senOut as s
from math import sin, asin, atan2, cos, pi, sqrt

def bearing():

    accRaw = s.AccelArray()
    magRaw = s.MagArray()

    accXnorm = accRaw[0]/sqrt(accRaw[0]* accRaw[0]+ accRaw[1] * accRaw[1] + accRaw[2] * accRaw[2])
    accYnorm =accRaw[1]/sqrt(accRaw[0] *accRaw[0] + accRaw[1] * accRaw[1] + accRaw[2] * accRaw[2])

    pitch = asin(accXnorm)
    roll = -asin(accYnorm/cos(pitch))

    magXcomp = magRaw[0]*cos(pitch)+(magRaw[2]+2)*sin(pitch)
    magYcomp = magRaw[0]*sin(roll)*sin(pitch)+(magRaw[1]+1)*cos(roll)-(magRaw[2]+2)*sin(roll)*cos(pitch)

    heading = 180*atan2(magYcomp,magXcomp)/pi
    return heading