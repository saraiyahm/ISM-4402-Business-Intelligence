#!/usr/bin/env python
# coding: utf-8

# In[21]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd

df = pd.read_csv('C:/Users/sarai/OneDrive/Desktop/Business Intelligence/weekly_call_data/gradedata.csv', index_col=0)

df.head()


# In[23]:


dataframe = pd.DataFrame({'Col':
                          np.random.normal(size=200)})


# In[24]:


plt.scatter(dataframe.index, dataframe['Col'])


# In[ ]:




