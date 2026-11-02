import numpy as np 

# tranpose matrix 
A = np.arange(12).reshape(3,4)
print(A)

B = np.transpose(A)
print(B)

# or 

print(A.T)