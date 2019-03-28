#!/usr/bin/env python
# coding: utf-8

# In[19]:


from urllib.request import urlopen
import bs4

url = "https://news.naver.com/"
html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(),"html.parser")

#print(bs_obj)

#f12 눌러서 개발자 도구 들어가서 왼쪽위 마우스 누르면 항목정보를 볼수 있음 
#원하는 단어만 출력 좀더 상세히 하려고 클래스 대신 id 사용함
ul=bs_obj.find("ul",{"id":"text_today_main_news_801001"})
lis=ul.findAll("li")

for li in lis:
    print(li)
    
print("///////////////////////////////\n\n\n\n\n")

for li in lis:
    strong=li.find("strong")#여기다가 .text를 붙여도 됨 그러면 strong에 글자만 저장됨
    print(strong.text)
    
print("///////////////////////////////\n\n\n\n\n")

#리스트에  넣는법 리스트에 넣으면 연산이나 관리하기가 편함
titles = [li.find("strong").text for li in lis]

for title in titles:
    print("오늘의 기사는",title)


# In[ ]:





# In[ ]:




