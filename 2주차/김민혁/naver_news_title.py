#-*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://news.naver.com/"
html = urlopen(url)

bs_obj = BeautifulSoup(html.read(),"html.parser")

ul = bs_obj.find('ul',{"id":"text_today_main_news_801001"})

lis = ul.findAll("li")


for li in lis:
    title = li.find("strong")
    print(title.text)
    