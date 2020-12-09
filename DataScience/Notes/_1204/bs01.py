import pandas as pd
import bs4


#뷰티폴숩 사용 (파싱을 통해 원하는 목적에 따라 데이터 갖고옴)
htm_str = "<html><div>Hello</div></html>"
result = bs4.BeautifulSoup(htm_str, 'html.parser')

#find는 첫번째 나와있는 태그(맨처음)
result = result.find('div')  #결과/ <div>Hello</div>
print(result.text,'\n')


# 연습용 데이터 생성
html_str = """
<html>
<body>
    <ul class="great">
        <li>hello</li>
        <li>by</li>
        <li>welcome</li>
    </ul>
    <ul class="reply">
        <li>ok</li>
        <li>no</li>
        <li>sure</li>
    </ul>
</body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, 'html.parser')

# li 태그 내용을 all 찾아서 갖고오고 여러개일 경우 리스트로 갖고옴
result = bs_obj.find_all('li')
print(result)

print()

# for문을 통해 태그 속 text(내용)을 갖고옴
for li in bs_obj.find_all('li'):
    print(li.text)