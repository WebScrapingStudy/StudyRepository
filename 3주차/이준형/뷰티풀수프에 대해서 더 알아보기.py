#!/usr/bin/env python
# coding: utf-8

# In[28]:


#뷰티풀숩 사용을 위한 임포트 하는거
import bs4

#이렇게 한줄을 넘는 긴 형태의 문장을 문자열로 쓸때 에는 따옴표 3개를 사용하는게 좋음
html_str="""
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        <ul>
    </body>
</html>
"""

#뷰티풀솝을 이용해서 obj로 읽어오는것
bs_obj=bs4.BeautifulSoup(html_str,"html.parser")


#읽어온거 중에서 li요소만 뽑음
hello=bs_obj.find("li")
#뽑은것에서 txt요소만 출력
print(hello.txt)


# In[27]:


#읽어온거 에서 모든 li를 다 읽어오려면 findAll을 사용 a가 대문자인거 유의
lis=bs_obj.findAll("li")
print(lis)
#하나씩 줄별로 출력하는법
for li in lis:
    print(li)


# In[30]:


#lis의 타입을 확인하는법 result set 이라고 나오는데 일종의 리스트임
print(type(lis))
#lis의 요소중 1자리에 있는 내용을 출력하는것 0부터 시작하므로 2번째 자리임
print(lis[1].text)


# In[34]:


#for문을 사용하면서 한줄만 출력하게 하려면
#1:2는 1이상 2미만을 의미
for li in lis[1:2]:
    print(li.text)


# In[37]:


#tag 란 무엇인가? <ul></ul> <li></li> <div></div>... 같이 꺽쇠로 표현되어 있는것
#property 속성(프로퍼티) 이란? class,id,href,title,src 같이 tag뒤에 ...=으로 표현
#property value 속성값 class="greet"에서 greet이 속성값
#ex) <a href="www.google.com">구글</a> 에서의 태그,속성값은?
#tag? a, property(속성) href, 속성값 of href : www.google.com
#html <html></html> 

#모든 ㅣi의 요소가 아닌 특정부분의 요소를 뽑는법
#ul요소를 뽑는데 class 가 reply인 곳을 뽑는거
ul_reply=bs_obj.find("ul",{"class":"reply"})

print(ul_reply)


# In[41]:


#ul요소 중에서 class명이 reply인 것을 받아오고 그 중에서 li요소를 뽑는거
ul_reply=bs_obj.find("ul",{"class":"reply"})
lis=ul_reply.findAll("li")

for li in lis:
    print(li.text)


# In[ ]:




