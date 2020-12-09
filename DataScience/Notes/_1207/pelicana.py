'''  페리카나 매장찾기 매장 데이터 엑셀로 저장  '''

import urllib.request
from bs4 import BeautifulSoup
from itertools import count 
import pandas as pd
import ssl
import datetime

def get_request_url(url, enc='utf-8'):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url)
    try:
        respose = urllib.request.urlopen(req, context=context)
        if respose.getcode() == 200:
            # url 성공적으로 갖고오면 프린트
            print("[%s] Url Request Success" % datetime.datetime.now())
            try:
                # 데이터를 핸들링 하기위해 내 컴퓨터환경에 맞게 다시 캐릭터셋하는 과정 (decode)
                # 즉, 각자 본인들 환경에 맞춰서 정의된 캐릭터셋을 내 환경에 맞게 change
                rcv = respose.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')
            return ret
    except Exception as e:
        print(e)
        print("[%s] Error for URL " % datetime.datetime.now())

def getPelicanaAdress(sido, result):
    for page in count(): #페이지별 데이터 갖고오기 (itertools 모듈사용)
        context = ssl._create_unverified_context() #ssl은 웹페이지 보안관련

        #문자열데이터는 반드시 웹에서 쓸 수 있는 문자로 바꿔줘야 하기때문에 %(urllib.parse.quote(파싱할 데이터)) 필요
        url = "https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=%s&page=%s" \
        %(urllib.parse.quote(sido), str(page+1))
        rcv_data = get_request_url(url) #함수호출
        soupData = BeautifulSoup(rcv_data, "html.parser")
        store_table = soupData.find('table', {'class':'table mt20'})    
        tbody = store_table.find('tbody')
        bEnd = True
        for store in tbody.findAll('tr'):
            bEnd = False;
            tr_tag = list(store.strings) #웹페이지에서 크롤링한 데이터의 태그 없애고 리스트형으로..
            store_name = tr_tag[1]
            store_address = tr_tag[3]
            store_phone = tr_tag[5].strip()
            store_sido_gu = store_address.split()[:2] #리스트형
            result.append([store_name]+ store_sido_gu+[store_address]+[store_phone]) #리스트 합치기
        if(bEnd == True):
            return;


# 시/도 리스트
sido_list = ['서울특별시','부산광역시','대구광역시','제주특별자치도','광주광역시',
        '울산광역시','인천광역시','세종특별자치시','경기도','강원도','경상북도',
        '경상남도','충청북도','충청남도','전라북도','전라남도','대전광역시']
result = [];

print("페리카나 주소 크롤링 시작")

# 시/도 리스트를 이용해 주소 얻어옴
for sido in sido_list:
    getPelicanaAdress(sido, result)

# 엑셀로 저장하기 위해 DF 생성
perincana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'address', 'phone'))

# 엑셀로 저장
perincana_table.to_csv('perlicana.csv', encoding='cp949',index =True)                
print("페리카나 주소 크롤링 종료")
