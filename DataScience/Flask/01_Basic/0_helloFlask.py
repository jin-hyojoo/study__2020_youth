from flask import Flask

app = Flask(__name__)

# 데코레이터 @, 한줄에 하나만 실행됨, 이벤트 처리하고 정해져 있는 룰을 알려줘야함
@app.route("/") #알아서 패스 걸어놓고 슬래쉬 뒤에 함수가 실행됨
def index():
    return 'hello Flask'

@app.route("/jhj")
def index2():
    return '<h1> Bye Flask </h1>'

if __name__ == '__main__':
    app.run()