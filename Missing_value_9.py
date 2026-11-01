import numpy as np 

A = np.array([1,2,3,4,np.nan,6])
print(A)
print(np.isnan(A)) # give boolean answers
print(A[~np.isnan(A)])  # give non nan values from array 