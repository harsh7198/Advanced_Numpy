import numpy as np

A = np.array([10, 20, 30, 40])
B = A.copy() # make a copy of original array 
B[0] = 100

print("Original Array:", A)
print("Copied Array:", B)

C = np.array([10, 20, 30, 40])
D = C.view() # share a underlying data 
D[0] = 100

print("Original Array:", C)
print("Copied Array:", D)