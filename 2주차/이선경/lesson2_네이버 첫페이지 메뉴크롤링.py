import urllib.request
import bs4

url = "http://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
#print(bs_obj)
ul = bs_obj.find("ul",{"class":"an_l"}) #여기서 bs_obj 네이버 전체페이지

li_s = ul.findAll("li")     # [1,2,2,4][<li></li>, .. ]

for li in li_s: #li_s에서 li뽑는다
    a_tag = li.find("a",{"class":"an_a"})  #a tag하나만 있다는게 명백해서 굳이 안써줘도된다
    span = a_tag.find("span",{"class":"an_txt"})
    print(span.text)  #콤마랑 []없음

#print(li_s)     # finalAll과정으로 공백사라지고 리스트안에 들어가게되면서 콤마로 구분되었다
#print(len(li_s))
#for li in ul:#ul안에 li들 여러개 존재
#    print(li)

#print(ul)