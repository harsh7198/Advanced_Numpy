import numpy as np
# cumsum : calculate running sum of array 
# cumprod : calculate runnung multiplication of array
A = np.array([10, 20, 30, 40, 50])
B = np.array([2,3,4,5,6])
result_1 = np.cumsum(A)
result_2 = np.cumprod(B)
print(result_1)
print(result_2)