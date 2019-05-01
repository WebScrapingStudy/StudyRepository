from selenium import webdriver

path = "C:/Program Files\ChromeDriver/chromedriver.exe"

#selenium 제어 브라우저창 생성
driver = webdriver.Chrome(path)

#webdriver가 google 페이지 접속하도록 명령
driver.get('https://www.google.com')
# driver.close()

# 페이지 제목체크, Google에 제대로 접속된것인지 확인
assert "Google" in driver.title
# assert "Naver" in driver.title

#검색 입력부분에 커서 올리고,
#명령 내리기위해 elem 변수에 할당

elem = driver.find_element_by_name("q")

elem.clear()
elem.send_keys("Selenium")
elem.submit()

assert "No results found." not in driver.page_source
driver.close()