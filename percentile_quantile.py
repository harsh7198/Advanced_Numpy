import numpy as np

marks = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(np.percentile(marks, 25))
print(np.percentile(marks, 50))
print(np.percentile(marks, 75))
print(np.percentile(marks, 100))


print(np.quantile(marks, 0.25))
print(np.quantile(marks, 0.50))
print(np.quantile(marks, 0.75))