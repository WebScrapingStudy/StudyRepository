#-*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week='

html = urllib.request.urlopen(url)

bs4_obj = BeautifulSoup(html, 'html.parser')

ol = bs4_obj.find("ol",{"id":"realTimeRankFavorite"})
lis = ol.find_all("li")
webtoon_url=[]
webtoon_name = []
i=1
print("현재 웹툰 순위             URL")
for li in lis:
    a_tag = li.find("a")
    go_webtoon=str(a_tag).split()[1]
    webtoon_url.append("https://comic.naver.com"+go_webtoon.split("\"")[1])
#    print(str(a_tag).split()[1])
    webtoon_name.append(str(i) + ". " + a_tag.text.split('-')[0])
    i+=1
for i in range(len(webtoon_name)):
    print(webtoon_name[i] + " :     " + webtoon_url[i])
