import numpy as np 

import numpy as np

S = np.array([
    [17, 79, 60, 77, 87, 93],
    [90, 12, 60, 74, 93, 81],
    [38, 96, 57, 40, 17, 38],
    [99, 89, 88, 36, 72, 29],
    [70, 68, 90, 99, 16, 13]
])


# print(S>50)  true or false
print(S[S>50]) # boolean masking , print only true 

# multiple condition 
print(S[(S > 10) & (S < 20)])
print(S[(S < 10) | (S > 20)])


# modify value using boolean indexing 
S[S>50] = 0
print(S)


# return a copy not view 