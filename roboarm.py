import numpy as np

X=20.0
Y=10.0
Z=10.0
a1=10.0
a2=10.0
a3=10.0
a4=10.0
a5=10.0
a6=10.0

r2d=180.0/np.pi

d2r=1.0/r2d


theta1=np.arctan(Y/X)
print('theta1=',theta1,'radians')
theta1deg=theta1*r2d
print('theta1deg',theta1deg,'degrees')


r2=np.sqrt((X*X)+(Y*Y))
print('r2=',r2)

r1=Z-a1
print('r1=',r1)

r3=np.sqrt((r1*r1)+(r2*r2))
print('r3=',r3)

phi1=np.arctan(r1/r2)
print('phi1=',phi1)

phi2=((a3*a3)-(a2*a2)-(r3*r3))/(-2*a2*r3)
print('phi2',phi2)

phi2=np.arccosh(((a3*a3)-(a2*a2)-(r3*r3))/(-2*a2*r3))
print('phi2',phi2)

theta2=phi1-phi2 
print('theta2=',theta2,'radians')
theta2deg=theta2*r2d
print('theta2deg',theta2deg,'degrees')

phi3=(-(a3*a3)-(a2*a2)+(r3*r3))/(-2*a2*a3)
print('phi3',phi3)

phi3=np.arccosh((-(a3*a3)-(a2*a2)+(r3*r3))/(-2*a2*a3))
print('phi3',phi3)

theta3=(180.0*d2r)-phi3
print('theta3=',theta3,'radians')
theta3deg=theta3*r2d
print('theta3deg',theta3deg,'degrees')




R0_6=[[1.0,0.0,0.0],
      [0.0,1.0,0.0],
      [0.0,0.0,1.0]]

R0_1=[[np.cos(theta1),0.0,np.sin(theta1)],
      [np.sin(theta1),0.0,-np.cos(theta1)],
      [0.0,1.0,0.0]]

R1_2=[[np.cos(theta2),-np.sin(theta2),0.0],
      [np.sin(theta2),np.cos(theta2),0.0],
      [0.0,0.0,1.0]]

R2_3=[[-np.sin(theta3),0.0,np.cos(theta3)],
      [np.cos(theta3),0.0,np.sin(theta3)],
      [0.0,1.0,0.0]]

R0_2=np.dot(R0_1,R1_2)

R0_3=np.dot(R0_2,R2_3)
print('R0_3=',np.matrix(R0_3))

invR0_3=np.linalg.inv(R0_3)

R3_6=np.dot(invR0_3,R0_6)
print('R3_6',np.matrix(R3_6))

theta5=np.arccos(R3_6[2][2])
print('theta5=',theta5,'radians')
theta5deg=theta5*r2d
print('theta5deg',theta5deg,'degrees')

                  

if theta5==0.0 or abs(theta5)/180.0*d2r==1.0:
            theta4=0.0
            theta6=np.arccos(R3_6[0][0])
            print('theta4=',theta4,'radians')
            theta4deg=theta4*r2d
            print('theta4deg',theta4deg,'degrees')
            print('theta6=',theta6,'radians')
            theta6deg=theta6*r2d
            print('theta6deg',theta6deg,'degrees')
else:
      theta6=np.arccos(-R3_6[2][0]/np.sin(theta5))
      print('theta6=',theta6,'radians')
      theta6deg=theta6*r2d
      print('theta6deg',theta6deg,'degrees')


      theta4=np.arcsin(R3_6[1][2]/np.sin(theta5))
      print('theta4=',theta4,'radians')
      theta4deg=theta4*r2d
      print('theta4deg',theta4deg,'degrees')

# theta4check=np.arccos(R3_6[0][2]/np.sin(theta5))
# print('theta4check=',theta4check,'radians')
# theta4degcheck=theta4check*r2d
# print('theta4degcheck',theta4degcheck,'degrees')



R3_4=[[np.cos(theta4),0.0,-np.sin(theta4)],
      [np.sin(theta4),0.0,np.cos(theta4)],
      [0.0,-1.0,0.0]]
print('R3_4=',np.matrix(R3_4))

R4_5=[[np.cos(theta5),0.0,np.sin(theta5)],
      [np.sin(theta5),0.0,-np.cos(theta5)],
      [0.0,1.0,0.0]]
print('R4_5=',np.matrix(R4_5))

R5_6=[[np.cos(theta6),-np.sin(theta6),0.0],
     [np.sin(theta6),np.cos(theta6),0.0],
     [0.0,0.0,1.0]]
print('R5_6=',np.matrix(R5_6))



R3_5=np.dot(R3_4,R4_5)
print('R3_5=',np.matrix(R3_5))

R3_6check=np.dot(R3_5,R5_6)
print('R3_6check=',np.matrix(R3_6check))



# H0_6=[[-1.0,0.0,0.0,1.0],
#       [0.0,-1.0,0.0,1.0],
#       [0.0,0.0,1.0,1.0],
#       [0.0,0.0,0.0,1.0]]


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