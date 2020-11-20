#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "C:/Users/sarai/OneDrive/Desktop/Business Intelligence/axisdata.csv"
df = pd.read_csv(Location)
df


# In[4]:


# Average cars sold per month
df['Cars Sold'].mean()


# In[5]:


# Maximum cars sold per month
df['Cars Sold'].max()


# In[6]:


# Minimum cars sold per month
df['Cars Sold'].min()


# In[7]:


# Average cars sold per month by gender
df.groupby('Gender')['Cars Sold'].mean()


# In[13]:


# Average hours worked by people selling more than three cars per month
df.loc[df['Cars Sold'] > 3]['Hours Worked'].mean()


# In[9]:


# Average years of experience
df['Years Experience'].mean()


# In[10]:


# Average years of experience for people selling more than three cars per month
df.loc[df['Cars Sold'] > 3]['Years Experience'].mean()


# In[16]:


# Average cars sold per month sorted by whether they have had sales training
df.groupby('SalesTraining')['Cars Sold'].mean()


# In[19]:


# Chart showing hours worked
df.boxplot(column='Hours Worked')


# In[23]:


# Graph of average sales training
(df.loc[:,'SalesTraining'] == 'Y').mean()
df.groupby('SalesTraining')['SalesTraining'].count().plot.pie(autopct='%.2f',figsize=(5,5))


# In[ ]:




