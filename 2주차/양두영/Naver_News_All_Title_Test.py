import bs4
import urllib.request

url="https://news.naver.com/"
html=urllib.request.urlopen(url)

bs0bj=bs4.BeautifulSoup(html,"html.parser")

today_mains=bs0bj.findAll("div",{"class":"main_component droppable"})

for today_main in today_mains:
    lis=today_main.findAll("li")
    for li in lis:
        title=li.find("strong")
        print(title.text)

