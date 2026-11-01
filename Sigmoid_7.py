import numpy as np 

A = np.arange(10)

def sigmoid(Array):
    return 1/(1 + np.exp(-(Array)))
# sigmoid value of each numbers using formula 
print(sigmoid(A))