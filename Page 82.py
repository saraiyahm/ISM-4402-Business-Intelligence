#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create a histogram
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/sarai/OneDrive/Desktop/Business Intelligence/weekly_call_data/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df.hist()


# In[3]:


df.hist(column="hours")


# In[4]:


df.hist(column="hours", by="gender")


# In[5]:


# Create an age histogram categorized by gender
df.hist(column="age")


# In[6]:


# Categorize by gender
df.hist(column="hours", by="gender")


# In[ ]:




