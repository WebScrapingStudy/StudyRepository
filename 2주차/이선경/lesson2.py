# 9 . 나를 타겟으로 한 정적 웹페이지 스크래핑

#import urllib.request

#url = "http://www.naver.com/"
#html = urllib.request.urlopen(url)  #fuction 호출 , 이 주소 있는 페이지를 오픈하라

#print(html.read())

# 10. 11. beautiful soup 이라는 외부 라이브러리 사용 방법 및 사용
# ( 데이터를 추출하는데 필요한 기능이 들어있는 라이브러리 )
# 반도체 공장 (모래) = Beautifulsoup(html)

'''
import bs4
html_str = "<html><div></div></html>"
bsObj = bs4.BeautifulSoup(html_str, "html.parser")# beautiful soup object

print(type(bsObj))
print(bsObj)
print(bsObj.find("div"))
'''

#02_naver parsing

import urllib.request
import bs4


url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

# print(html.read())
# print(bsObj)

top_right = bsObj.find("div",{"class":"area_links"}) #div 이 페이지에 너무많음..
first_a = top_right.find("a")
#print(top_right)
print(first_a.text)  #텍스트만 뽑아내기