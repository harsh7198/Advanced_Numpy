import numpy as np 

A = np.array([1,2,3,4,5,6])
print(A.dtype)
print(A)
# int ---> float 
B = A.astype(float)
print(B.dtype)
print(B)
# Float ---> String
C = B.astype(str)
print(C.dtype)
print(C)