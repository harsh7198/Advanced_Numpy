import numpy as np 
# pick elements in specific position 
s = np.array([1,2,3,4,5])
print(s[[0,2,4]])

# with 2D array 

D = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) # if print specific like index 0,2,3
p = D[[0,2,3]]
print(p)

# let print first column and last column so 
print(D[:,[0,2]])