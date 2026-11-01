import numpy as np 
# Broadcasting
A = np.arange(12).reshape(4,3)
B = np.arange(3)

print(A + B)

C = np.arange(12).reshape(3,4)
D = np.arange(12).reshape(4,3)

print(C + D)