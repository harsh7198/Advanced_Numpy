import numpy as np 

array = np.array([[1,2,np.nan],
                  [4,np.nan,6],
                  [7,np.nan,9]])

# for column data replace mean 
col_mean = np.nanmean(array, axis = 0)

# cheking where nan 

check = np.where(np.isnan(array))

# replace with column mean 
# arr = np.array([10, 20, 30])
# print(np.take(arr, [2, 0]))
array[check] = np.take(col_mean , check[1])
print(array)