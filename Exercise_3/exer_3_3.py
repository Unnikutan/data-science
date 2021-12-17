#!/usr/bin/env python
# coding: utf-8

# In[28]:


import matplotlib.pyplot as plt
import numpy as np
num = np.loadtxt("coordinate.txt")
print(num)
xor = np.array(num[:,0])
yor = np.array(num[:,1])
plt.plot(xor,yor,'*-r')
plt.show()


# In[ ]:





# In[ ]:




