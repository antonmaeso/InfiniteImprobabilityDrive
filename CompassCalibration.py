import senOut as s
import datetime as dt

class compassCalibration(object):
    magXmax = -32767
    magYmax = -32767
    magZmax = -32767
    magXmin = 32767
    magYmin = 32767
    magZmin = 32767
    def HardIronCalibration():
        # run hard iron calibration for 15 seconds while sensor is being moved around
        timeToEnd = dt.datetime.now() + dt.timedelta(seconds=15)
        dt.time(15, 8, 24, 78915)
        magRaw = s.MagArray()

        currentTime = dt.datetime.now()

        while currentTime < timeToEnd:
            if magRaw[0] > compassCalibration.magXmax: 
                compassCalibration.magXmax = magRaw[0]
                print("magXmax: "+"{0:.4f}".format(compassCalibration.magXmax))
            if magRaw[1] > compassCalibration.magYmax: 
                compassCalibration.magYmax = magRaw[1]
                print("magYmax: "+"{0:.4f}".format(compassCalibration.magYmax))
            if magRaw[2] > compassCalibration.magZmax: 
                compassCalibration.magZmax = magRaw[2]
                print("magZmax: "+"{0:.4f}".format(compassCalibration.magZmax))

            if magRaw[0] < compassCalibration.magXmin: 
                compassCalibration.magXmin = magRaw[0]
                print("magXmin: "+"{0:.4f}".format(compassCalibration.magXmin))
            if magRaw[1] < compassCalibration.magYmin: 
                compassCalibration.magYmin = magRaw[1]
                print("magYmin: "+"{0:.4f}".format(compassCalibration.magYmin))
            if magRaw[2] < compassCalibration.magZmin: 
                compassCalibration.magZmin = magRaw[2]
                print("magZmin: "+"{0:.4f}".format(compassCalibration.magZmin))
            currentTime = dt.datetime.now()
            magRaw = s.MagArray()
        
        print("final readings")
        print("magXmax: "+"{0:.4f}".format(compassCalibration.magXmax))
        print("magYmax: "+"{0:.4f}".format(compassCalibration.magYmax))
        print("magZmax: "+"{0:.4f}".format(compassCalibration.magZmax))
        print("magXmin: "+"{0:.4f}".format(compassCalibration.magXmin))
        print("magYmin: "+"{0:.4f}".format(compassCalibration.magYmin))
        print("magZmin: "+"{0:.4f}".format(compassCalibration.magZmin))

compassCalibration.HardIronCalibration()