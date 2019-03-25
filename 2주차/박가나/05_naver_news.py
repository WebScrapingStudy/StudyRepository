from urllib.request import urlopen
import bs4

url = "http://news.naver.com"
html = urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

ul = bsObj.find("ul", {"id" : "text_today_main_news_801001"})

lis = ul.findAll("li")

for li in lis :
    strong = li.find("strong")
    print(strong.text)
