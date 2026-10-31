import numpy as np
import sys

A = [i for i in range(10000000)]
print(sys.getsizeof(A))

B = np.arange(10000000)
print(sys.getsizeof(B))