# request 사용 모듈 추가
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Flask</h1>'


# http://127.0.0.1:1234/search/?first=1000&second=4000
@app.route('/search/', methods=['GET'])
def serach():
    first = request.args.get('first')
    second = request.args.get('second')
    return "<h1> first={0}, second={1}</h1>".format(first, second)


if __name__ == '__main__':
    app.run(debug=True)  # 오류 시 확인