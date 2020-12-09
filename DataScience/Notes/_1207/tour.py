from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 웹드라이브에 어떤 태그 올라왔는지 확인
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://tour.interpark.com/'
driver = webdriver.Chrome('../../chromedriver.exe')
driver.get(url)
time.sleep(2)

# find_~ 어쩌구 이용해 이벤트처리 들어갈 부분을 특정할 수 있는 값넣기
# 예제 url에선 id값이 정해져 있었기 떄문에 element_by_id를 이용,send_keys로 그곳에 로마라는 값을 보냄
driver.find_element_by_id('SearchGNBText').send_keys('독일')

# css_selector는 모든 css를 갖고오고 해당 대상에 "클릭" 이벤트 발생시킴
driver.find_element_by_css_selector('button.search-btn').click()
time.sleep(5)

# 10초 이상은 못기다려! => 10초 동안만 해당 요소가 올라올 때 까지 기다림
try:
    WebDriverWait(driver,10).until(
        # 요소가 메모리에 올라왔는지..
        EC.presence_of_all_elements_located(By.CLASS_NAME, 'oTravelBox')
    )
except Exception as e:
    print('오류발생', e)

#time.sleep과 기능 동일
driver.implicitly_wait(2)

# 클래스명이 oTravelBox 아래 자식-손자 요소들 이용해 특정 값 지정
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()

driver.execute_script("searchModule.SetCategoryList(8, '')")
time.sleep(2)

boxItems = driver.find_elements_by_css_selector('.oTravelBox>.boxList>li')
for li in boxItems:
    print(li.find_element_by_css_selector('h5.proTit').text)
    print(li.find_element_by_css_selector('strong.proPrice').text[:-1])

    # proInfo 값이 여러개라 elements사용, 자식요소 아닌 손주요소라 > 사용안했고, 하위레벨이라 띄어쓰기 이용 (띄어쓰기 미사용은 동일레벨을 의미)
    print(li.find_elements_by_css_selector('.info-row .proInfo')[0].text)
    # 필요없는 문자열 없애기 (필요한 데이터로 만들기)
    print(li.find_elements_by_css_selector('.info-row .proInfo')[1].text.replace('출발 가능 기간 : ',''))
    print()
