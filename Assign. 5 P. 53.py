#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load Dataset from CSV
import pandas as pd
import numpy as np
Location = "C:/Users/sarai/OneDrive/Desktop/Business Intelligence/weekly_call_data/gradedata.csv"
df = pd.read_csv(Location)
df.tail()


# In[2]:


# Random Sample of 500 Rows from Dataframe
df.take(np.random.permutation(len(df))[:500])


# In[ ]:




