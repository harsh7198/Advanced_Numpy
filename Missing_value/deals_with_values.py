import numpy as np 

array = np.array([1,2,3,4,np.nan,6])
print(array)

#2 . detecting missing values
# np.isnan() --> checks if value is nan or not 
print(np.isnan(array))
print(np.sum(np.isnan(array)))


# 3 . to removing missing values 

clean_arr = array[~np.isnan(array)]
print(clean_arr)

# 4 .replacing missing value 
arr = np.array([10, 20, np.nan, 40 , 50])
arr[np.isnan(arr)] = 0 
print(arr)

# 5 . replace with mean
a = np.array([10,20,30,40,np.nan,60])
mean_value = np.nanmean(a)
a[np.isnan(a)] = mean_value
print(a)

