import numpy as np
a=np.array([[ 0, 1, 2, 3, 4],[5, 6, 7, 8, 9],[10, 11, 12, 13, 14]])
print("row sum: ")
print(a.sum(axis=1))
print("column sum: ")
print(a.sum(axis=0))
