import matplotlib.pyplot as plt
import numpy as np
x=['G1','G2','G3','G4','G5']
y=[22, 30, 35, 35, 26]
z=[25, 32, 30, 35, 29]
x1=np.arange(len(x))
plt.bar(x1- 0.2, y, width=0.4, label = 'men',color="green")
plt.bar(x1+0.2, z,  width=0.4,label = 'women',color="red")
plt.xticks(x1, x)
plt.xlabel("person")
plt.ylabel("scores")
plt.title("scores by person")
plt.legend()
plt.show()