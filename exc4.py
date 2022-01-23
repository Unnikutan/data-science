#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
x=pd.Series(['a','b','c'])
print(x)


# In[2]:


from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start= date(2021, 5, 1)
end= date(2021, 5, 12)
for dt in daterange(start, end):
    print(dt.strftime("%Y-%m-%d"))


# In[3]:


import pandas as pd
details = {
    'Name' : ['Meera', 'Shiyas', 'Ammu', 'Unnikuttan'],
    'Age' : [23, 21, 22, 21],
    'University' : ['KU','MG','KTU','CUSAT'],
}
df = pd.DataFrame(details)
  
df


# In[4]:


import pandas as pd

data = [['New York Yankees', 'Acevedo Juan', 900000, 'Pitcher'], 
        ['New York Yankees', 'Anderson Jason', 300000, 'Pitcher']]
df = pd.DataFrame.from_records(data)
df


# In[5]:


import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())


# In[6]:


import numpy as np
import pandas as pd
df = pd.DataFrame({'Name': ['kavya','meera','aishu','ambadi','anu','rahul'],
                   'Age': [20, 22, 21, 19, 17, 23],
                   'Rank': [1, np.nan, 8, 9, 4, np.nan]})
print(df)
print('\nSORTED DATAFRAME\n')

print(df.sort_values(by=['Age'], ascending=True))


# In[7]:


import pandas as pd
data = {'Name':['Jai', 'Princi', 'Gaurav'],
        'Age':[27, 24, 22],
        'Address':['Delhi', 'Kanpur', 'Allahabad'],
        'Qualification':['Msc', 'MA', 'MCA'] }
  
index = {'a', 'b', 'c'}
df = pd.DataFrame(data, index)
df


# In[8]:


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


# In[ 9]:

import pandas  as pd
data={'name':['meera','kavya'],
      'occupation':['engineer','manager'],
      'salary':[45000,55000]}
df=pd.Dataframe(data)
print(df)
sal_avg=df.groupby('occupation')['salary'].mean()
print(sal_avg)

# In[10]:

import pandas as pd
df1=[[2,'anu',49],[4,'devika'],[8,'manu'],[10,'sona',50]]
df2=Dataframe(df1,columnd=['Rollno','Name','Mark'])
print(df2)
print("\n after modification:\nafter modification:\n")
df3=df2.fillna(0)
print(df3)

# In[11]:

import pandas as pd
df11=pd.read.csv("program11.csv")
print(df1)
df1[profit]=df1['profit']apply(lamda x:x>0)
df1

# In[12]:

import  pandas as pd
l1=[[100,'Arun',10000],[200,'vivek',14000],[300,'sona',9000]]
df1=pd.Dataframe(l1.columns=['eid','ename','stipend'])
print("\n Dataframe\n")
print(df1)
l2=[[100,'teacher'],[200,'hod'],[300,'librarian']]
df2=pd.ataframe(l2.columns=['eid','ename','stipend'])
print("\n Dataframe\n")
print(df2)
l3=pd.merge(df1,df2,how="inner",own="eid")
l3=rename(column2={'designation':'position'},inplace=True)
print("merged dataframe")
l3

