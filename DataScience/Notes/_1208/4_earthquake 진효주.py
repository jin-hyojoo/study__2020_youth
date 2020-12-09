''' 기상청 홈페이지의 국내지진 데이터 저장'''
import urllib.request
import ssl
from bs4 import BeautifulSoup
import datetime
import math
import pandas as pd
import json
from itertools import count

def get_request_url(url):
    context = ssl._create_unverified_context()
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

def get_data(num):
        url = "http://www.weather.go.kr/weather/earthquake_volcano/domesticlist.jsp?"
        Data = get_request_url(url)
        soupData = BeautifulSoup(Data, 'html.parser')
        earthquake_table = soupData.find('table', {'class':'table_develop'})
        earthquake_tbody = soupData.find('tbody')
        for earth in earthquake_tbody.findAll('tr'):
            bEnd = False;
            tr_tag = list(earth.strings)
            if num == 1:
                Result.append({'time': tr_tag[1], 'magnitude': tr_tag[2],
                               'depth': tr_tag[3], 'maxScale': tr_tag[4],
                               'latitude': tr_tag[5], 'longitude': tr_tag[6],
                               'location': tr_tag[7]})
            elif num == 2:
                Result.append([tr_tag[1]]+[tr_tag[2]]+[tr_tag[3]]+[tr_tag[4]]+[tr_tag[5]]+[tr_tag[6]]+[tr_tag[7]])
        if (bEnd == True):
            return;

def save_json():
    get_data(1)
    with open('국내지진목록.json', 'w', encoding='utf8') as outfile:
        kr_earthqk = json.dumps(Result, indent= 4, sort_keys=True, ensure_ascii=False)
        outfile.write(kr_earthqk)

def save_csv():
    get_data(2)
    kr_earthqk = pd.DataFrame(Result, columns=('time', 'magnitude', 'depth', 'maxScale', 'latitude', 'longitude', 'location'))
    kr_earthqk.to_csv('kr_earthqk.csv', encoding='utf8', index =True)


# Main
if __name__ == "__main__":
    Result = []
    # 원하는 저장 형식(json, csv)에 해당하는 함수코드 주석 풀기, 단 둘다 동시실행 X
    #save_json()
    save_csv()

