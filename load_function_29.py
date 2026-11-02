import numpy as np 

# load() : is used to read a existing .npy file 

data = np.load("Marks.npy")
print(data)

np.savetxt("marks.txt", data, fmt="%d") # used to convert .npy to txt or csv