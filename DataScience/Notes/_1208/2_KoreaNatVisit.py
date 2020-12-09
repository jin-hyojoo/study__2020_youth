''' 특정 나라의 한국 입국자 수


# REST(URL)에 발급받은 서비스키 넣고 원하는 정보값으로 수정한 후 type= json으로 얻어온 데이터 예시
{"response":{"header":
{"resultCode":"0000","resultMsg":"OK"},
"body":{"items":{"item":{"ed":"방한외래관광객","edCd":"E","natCd":112,"natKorNm":"중  국",
"num":167022,"rnum":1,"ym":201201}},"numOfRows":10,"pageNo":1,"totalCount":1}}}


# {}.format() 문자출력 포맷 알아두기
ex)     "{0:0<2}".format(1)  =>  10
        "{0:0>2}".format(2)  =>  02
        "{0:0<3}".format(1)  =>  100
        "{0:0>3}".format(1)  =>  001
        "{0}{1}{0}".format(10,20)  => 102010  
설명) 괄호{ 첫번쨰 자릿수:두번쨰 자릿수 }라고 지칭.
     "{0:0<2}".format(1)경우엔 값 1, 남은 공간은 0으로 채우기,자리는 두자리수, <부등호는 오른쪽, >부등호는 왼쪽으로 채워라.
     "{0}{1}{0}".format(10,20)경우엔 매개변수가 2개 주어졌고 10은 첫쨰자리, 20은 둘째자리 의미. 
     따라서 첫쨰자리 의미하는 0에 10값이, 둘쨰자리 의미하는 1에 20값이 들어가 102010이란 결과가 나옴

'''
import urllib.request
import datetime
import json
from DataScience.Notes._1208.config import *
from DataScience.Notes._1208.getUrl import get_request_url

# 우리나라 방문객 json데이터 읽기 함수
def getNatVistor(yyyymm, nat_cd, ed_cd):
    # 활용가이드의 REST(URI) 쪼개기
    endPoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    # 데이터를 한 번에 가져오기 때문에 변수순서는 상관없음
    param = '?_type=json&serviceKey=' + service_key
    param += '&YM=' + yyyymm
    param += '&NAT_CD=' + nat_cd
    param += '&ED_CD=' + ed_cd
    url = endPoint + param

    # 데이터 로드 됐는지 확인
    retData = get_request_url(url)
    if(retData == None):
        return None
    else:
        return json.loads(retData)

jsonResult = []
nStarYear, nEndYear, nat_cd, ed_cd = 2011, 2017, '275', 'E'

for year in range(nStarYear, nEndYear+1):
    for month in range(1,13):
        yyyymm ="{0}{1:0>2}".format(str(year),str(month))
    
        # yyyymm에 해당하는 특정 나라의 한국 입국자 수의 json 데이터 읽어오기
        jsonData = getNatVistor(yyyymm, nat_cd, ed_cd)
    
        # 특정 데이터 접근해서 변수에 저장
        if(jsonData['response']['header']['resultMsg'] == 'OK'):
            krName = jsonData['response']['body']['items']['item']['natKorNm']
            iTotalVisit = jsonData['response']['body']['items']['item']['num']
            
            # 변수값 json 데이터에 추가
            jsonResult.append({'nat_name':krName,
                               'nat_cd':nat_cd,
                               'yyyymm': yyyymm,
                               'visit_cnt':iTotalVisit})

# 미국(275)_해외방문객정보_2011~2017.json 이름의 파일로 저장
with open('%s(%s)_해외방문객정보_%d~%d.json'%(krName, nat_cd, nStarYear, nEndYear),'w', encoding='utf8') as outfile:
    retJson = json.dumps(jsonResult, indent= 4, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson)
