# 웹페이지 사이트 접근 (2)
import urllib.request
from bs4 import BeautifulSoup

# 접근대상
url='https://www.naver.com/'
html = urllib.request.urlopen(url)
bs_obj = BeautifulSoup(html, 'html.parser')

# 데이터 찾기
ul = bs_obj.find('ul', {'class':'list_nav NM_FAVORITE_LIST'}) #근처 접근

# li 태그를 찾고, 그 속에 있는 a태그 접근
li_list = ul.find_all('li')
for li in li_list:
    a_tag = li.find('a')
    print(a_tag.text)

print()

# ============================================
# 직접해보기  => 카페 할리스 매장찾기
url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=1&sido=%EC%84%9C%EC%9A%B8&gugun=&store='
html = urllib.request.urlopen(url)
bs_obj = BeautifulSoup(html,'html.parser')
store_tbody = bs_obj.find('tbody')
stores = store_tbody.find_all('tr')

for store in stores:
    # tr태그 속 데이터를 list형으로.., 태그 없애기는 .strings 사용
    tr_tag = list(store.strings)
    # print(tr_tag) # 데이터 맞게 들어오는지..(구조 확인용)

    store_local = tr_tag[1]
    store_name = tr_tag[3]
    store_addr = tr_tag[7]
    store_ph = tr_tag[11]
    store_open = tr_tag[5]
    print(f'지역: {store_local}\n'
          f'점포명: {store_name}\n'
          f'주소:{store_addr}\n'
          f'번호: {store_ph}\n'
          f'영업상태:{store_open}\n'
          f'{"*"*30}')
