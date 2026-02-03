import numpy as np 

# increment by 1 both side 
a = np.array([1])
# shape --> (1,1)
b = np.arange(4).reshape(2,2)
# shape --> (2,2)

print(a)
print("\n")
print(b)
print("\n")
print(a + b )
