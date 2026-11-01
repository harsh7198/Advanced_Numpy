import numpy as np 


# Fancy Indexing 
A = np.arange(12).reshape(3,4)
print(A)
B = A[[0,1]] # pass the index number directly for fancy indexing multiple rows
print(B)

