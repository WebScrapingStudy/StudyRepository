from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request

browser = webdriver.Chrome('C:/Users/Minho/Desktop/chromedriver.exe')
url = 'http://www.alio.go.kr/informationRecruit.do'
browser.get(url)
#정규직, 채용 진행중만 출력하기
browser.find_element_by_xpath('//*[@id="chk2_R1010"]').click()
browser.find_element_by_xpath('//*[@id="chk3_Y"]').click()

#검색 버튼 누르기
browser.find_element_by_xpath('//*[@class="cbot_area"]/a').click()

html = browser.page_source
soup = BeautifulSoup(html,'lxml')

items = soup.find() 
titles = soup.find_all('a')

for title in titles:
    print(title.get_text())