import numpy as np

theta1=0.0
theta2=0.0
theta3=0.0
theta4=0.0
theta5=0.0
theta6=0.0

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