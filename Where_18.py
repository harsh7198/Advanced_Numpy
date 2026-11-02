import numpy as np 

marks = np.array([20,30,45,56,89,98])
# where check the condition and give result 
# syntax = np.where(conrition , return_if_true , return_if_false)

result = np.where(marks>=32,"Pass","Fail" )
print(result)
