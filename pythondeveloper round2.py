#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[16]:


df=pd.read_excel("Book.xlsx")


# In[17]:


df


# In[13]:


df1=pd.read_excel('Book2.xlsx')


# In[14]:


df1


# # Output 1

# In[20]:


output1=df.groupby('Team Name').mean()


# In[21]:


output1


# In[24]:


state=df1['total_statements']


# In[25]:


state


# In[26]:


df['total_statements']=state


# In[27]:


df


# In[28]:


reason=df1['total_reasons']


# In[29]:


df['total_reasons']=reason


# In[30]:


df


# In[45]:


output1=df.groupby('Team Name',sort=False).mean()


# In[46]:


output1


# In[47]:


df1


# In[52]:


output2=df.sort_values(by=['total_statements'],ascending=False)


# In[53]:


output2


# In[51]:


output1.to_excel('output.xlsx')


# In[54]:


output2.to_excel('output2.xlsx')


# In[ ]:




