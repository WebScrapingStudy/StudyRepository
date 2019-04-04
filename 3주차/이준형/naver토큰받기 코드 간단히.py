#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from urllib.parse import urlparse

keyword="디퓨저"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(),
                     headers={"X-Naver-Client-Id":"6wpQoaf2csNYYAPvaFig",
                              "X-Naver-Client-secret":"IC8xm8jfyE"})
json_obj=result.json()
print(json_obj)


# In[ ]:




