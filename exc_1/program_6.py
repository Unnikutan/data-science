import numpy as np
arr = np.array([[1,2,3],[6,7,8]])
print("sum of elements :",np.sum(arr))
print("sum of elements in a row :",np.sum(arr,axis=1))
print("sum of elements in a column :",np.sum(arr,axis=0))
