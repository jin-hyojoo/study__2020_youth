''' itertools 사용 '''
import urllib.request
from bs4 import BeautifulSoup
from itertools import count
import ssl #보안관련으로 페이지 데이터 로딩 안될때

context = ssl.create_default_context()
url = 'https://pelicana.co.kr/store/stroe_search.html?page=2&branch_name=&gu=&si='
req = urllib.request.Request(url)
response = urllib.request.urlopen(req, context=context)
soupData = BeautifulSoup(response, 'html.parser')







