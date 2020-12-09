from bs4 import BeautifulSoup
import json

with open('1_employees.json', 'r', encoding='utf-8') as file:
    content = file.read()
    
    # json 포멧으로 인지하고 데이터 로딩
    json_data = json.loads(content)

    # 특정 데이터 지칭 (리스트, 딕셔너리 각각의 값 지정방법을 왔다갔다하면서 사용 가능)
    print(json_data["employees"]) #[{'firstName': 'John', 'lastName': 'Doe'}, {'firstName': 'Anna', 'lastName': 'Smith'}, {'firstName': 'Peter', 'lastName': 'Jones'}]
    print(json_data["employees"][0]) #{'firstName': 'John', 'lastName': 'Doe'}
    print(json_data["employees"][0]['firstName']) #John


    ''' for문 결과
        John:Doe
        Anna:Smith
        Peter:Jones
    '''
    for item in json_data['employees']:
        print(item['firstName'] + ":" + item['lastName'])
    