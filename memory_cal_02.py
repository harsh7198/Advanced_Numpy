import sys
import numpy as np 

a = np.arange(10000000, dtype=np.int8)

print(sys.getsizeof(a))

# numpy gave the best size compared to python list 