#!/usr/bin/env python
# coding: utf-8

# In[41]:


from urllib.request import urlopen
import bs4

url = "https://www.op.gg/champion/statistics"
html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(),"html.parser")

#print(bs_obj)

#f12 눌러서 개발자 도구 들어가서 왼쪽위 마우스 누르면 항목정보를 볼수 있음 
#원하는 단어만 출력 좀더 상세히 하려고 클래스 대신 id 사용함
div=bs_obj.find("div",{"class":"champion-index__champion-list"})
lis=div.findAll("div")

for li in lis:
    print(li)
    
for li in lis:
    strong=div.find("div",{"class":"champion-index__champion-item__name"})#여기다가 .text를 붙여도 됨 그러면 strong에 글자만 저장됨
    print(strong.text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




