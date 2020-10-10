#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Creating Dataset for Statistics
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
GradeList = zip(names,grades)
df = pd.DataFrame(data=GradeList,
columns=['Names','Grades'])
df


# In[2]:


# Computing Aggregate Statistics
df['Grades'].count()# number of values


# In[3]:


df['Grades'].mean()# arithmetic average


# In[4]:


df['Grades'].std()# standard deviation


# In[5]:


df['Grades'].min()# minimum


# In[6]:


df['Grades'].max()# maximum


# In[7]:


df['Grades'].quantile(.25)# first quartile


# In[8]:


df['Grades'].quantile(.5)# second quartile


# In[9]:


df['Grades'].quantile(.75)# third quartile


# In[10]:


#Other Measures of Central Tendency
# computes the arithmetic average of a column
# mean = dividing the sum by the number of values
df['Grades'].mean()


# In[11]:


# finds the median of the values in a column
# median = the middle value if they are sorted in order
df['Grades'].median()


# In[12]:


# finds the mode of the values in a column
# mode = the most common single value
df['Grades'].mode()


# In[13]:


#Computing Variance
# computes the variance of the values in a column
df['Grades'].var()


# In[14]:


#Computing Variance on All Numeric Columns
df.var()


# In[ ]:




