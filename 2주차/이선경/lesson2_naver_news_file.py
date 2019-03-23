from urllib.request import urlopen
import bs4

url = "http://"
html = urlopen(url)
print(html.read())

bs_obj = bs4.BeautifulSoup(html.read(),"html.parser")
print(bs_obj)


# 생략