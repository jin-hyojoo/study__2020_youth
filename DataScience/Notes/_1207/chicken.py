'''
    2020년 12월 4일 수업
  # 셀레니움(스크립트, 인터렉션)을 통해 이벤트 처리 가능하도록 하는 라이브러리
    ex) 주소에 데이터값 변경 없는 사이트를 크롤링 할 때 페이지 버튼을 넘어가게 해주기

   셀레니움은 파이썬 전용은 아님, 실습에 chromedriver.exe 필요

   셀레니움 관련해 찾은 블로그, 간략하게 감 잡자!
   https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
'''


# 실습시작하기에 앞서 프로젝트 폴더에 "pip install selenium" 설치요함
import ssl
import time
import pandas as pd
from itertools import count
from bs4 import BeautifulSoup
from selenium import webdriver

# 굽네 매장찾기 페이지
url = 'https://www.goobne.co.kr/store/search_store.jsp'

# 실행파일 path정의
driver = webdriver.Chrome('../../chromedriver.exe')
driver.get(url)

# 크롤링 하기 전에 타임을 좀 늦춰야 함
# => 웹 뜨기 전엔 데이터 없는데.. 스크립트 속도가 너무 빨라 웹 뜨기 전부터 데이터 갖고오려고 하기 때문
time.sleep(2)

# 자바스크립트=표준스크립트라 따로 안적어도 됨
# => (a href="javascript:store.getList('7');") 에서 스크립트 생략
driver.execute_script("store.getList('7')")
time.sleep(2)
driver.execute_script("store.getList('2')")

#execute뒤에 타임슬립 해줘야 제대로된 데이터 갖고옴
time.sleep(2)

'''  2020년 12월 7일 수업, 데이터 얻어와 csv로 저장'''
rcv_data = driver.page_source
soupData = BeautifulSoup(rcv_data, "html.parser")

for storelist in soupData.findAll('tbody', {'id':'store_list'}):
    for strore_tr in storelist:
        tr_tag = list(strore_tr.strings)
        store_name = tr_tag[1]
        store_phone = tr_tag[3]
        store_address = tr_tag[6]
        print(store_name, ":", store_address, ":", store_phone)
        #result.append([store_name]+[store_address]+[store_phone])

# 크롤링 완료시 브라우저 종료
driver.close()
driver.quit()
