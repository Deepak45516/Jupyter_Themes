#!/usr/bin/env python
# coding: utf-8

# In[1]:


from jupyterthemes import get_themes


# In[2]:


get_ipython().system('pip install jupyterthemes')


# In[5]:


get_ipython().system('jt -l')


# In[8]:


get_ipython().system('jt -t onedork')


# In[9]:


from jupyterthemes import get_themes


# In[10]:


from jupyterthemes.stylefx import set_nb_theme


# In[11]:


set_nb_theme('onedork')


# In[ ]:




