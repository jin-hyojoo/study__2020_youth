''' 서울 관광지 입장정보 관련 데이터

{"response":{"header":{"resultCode":"0000","resultMsg":"OK"},"body":{"items":
{"item":[{"addrCd":2635,"csForCnt":286,"csNatCnt":9110,"gungu":"해운대구",
"resNm":"부산시립미술관","rnum":1,"sido":"부산광역시","ym":201201}}],
"numOfRows":10,"pageNo":1,"totalCount":1}}}

'''
from DataScience.Notes._1208.getUrl import get_request_url
import urllib.request
import json
import math
from DataScience.Notes._1208.config import *
def getTourPointVisitor(yyyymm, sido, gungu, nPageNum, nItems):
    endPoint = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
    param = '?_type=json&serviceKey=' + service_key
    param += '&YM=' + yyyymm
    param += '&SIDO=' + urllib.parse.quote(sido)
    param += '&GUNGU=' + urllib.parse.quote(gungu)
    param += '&RES_NM=&pageNo=' + str(nPageNum)
    param += '&numOfRows=' + str(nItems)
    url = endPoint + param

    # 위에서 조합한 최종 url 갖고오기
    retData = get_request_url(url)
    if(retData == None):
        return None
    else:
        return json.loads(retData) # 데이터 존재 시 json 데이터로 갖고옴

def getTourPointData(item, yyyymm, jsonResult):
    # 갖고올 item 데이터가 NULL값일 때 처리방법 (빈값이면 에러나기 때문)
    # ex) keys 목록안에 addrCd이 없으면 0값으로 대체, 있으면 해당값 넣기
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
    gungu = '' if 'gungu' not in item.keys() else item['gungu']
    sido = '' if 'sido' not in item.keys() else item['sido']
    resNm = 0 if 'resNm' not in item.keys() else item['resNm']
    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
    csForCnt = 0 if 'csForCnt' not in item.keys() else item['csForCnt']
    csNatCnt = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt']
    jsonResult.append({'yyyymm': yyyymm, 'addrCd': addrCd,
                       'gungu': gungu, 'sido': sido,
                       'resNm': resNm, 'rnum': rnum,
                       'csForCnt': csForCnt, 'csNatCnt': csNatCnt})

jsonResult = []
sido, gungu, nPageNum, nTotal, nItems, nStarYear, nEndYear = '서울특별시', '', 1, 0, 100, 2012, 2016

for year in range(nStarYear, nEndYear+1):
    for month in range(1,13):
        yyyymm = "{0}{1:0>2}".format(str(year), str(month))
        nPageNum = 1
        while True:
            jsonData = getTourPointVisitor(yyyymm, sido, gungu, nPageNum, nItems)
            if(jsonData['response']['header']['resultMsg'] == 'OK'):
                nTotal = jsonData['response']['body']['totalCount']

                # 데이터 없다면 루프 탈출
                if nTotal == 0:
                    break

                # 데이터 존재할 때 작업진행
                for item in jsonData['response']['body']['items']['item']:
                    getTourPointData(item, yyyymm, jsonResult)

                # 페이지 넘어갈 때
                nPage = math.ceil(nTotal/100)
                if(nPageNum == nPage) : break
                nPageNum += 1
        else:
            break

# json 파일로 저장
with open('%s_관광지입장정보_%d_%d.json'%(sido, nStarYear, nEndYear), 'w', encoding='utf8') as outfile:
    retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson)

# 파일저장 성공
print('%s_관광지입장정보_%d_%d.json Saved'%(sido, nStarYear, nEndYear))


# 데이터 잘 갖고왔는지 프린터해서 확인
# for item in jsonResult:
#     print(item['yyyymm'], ":", item['resNm'], ":", item['csForCnt'])

