from flask import Flask

app = Flask(__name__)

# 데코레이터 @, 한줄에 하나만 실행됨, 이벤트 처리하고 정해져 있는 룰을 알려줘야함
# =>  애플리케이션에 어떤 URL가 호출해야 하는 연관된 함수를 요청
@app.route("/") #알아서 패스 걸어놓고 슬래쉬 뒤에 함수가 실행됨
def index():
    return 'hello Flask'

@app.route("/jhj")
def index2():
    return '<h1> Bye Flask </h1>'

# app.add_url_rule() 함수로  = app.route()와 동일한 기능
def hello_world():
       return 'hello world'
app.add_url_rule('/hello', 'hello_world', hello_world)

if __name__ == '__main__':
    app.run()