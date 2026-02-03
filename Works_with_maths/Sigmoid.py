import numpy as np 

A = np.arange(10)

sigmoid = 1 / (1 + np.exp(-A))

print(sigmoid)