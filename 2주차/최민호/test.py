from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request

browser = webdriver.Chrome('C:/Users/Minho/Desktop/chromedriver.exe')
url = 'https://www.op.gg/champion/statistics'
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html,'lxml')

herolist = soup.findAll("div",{"class":"champion-index__champion-list"})
titles = herolist.findAll("td",{"class":"left"})

for title in titles:
    a_tag = title.find("a").text
    print(a_tag)