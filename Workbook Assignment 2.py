#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import glob


# In[19]:


all_data = pd.DataFrame()
for f in glob.glob("C:/Users/sarai/OneDrive/Desktop/Business Intelligence/weekly_call_data/weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[21]:


df.head()


# In[22]:





# In[ ]:





# In[41]:





# In[ ]:




