import numpy as np

# Boolean Indexing 

A = np.random.randint(1,100,24).reshape(6,4)
# Randomly Selected Items 
print(A)
print(A > 50) # print Boolean values like True , False 
print(A[A > 50]) # print Actual Value , given condition 

print(A[A %2==0]) # print Even numbers 
print(A[(A > 50) & ( A%2 ==0)]) # even and greater than 50
print(A[A %7 !=0]) # not divisible by 7