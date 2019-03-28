from urllib.request import urlopen
import bs4
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://news.naver.com/"
html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")

ul = bs_obj.find("ul", {"id":"text_today_main_news_801001"})

lis = ul.findAll("li")

titles = [li.find("strong").text for li in lis ]

for title in titles:
    print("오늘의 기사는", title)
