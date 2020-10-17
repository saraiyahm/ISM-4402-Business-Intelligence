#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:/Users/sarai/OneDrive/Desktop/Business Intelligence/weekly_call_data/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


import statsmodels.formula.api as sm
result = sm.ols(
    formula='grade ~ age + exercise + hours',
    data=df).fit()
result.summary()


# In[4]:


import statsmodels.formula.api as sm
result = sm.ols(
    formula='grade ~ exercise + hours',
    data=df).fit()
result.summary()


# In[8]:


# Convert string to numbers
male = "0"
female = "1"


# In[9]:


# Add gender to the regression
import statsmodels.formula.api as sm
result = sm.ols(
    formula='grade ~ gender + exercise + hours',
    data=df).fit()
result.summary()


# In[ ]:


# This increases my R-squared

