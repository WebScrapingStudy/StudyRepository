#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import sys
import urllib.request
#client id와 secret 수정
client_id = "6wpQoaf2csNYYAPvaFig"
client_secret = "IC8xm8jfyE"
#검색할 정보 넣기
encText = urllib.parse.quote("에어컨")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


# In[ ]:




