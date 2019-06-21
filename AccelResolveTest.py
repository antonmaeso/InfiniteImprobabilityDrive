import math

AccelX = 1
AccelY = 2
AccelZ = 3

theta = math.atan( AccelX/ (math.sqrt( (AccelY**2)+ (AccelZ**2) )) )
psi = math.atan( AccelY/ (math.sqrt( (AccelX**2)+ (AccelZ**2) )) )
omega = math.atan( (math.sqrt( (AccelX**2)+ (AccelY**2) ))/ AccelZ )

print('Theta: '+str(theta))
print('Psi: '+str(psi))
print('Omega: '+str(omega))