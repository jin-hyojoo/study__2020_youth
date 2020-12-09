''' 0_book.xml 파싱 '''
from bs4 import BeautifulSoup

# 데이터 불러오기
with open('0_book.xml', 'r', encoding='utf-8') as book_xml:
    xml = book_xml.read()
    
# 데이터 갖고오기
soupdata = BeautifulSoup(xml, 'lxml')
print(soupdata.findAll('book')[0].text)
print(soupdata.findAll('book')[1].text)