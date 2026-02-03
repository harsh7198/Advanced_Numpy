import numpy as np 


x = np.array([-4, -1, 0, 3, 6])
relu = np.maximum(0, x)

print(relu)

# avoid vanishing gradient 
# faster training 
