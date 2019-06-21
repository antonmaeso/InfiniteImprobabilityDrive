import math
import AccelResolveTest as acc
import senOut as s

def bearingAngle():
    correctionAngles = acc.getCorrectionAngles()# use these angles to rotate the refence frame of the magnetic vector to that it aligns with the ground

    Magx = s.MagX#get from sensor
    MagY = s.MagY
    MagZ = s.MagZ


    for x in correctionAngles:
        print(str(x))
