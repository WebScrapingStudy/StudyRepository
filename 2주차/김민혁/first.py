#-*- coding: utf-8 -*-
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

html_str="<html><div></div></html>"
bsObj=bs4.BeautifulSoup(html_str,"html.parser")
print(type(bsObj))
print(bsObj.find("div"))
#print(html)