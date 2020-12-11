import numpy as np

a1=1.0
a2=1.0
a3=1.0 
a4=1.0
a5=1.0
a6=1.0

theta1=0.0
theta2=0.0
theta3=0.0
theta4=0.0
theta5=0.0
theta6=0.0

r2d=180.0/np.pi

d2r=1.0/r2d

PT=[[theta1,90.0*d2r,0.0,a1],
    [theta2,0.0,a2,0.0],
    [(90.0*d2r)+theta3,90.0*d2r,0.0,0.0],
    [theta4,-90.0*d2r,0.0,a3+a4],
    [theta5,90.0*d2r,0.0,0.0],
    [theta6,0.0,0.0,a5+a6]]



i=0
H0_1=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
      [0.0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
      [0.0,0.0,0.0,1.0]]
print('H0_1=',np.matrix(H0_1))

i=1
H1_2=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
      [0.0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
      [0.0,0.0,0.0,1.0]]
print('H1_2=',np.matrix(H1_2))

i=2
H2_3=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
      [0.0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
      [0.0,0.0,0.0,1.0]]
print('H2_3=',np.matrix(H2_3))




i=3
H3_4=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
      [0.0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
      [0.0,0.0,0.0,1.0]]
print('H3_4=',np.matrix(H3_4))

i=4
H4_5=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
      [0.0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
      [0.0,0.0,0.0,1.0]]
print('H4_5=',np.matrix(H4_5))

i=5
H5_6=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
      [0.0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
      [0.0,0.0,0.0,1.0]]
print('H5_6=',np.matrix(H5_6))


H0_2=np.dot(H0_1,H1_2)
H2_4=np.dot(H2_3,H3_4)
H4_6=np.dot(H4_5,H5_6)
H0_4=np.dot(H0_2,H2_4)
H0_6=np.dot(H0_4,H4_6)
print('H0_6=',np.matrix(H0_6))