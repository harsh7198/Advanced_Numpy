import numpy as np 

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

C = np.concatenate((A,B),axis=0) # for vertically concatenate 
D = np.concatenate((A,B),axis=1) # for Horizontally concatenate 

print(C)
print(D)