import math
import senOut as s

def getCorrectionAngles():
    AccelX = s.AccelX() #get from sensor
    AccelY = s.AccelY()
    AccelZ = s.AccelZ()

    omega = math.atan( AccelX/ (math.sqrt( (AccelY**2)+ (AccelZ**2) )) ) #x axis offset
    psi = math.atan( AccelY/ (math.sqrt( (AccelX**2)+ (AccelZ**2) )) ) #y axis offset
    theta = math.atan( (math.sqrt( (AccelX**2)+ (AccelY**2) ))/ AccelZ ) #z axis offset

    print('Theta: '+str(theta))
    print('Psi: '+str(psi))
    print('Omega: '+str(omega))

    return [theta,psi,omega]