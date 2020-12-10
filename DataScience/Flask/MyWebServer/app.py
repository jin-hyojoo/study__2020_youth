from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return 'Hello Virtual app'


'''
    python-dotenv 관련//
    가상환경에서 flask 실행시 .env에 설정한 환경변수를 자동으로 불러와야 하는데
    나는 안먹혀서 실행하기 전에 set FLASK_APP=start.py.. 이런식으로 지정해서 불러왔음
    원래는 set ~명령 입력없이 파일의 값만 바꿔주면 됨
'''
