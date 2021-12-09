import numpy as np
list1 = np.arange(start=0, stop=21)
vector= np.array(list1)
print("\n\t Original vector:",vector)

print("After changing the sign of the numbers in the range from 9 to
15:")
vector[(vector > 8) & (vector < 16)] *= -1
print(vector)
