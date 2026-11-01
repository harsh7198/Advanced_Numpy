import numpy as np
import matplotlib.pyplot as plt

A = np.linspace(-10 , 10 , 100)
B = A*np.log(A)
plt.plot(A,B)
plt.show()