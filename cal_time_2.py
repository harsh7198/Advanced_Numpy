import time 
import numpy as np 

a = np.arange(10000000)
b = np.arange(10000000,20000000)
start = time.time()

c = a + b 
print(time.time()-start)

# numpy array faster then phython list for execution 
print(time.time())