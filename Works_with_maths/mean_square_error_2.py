import numpy as np

actual = np.random.randint(1,50,25)
predicted  = np.random.randint(1,50,25)

def mse(actual, predecited) : 
    return np.mean((actual - predecited)^2)

print(mse(actual, predicted))
