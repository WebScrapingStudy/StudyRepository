#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request

url = "https://www.naver.com"
html=urllib.request.urlopen(url)

print(html.read())


# In[ ]:




