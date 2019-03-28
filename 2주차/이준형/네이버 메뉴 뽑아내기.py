#!/usr/bin/env python
# coding: utf-8

# In[6]:


import urllib.request
import bs4

url="https://www.naver.com"
html=urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")

ul=bs_obj.find("ul",{"class":"an_l"})

#리스트가 아닌 형태로 출력
for li in ul:
    print(li)

print("////////////////////////\n\n\n")
#findAll을 사용하면 리스트 형태로 출력이 가능[1,2,3]
#리스트 안에서 각항목들은 ,로 구분이 됨
#lis의 개수 보는법

#class를 따로 붙여주지 않고 "문자" 만 한 이유 하나밖에 없어서 구분이 되기 때문
lis = ul.findAll("li")
print(len(lis))
print(lis)

print("//////////////////////////\n\n\n")
    
#lis 에서 li라는 것을 찾는다.배열 형태로 원하는 위치꺼 출력 가능
for li in lis[0]:
    print(li)

print("//////////////////////////\n\n\n")
#더 깊이 들어가서 원하는 글자를 뽑는거 출력하는 부분에.text를 붙이면 단어만 아니면 정보 전체가 출력됨
for li in lis:
    a_tag=li.find("a")
    span=a_tag.find("span",{"class":"an_txt"})
    print(span.text)
    #print(a_tag) #a기준으로 나눠진거 보려면 이거
    
    


# In[ ]:




