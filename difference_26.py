import numpy as np

A = np.array([10, 20, 35, 50, 80])
# diff() = find the difference in array elements 
result = np.diff(A)
print(result)

B = np.array([100, 80, 90, 60, 70])
# negetive diffrence 
print(np.diff(B))

print(np.diff(A, n=2)) # calculate difference 2 times 


C = np.array([
    [10, 20, 30],
    [40, 60, 90]
])
# axis = 1 : every row difference 
# axis = 0 : every column difference 
print(np.diff(C, axis=1))
print(np.diff(C, axis=0))
