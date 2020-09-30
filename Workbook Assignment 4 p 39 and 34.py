#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
Location = "C:/Users/sarai/OneDrive/Desktop/Business Intelligence/weekly_call_data/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[8]:


# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]
# Create names for the four groupsgroup_names = ['F', 'D', 'C', 'B', 'A']
group_names = ['F', 'D', 'C', 'B', 'A']


# In[10]:


df['lettergrade'] = pd.cut(df['grade'], bins,
                           labels=group_names)
df


# In[11]:


pd.value_counts(df['lettergrade'])


# In[15]:


# Page 39 - How often a student exercises 
import numpy as np
df['timemgmt'] = np.where((df['exercise']>3)
                               & (df['hours']>17),'yes','no')
df.tail(10)


# In[17]:


# Page 34 - If a student passes or fails
df['pass'] = np.where((df['grade']>80),
                      'pass','fail')
df.tail(10)


# In[ ]:




