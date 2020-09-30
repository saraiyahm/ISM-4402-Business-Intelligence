#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Loading the Dataset from CSV
import pandas as pd
Location = "C:/Users/sarai/OneDrive/Desktop/Business Intelligence/weekly_call_data/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]
# Create names for the four groupsgroup_names = ['F', 'D', 'C', 'B', 'A']
group_names = ['F', 'D', 'C', 'B', 'A']


# In[3]:


# Cut Grades
df['lettergrade'] = pd.cut(df['grade'], bins,
                           labels=group_names)
df


# In[4]:


# Count Number of Observations
pd.value_counts(df['lettergrade'])


# In[5]:


# Page 34 - If a student passes or fails
import numpy as np
df['pass'] = np.where((df['grade']>80),
                      'pass','fail')
df.tail(10)


# In[ ]:




