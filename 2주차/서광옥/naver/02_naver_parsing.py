import urllib.request
import bs4
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url = "https://naver.com/"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")


#print(html.read())
#print(bsObj)

top_right = bsObj.find("div", {"class":"area_links"})
first_a = top_right.find("a")
print(first_a.text)
