#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:/Users/sarai/OneDrive/Desktop/Business Intelligence/weekly_call_data/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[4]:


df = df.sort_values(by='fname', ascending=0)
df.head()


# In[6]:


df = df.sort_values(by='age', ascending=0)
df.head()


# In[7]:


df = df.sort_values(by='grade', ascending=0)
df.head()


# In[8]:


df = df.sort_values(by=['fname', 'age'],
                   ascending=[True, True])
df.head()


# In[ ]:




