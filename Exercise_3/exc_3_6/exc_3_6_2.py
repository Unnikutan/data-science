#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
x = np.array(["java","python","php","javascript","c#","c++"])
y = np.array([22.2,17.6,8.8,8,77,6.7])
plt.barh(x,y,color="red")
plt.xlabel("programming language")
plt.ylabel("popularity")
plt.show()


# In[ ]:




-

