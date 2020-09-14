#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db


# In[15]:


db_file = r'C:/Users/sarai/OneDrive/Desktop/Business Intelligence/salesdata.db'
engine = create_engine(r"sqlite:///{}"
                       .format(db_file))
sql = "select name from sqlite_master"
"where type = 'table';"
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[18]:


db_file = r'C:/Users/sarai/OneDrive/Desktop/Business Intelligence/salesdata.db'
engine = create_engine(r"sqlite:///{}"
                       .format(db_file))
sql = "select * from scores;"
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[ ]:




