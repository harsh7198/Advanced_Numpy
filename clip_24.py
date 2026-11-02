import numpy as np
# convert minimum limit to minimum value same as maximum 
A = np.array([10, 20, 30, 40, 50, 60, 70])

result = np.clip(A, 25, 55) # array - min value - max value

print(result)