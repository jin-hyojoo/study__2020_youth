def testPrint():
    print("test.py 파일 출력")

def HelloMessage(m):
    print('test.py에 등록된 HellowMessage() 함수호출')
    print(f'Hello {m}')

# 다른 파일에서 임포트해 모듈로 사용될 경우를 대비
# 메인으로 실행될때만 특정 메세지 출력하기 (모듈로써 사용되는 경우가 아니라)
if __name__ == '__main__':
    print('메인으로 실행됨')

