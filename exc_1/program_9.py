import numpy as np
num = np.arange(16, dtype='int').reshape(-1, 4)
print("Original array:")
print(num)
print("\nNew array after swapping first and last rows of the said array:")
new_num = num[::-1]
print(new_num)
