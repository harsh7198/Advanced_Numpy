import numpy as np 

Actual = np.random.randint(1,50,25)
Predicted = np.random.randint(1,50,25)
n= 25
def MSE(actual , predicted):
    return np.mean((actual - predicted)**2)


print(MSE(Actual, Predicted))
