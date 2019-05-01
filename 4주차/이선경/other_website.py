from prompt_toolkit.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request

path = "C:/Program Files\ChromeDriver/chromedriver.exe"

#selenium 제어 브라우저창 생성
driver = webdriver.Chrome(path)

#webdriver가 google 페이지 접속하도록 명령
driver.get('http://yimsiwan.com/index3.html')
# driver.close()

# 페이지 제목체크, Google에 제대로 접속된것인지 확인
# assert "Naver" in driver.title

# #검색 입력부분에 커서 올리고,
# #명령 내리기위해 elem 변수에 할당
# elem = driver.find_element_by_name("q")
# # 입력part default 값 있을수 있음
# elem.clear()
# #검색어 입력
# elem.send_keys("Selenium")
# #검색을 실행
# elem.submit()

def get(max_count = 1):
    driver.get('http://yimsiwan.com/bbs/010/main.html')

    element = driver.find_element_by_name("user_id")
    element.send_keys("ssunkyung00")
    element = driver.find_element_by_name("password")
    element.send_keys("lsk0129")
    # element.submit()

    #button tag 가 없고input 태그 밖에 없다. (id 값이 없음)
    # 그렇기에 대신 DOM 구조에서 위치를 나타내는 XPath 값을 알면 접근 가능
    # 코드 우클릭, copy > copy xpath 선택
    # 양측에 따움표 """ 붙이고 그 사이에 Xpath 값 입력, 끝에 click() 붙이면
    # 사용자가 로그인을 위해 버튼을 클릴한 것과 같다.
    driver.find_element_by_xpath("""/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td[8]/span/input""").click()

    driver.get("http://yimsiwan.com/bbs/zboard.php?id=index")
    imgs = driver.find_elements_by_tag_name('img')
    for i in imgs:
        # print(i)
        img_src = i.get_attribute("src")
        print(img_src)
        img_url = str(i) + str(img_src)
        parse = img_src.split('/')[1]
        print(parse)
        # urllib.request.urlretrieve(img_url,"./img/"+img_name)
    # driver.get_screenshot_as_png("test1.png")
    #검색이 제대로 되었는지 체크
get(25)
assert "No results found." not in driver.page_source
# driver.close()