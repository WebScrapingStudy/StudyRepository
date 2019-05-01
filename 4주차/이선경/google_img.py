from prompt_toolkit.keys import Keys
from selenium import webdriver

import shutil
path = "C:/Program Files\ChromeDriver/chromedriver.exe"

#selenium 제어 브라우저창 생성
driver = webdriver.Chrome(path)

#webdriver가 google 페이지 접속하도록 명령
driver.get('https://www.google.co.kr/')
word = '임시완'
url = "https://www.google.co.kr/search?q=" + word + "&tbm=isch"
driver.get(url)

imgs = driver.find_elements_by_tag_name('img')
# print(img_num)
print(len(imgs))
# for img in imgs:
    # print(img.get_attribute('src'))
#검색이 제대로 되었는지 체크
assert "No results found." not in driver.page_source
# driver.close()