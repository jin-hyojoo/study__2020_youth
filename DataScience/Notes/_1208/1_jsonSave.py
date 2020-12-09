import json

# json 데이터 생성
dic_data = {'Name':'Jane', 'Age':43, 'Class':'Thrid'}

with open('result.json', 'w') as jsonFile:
    # dic_data의 json 내용을 jsonFile에 담겠다
    #result.json으로 파일이 생성됨
    json.dump(dic_data, jsonFile)
    
    
'''
    json.dump는 저장
    json.read는 읽기
'''
    