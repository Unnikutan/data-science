#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,10,8,12])
y = np.array([4,6,18,20])
plt.plot(x,label="Line 1")
plt.plot(y,label="Line 2")
plt.legend()
plt.show()


# In[ ]:




