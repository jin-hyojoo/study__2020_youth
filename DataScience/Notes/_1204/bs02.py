# 웹페이지 사이트 접근 (1)
import requests
import bs4

# 접근대상
url='https://finance.naver.com/item/main.nhn?code=252670'
result = requests.get(url)
#print(result)
bs_obj = bs4.BeautifulSoup(result.content, 'html.parser') # content로 갖고옴

# 원하는 값까지 도달하기 위해 몇번정도(여러번) 반복하며 찾아가기
# 태그는 div, 하위 애트리뷰트 속성 class값이 today인 것 찾기
today = bs_obj.find('div', {'class':'today'})
span = today.find('span')

# 원하는 곳에 도달했으면 그 태그의 데이터 값 갖고오자 !
print(span.text)