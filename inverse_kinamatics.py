import numpy as np

X=2.0
Y=0.0
Z=1.0
a1=1.0
a2=1.0
a3=1.0
a4=1.0
a5=1.0
a6=1.0

r2d=180.0/np.pi

d2r=1.0/r2d


theta1=np.arctan(Y/X)
print('theta1=',theta1,'radians')
theta1deg=theta1*r2d
print('theta1deg',theta1deg,'degrees')


r2=np.sqrt((X*X)+(Y*Y))

r1=Z-a1

r3=np.sqrt((r1*r1)+(r2*r2))

phi1=np.arctan(r1/r2)

phi2=np.arccos(((a3*a3)-(a2*a2)-(r3*r3))/(-2*a2*r3))

theta2=phi1-phi2
print('theta2=',theta2,'radians')
theta2deg=theta2*r2d
print('theta2deg',theta2deg,'degrees')

phi3=np.arccos((-(a3*a3)-(a2*a2)+(r3*r3))/(-2*a2*a3))

theta3=(180.0*d2r)-phi3
print('theta3=',theta3,'radians')
theta3deg=theta3*r2d
print('theta3deg',theta3deg,'degrees')