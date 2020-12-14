from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask</h1>'

@app.route('/information')
def info():
    return '<h1>Flask is very simple </h1>'

# 임의로 변수받기
@app.route('/model/<name>')
def model(name):
    return '<h1>This is a page for {}</h1>'.format(name)

if __name__ == '__main__':
    # 포트번호 변경 해 실행
    app.run(port=1234)