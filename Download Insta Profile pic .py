#!/usr/bin/env python
# coding: utf-8

# In[1]:


import instaloader


# In[ ]:


j = instaloader.Instaloader()
username = input("Enter username")
j.download_profile(username, profile_pic_only = True)


# In[ ]:




