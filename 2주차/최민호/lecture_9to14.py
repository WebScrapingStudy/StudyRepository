'''9강'''
'''
import urllib.request                           #urllib에 request한다.

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)              #urlopen이라는 function을 호출

print(html.read())                  
'''

'''10강'''
'''
import bs4

html_str = "<html><div></div></html>"
bsObj = bs4.BeautifulSoup(html_str,"html.parser")    

print(bsObj)
'''

'''11강'''
'''
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")          #html을 크롤링하고 bsObj에 대입

top_right = bsObj.find("div",{"class":"area_links"})    #{ } = add option
first_a = top_right.find("a")                           #class이름을 알아야 옵션을 상세화 할 수 있음(여기선 a)

print(first_a.text)                                     #text만 출력하고 싶을때
#print(top_right)
#print(html.read())                              
#print(bsObj)
'''

'''12강'''
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class" : "an_l"})
lis = ul.findAll("li")

for li in lis:
    a_tag = li.find("a")
    span = a_tag.find("span", {"class":"an_txt"})
    print(span.txt)