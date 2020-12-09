import urllib.request
import ssl 

from bs4 import BeautifulSoup

import datetime
import math
import pandas as pd

context = ssl._create_unverified_context()

def get_request_url(url):
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now() )
            return response.read().decode("CP949")
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None


if __name__ == "__main__":
    
    curr_page = 1   # 현재 페이지 
    views = 20      # 페이지당 뷰 수
    last_num = 0    # 최종페이지 계산을 위한 값
    last_page = 0   # 최종페이지

    eq_list = []

    stDate = "2017-03-24"
    edDate = "2020-03-24"

    while(1):
        endpoint = "http://www.weather.go.kr/weather/earthquake_volcano/domesticlist.jsp?"
        params = "startSize=2&endSize=999&x=0&y=0&schOption=T"
        params += "&startTm=" + stDate
        params += "&startTm=" + edDate
        params += "&pNo="  + str(curr_page)

        url = endpoint + params

        response = get_request_url(url)
        soupdata = BeautifulSoup(response, "html.parser")
        tableData = soupdata.find("table", {"id":"excel_body"})
        tableBody = tableData.find("tbody")        
        tr_list = tableBody.find_all("tr")
        
        # 버튼 영역(tr) 제거
        del tr_list[-1]

        for tr in tr_list:
            tr = list(tr.strings)
            print(tr)

            # 발생시각 / 규모 / 깊이(km) / 최대진도 / 위도 / 경도 / 위치 
            eq_info = {}
            eq_info['timestamp']    = tr[1]
            eq_info['magnitude']    = tr[2]
            eq_info['depth']        = tr[3]
            eq_info['MMI_scale']    = tr[4]
            eq_info['lat']          = tr[5]
            eq_info['lon']          = tr[6]
            eq_info['location']     = tr[7]

            eq_list.append(eq_info)          
        
            # 마지막 페이지 계산
            if(last_num == 0):
                #print(last_num, views)
                last_num = int(tr[0])
                last_page = math.ceil(last_num/views)                

        result = pd.DataFrame(eq_list)
        result = result[['timestamp', 'magnitude', 'depth', 'MMI_scale', 'lat', 'lon','location']]
        
        # 마지막 페이지이면 크롤링 정지 // 마지막 페이지가 아니면 페이지수 증가후 크롤링
        if(last_page > curr_page):
            curr_page = curr_page + 1
        else:
            break
               
    result.to_csv("earthquake_list_%s-%s.csv"%(stDate[0:4], edDate[0:4]), encoding="CP949")
    print("Crawling Complete!!")
