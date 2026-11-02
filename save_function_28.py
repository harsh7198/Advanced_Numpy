import numpy as np 

# save() : used to store an array in .npy
# format : np.save("File_name.npy",array)

Marks = np.array([10,20,30,40,50,60])
np.save("Marks.npy",Marks)
print("Marks saved Successfully.")