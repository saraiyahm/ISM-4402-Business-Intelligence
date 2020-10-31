#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Create a pie chart
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','Mel','John']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']
df = pd.DataFrame(data = GradeList, columns=columns)
df


# In[13]:


df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']
df


# In[14]:


plt.pie(df['TotalDemerits'])


# In[15]:


plt.pie(df['TotalDemerits'],
        labels=df['Names'],
        explode=(0,0,0,0,0.15),
        startangle=90,
        autopct='%1.1f%%',)
plt.axis('equal')
plt.show()


# In[16]:


# Highlight John instead of Mel
plt.pie(df['TotalDemerits'],
        labels=df['Names'],
        explode=(0,0,0,0,0.15),
        startangle=90,
        autopct='%1.1f%%',)
plt.axis('equal')
plt.show()


# In[ ]:




