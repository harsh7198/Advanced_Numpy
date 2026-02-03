import numpy as np 


s = np.arange(6).reshape(2,3)
h = np.arange(3).reshape(1,3)  # both have different shapes 

print(s)
print("\n")
print(h)
print("\n")
print(s + h)