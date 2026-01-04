#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("C:/Users/ypras/Downloads/world_population.csv")
df


# In[3]:


pd.set_option('display.float_format', lambda x : '%.2f' % x)
df


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


df.nunique()


# In[8]:


df


# In[9]:


df.sort_values(by = "2022 Population", ascending = False).head(10)


# In[10]:


df.corr(numeric_only=True)


# In[11]:


sns.heatmap(df.corr(numeric_only = True), annot = True)
plt.rcParams['figure.figsize'] = (25,8)
plt.show()


# In[12]:


df.groupby('Continent').mean(numeric_only = True)


# In[13]:


df[df['Continent'].str.contains('Oceania')]


# In[14]:


df.groupby('Continent').mean(numeric_only = True).sort_values(by = "2022 Population", ascending = False)


# In[15]:


dframe = df.groupby('Continent').mean(numeric_only = True).sort_values(by = "2022 Population", ascending = False)
dframe


# In[16]:


dframe.plot()


# In[17]:


dframe.transpose()


# In[18]:


dframe2 = dframe.transpose()
dframe2.plot()


# In[19]:


df.columns


# In[20]:


df3 = df.groupby('Continent')[df.columns[5:13]].mean(numeric_only = True).sort_values(by =  "2022 Population", ascending = False)
df3


# In[21]:


df4 = df3.transpose()
df4.plot()


# In[22]:


data_f = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean().sort_values(by = "2022 Population", ascending = False)
data_f


# In[23]:


d_f = data_f.transpose()
d_f


# In[24]:


d_f.plot()


# In[25]:


df.boxplot(figsize = (20,10))


# In[26]:


df.dtypes


# In[27]:


df.select_dtypes(include = 'object')


# In[28]:


df.select_dtypes(include = 'float')


# In[ ]:




