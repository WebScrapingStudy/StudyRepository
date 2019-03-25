#-*- coding: utf-8 -*-
import urllib.request
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
r=requests.get("https://news.naver.com/")
#print(r.content)
url = "https://news.naver.com/"
html = urlopen(url)

bs_obj = BeautifulSoup(html.read(),"html.parser")

ul = bs_obj.find('ul',{"id":"text_today_main_news_801001"})

lis = ul.find_all ("li")


for li in lis:
    title = li.find("strong")
    print(title.text)
    