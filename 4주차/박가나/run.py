from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Tour import TourInfo
import sys
from DbMgr import DBHelper as Db

# 사전에 필요한 정보를 로드 => 디비, 쉘, 배치파일에서 인자로 받아서 세팅
db = Db()
main_url = 'https://tour.interpark.com/'
keyword = '로마'

# 상품 정보를 담는 리스트 (TourInfo 리스트)
tour_list = []

# 드라이버 로드
driver = wd.Chrome(executable_path='chromedriver.exe')

# 사이트 접속 (get)
driver.get(main_url)

# 검색창을 찾아서 검색어를 입력
# 수정할 경우 뒤에 내용이 붙어버림 => .clear() -> .send_keys('내용')
driver.find_element_by_id('SearchGNBText').send_keys(keyword)

# 검색 버튼 클릭
driver.find_element_by_css_selector('button.search-btn').click()

# 잠시 대기 (페이지가 로드되고 나서 즉각적으로 데이터를 획득하는 행위는 자제해야 함)
# (1)명시적 대기 => 특정 요소가 발견될 때까지 대기
try:
    element = webDriverWait(driver, 10).until(
        # 지정한 한개 요소가 올라오면 wait 종료
        EC.presence_of_element_located((By.CLASS_NAME, 'oTravelBox'))
    )
except Exception as e:
    print('오류 발생', e)
# (2)암묵적 대기 => DOM이 다 로드될 때까지 대기하고 로드되면 바로 진행
# 요소를 찾을 특정 시간동안 DOM 폴링을 지시
driver.implicitly_wait(10)
# (3)절대적 대기 => 무조건 대기 -> time.sleep(10)

# 더보기 눌러서 게시판 진입
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()

# 게시판에서 데이터를 가져올 경우 => 데이터가 많으면 세션 (로그인을 해서 접근되는 사이트일 경우) 관리
# 특정 단위 별로 로그아수 로그인 계속 시도
# 특정 게시물이 사라질 경우 => 팝업 발생 => 팝업 처리 검토
# 게시판을 스캔할 경우 => 임계점을 모름
# 게시판 스캔 => 메타 정보 획득 => loop를 돌려서 일괄적으로 방문 접근 처리

# 16은 임시값 => 게시물을 넘어갔을 때 현상 확인
for page in range(1, 2):
    try:
        # 자바스크립트 구동하기
        driver.execute_script("searchModule.SetCategoryList(%s, '')" % page)
        time.sleep(1)
        print("%s 페이지 이동" % page)
        ##################################################################
        # 여러 사이트에서 정보를 수집할 경우 공통 정보 정의 단계 필요
        # 상품명, 코멘트, 기간1, 기간2, 가격, 평점, 썸네일, 링크(상품상세정보)
        boxItems = driver.find_elements_by_css_selector('.oTravelBox>.boxList>li')
        # 상품 하나하나 접근
        for li in boxItems:
            # 이미지를 링크값을 사용할 것인가? 직접 다운로드해서 우리 서버에 업로드 할 것인가?
            print('썸네일 : ', li.find_element_by_css_selector('img').get_attribute('src'))
            print('링크 : ', li.find_element_by_css_selector('a').get_attribute('onclick'))
            print('상품명 : ', li.find_element_by_css_selector('h5.proTit').text)
            print('코멘트 : ', li.find_element_by_css_selector('p.proSub').text)
            print('가격 : ', li.find_element_by_css_selector('strong.proPrice').text)
            for info in li.find_elements_by_css_selector('.info-row .proInfo'):
                print(info.text)
            print('='*100)
            # 데이터 모음
            obj = TourInfo(
                li.find_element_by_css_selector('h5.proTit').text,
                li.find_element_by_css_selector('strong.proPrice').text,
                # 데이터가 부족하거나 없을 수도 있으므로 직접 인덱스로 표현하면 위험성이 있음
                li.find_elements_by_css_selector('.info-row .proInfo')[1].text,
                li.find_element_by_css_selector('a').get_attribute('onclick'),
                li.find_element_by_css_selector('img').get_attribute('src')
            )
            tour_list.append(obj)
    except Exception as e1:
        print('오류', e1)

print(tour_list, len(tour_list))

#수집한 정보 개수를 루프 돌려서 페이지 방문 => 컨텐츠 획득 (상품 상세정보) => DB
for tour in tour_list:
    # tour => TourInfo
    print(type(tour))
    # 링크데이터에서 실데이터 획득
    # 분해
    arr = tour.link.split(',')
    if arr:
        # 대체
        link = arr[0].replace('searchModule.OnClickDetail(','')
        # 슬라이싱 => 앞에 ', 뒤에 ' 제거
        detail_url = link[1:-1]
        # 상세 페이지 이동 : URL 값이 완성된 형태인지 확인 (http~)
        driver.get(detail_url)
        time.sleep(1)
        # 현재 페이지를 bs4의 DOM으로 구성
        soup = bs(driver.page_source, 'html.parser')
        # 현재 상세 정보 페이지에서 스케줄 정보 획득
        data = soup.select('.tip-cover')
        print(type(data), len(data), data[0].contents)
        # DB 입력
        content_final = ''
        # for c in data[0].contents:
        #     contnet_final = str(c)

        # 컨텐츠 내용에 따라 전처리
        db.db_insertCrawlingData(
            tour.title,
            tour.price,
            tour.area,
            data[0].contents,
            keyword
        )




# 종료
driver.close()
driver.quit()
sys.exit()
