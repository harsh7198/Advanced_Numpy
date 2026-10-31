import numpy as np 
import time
A = np.arange(10000000)
B = np.arange(10000000 , 20000000)
start = time.time()
C = A + B 
print(time.time() - start)
