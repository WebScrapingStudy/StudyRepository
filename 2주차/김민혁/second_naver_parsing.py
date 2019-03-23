#-*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

url="https://www.naver.com/"
html=urllib.request.urlopen(url)

bs_obj=BeautifulSoup(html,"html.parser")

ul=bs_obj.find("ul", {"class":"an_l"})

lis= ul.find_all("li")
print(lis)
for li in lis:
	a_tag=li.find("a")
	span=a_tag.find("span",{"class":"an_txt"})
	print(span.text)


