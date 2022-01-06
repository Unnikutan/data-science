#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
x=pd.Series(['a','b','c'])
print(x)


# In[9]:


from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start= date(2021, 5, 1)
end= date(2021, 5, 12)
for dt in daterange(start, end):
    print(dt.strftime("%Y-%m-%d"))


# In[10]:


import pandas as pd
details = {
    'Name' : ['Meera', 'Shiyas', 'Ammu', 'Unnikuttan'],
    'Age' : [23, 21, 22, 21],
    'University' : ['KU','MG','KTU','CUSAT'],
}
df = pd.DataFrame(details)
  
df


# In[11]:


import pandas as pd

data = [['New York Yankees', 'Acevedo Juan', 900000, 'Pitcher'], 
        ['New York Yankees', 'Anderson Jason', 300000, 'Pitcher']]
df = pd.DataFrame.from_records(data)
df


# In[12]:


import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())


# In[28]:


import numpy as np
import pandas as pd
df = pd.DataFrame({'Name': ['kavya','meera','aishu','ambadi','anu','rahul'],
                   'Age': [20, 22, 21, 19, 17, 23],
                   'Rank': [1, np.nan, 8, 9, 4, np.nan]})
print(df)
print('\nSORTED DATAFRAME\n')

print(df.sort_values(by=['Age'], ascending=True))


# In[57]:


import pandas as pd
data = {'Name':['Jai', 'Princi', 'Gaurav'],
        'Age':[27, 24, 22],
        'Address':['Delhi', 'Kanpur', 'Allahabad'],
        'Qualification':['Msc', 'MA', 'MCA'] }
  
index = {'a', 'b', 'c'}
df = pd.DataFrame(data, index)
df


# In[58]:


import pandas as pd
data = {'Name':['Jai', 'Princi', 'Gaurav'],
        'Age':[27, 24, 22],
        'Address':['Delhi', 'Kanpur', 'Allahabad'],
        'Qualification':['Msc', 'MA', 'MCA'] }
  
#print(data)
df = pd.DataFrame(data, index)
df[0:2]
#df1 = df.loc[df['index']]
#df1


# In[ ]:




