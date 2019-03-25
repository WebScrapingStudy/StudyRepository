import urllib.request
import bs4

url = "https://comic.naver.com/index.nhn"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

div = bsObj.find("div", {"class" : "tab_gr"})

lis = div.findAll("li")

for li in lis :
    a_tag = li.find("a")
    print(a_tag.text)
