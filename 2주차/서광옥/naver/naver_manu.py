import urllib.request
import bs4

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') #한글 깨짐 방지
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"an_l"})

lis = ul.findAll("li") #[1,2,3,4] [<li></li>, <li></li>] //리스트로 뽑아내는 것 (li들)
#for li in ul: #ul 안의 li 반복문 #대괄호가 있음
for li in lis:
    #print(lis) #대괄호가 있음
    a_tag = li.find("a")
    span = a_tag.find("span", {"class":"an_txt"})
    print(span.text) #.text면 글자만 뽑힘
