#!/usr/bin/env python
# coding: utf-8

#셀레니움과 뷰티풀 수프 사용을 위한 import
from selenium import webdriver
from bs4 import BeautifulSoup

#창이 완전히 켜질때 까지 기다림
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#'chromedriver.exe'가 존재하는 경로를 준다.
driver=webdriver.Chrome('chromedriver.exe')

#유투브 창을 띄움.
main_url = 'https://www.youtube.com/'
driver.get(main_url)

#콘솔로 검색어를 입력 받는다.
keyword=input("검색어 입력: ")

#검색어를 입력 창에 넣고 검색을 실행
driver.find_element_by_name('search_query').send_keys(keyword)
driver.find_element_by_id('search-icon-legacy').click()

#현재페이지 url를 주고 해당하는 정보를 beautifulsoup로 받는다.
page=driver.current_url
driver.get(page)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

#가장 위에 있는 동영상을 튼다.
driver.find_element_by_id("video-title").click()

#광고가 재생될경우 반복해서 광고 건너뛰기 버튼을 눌러준다.
while 1:
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ytp-ad-skip-button'))
        )
        
        driver.find_element_by_class_name('ytp-ad-skip-button').click()
        
    except:
        pass

    

