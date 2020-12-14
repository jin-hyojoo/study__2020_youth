# request 사용 모듈 추가
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

def about():
    return 'This is about page'
app.add_url_rule('/about', "about", about)

if __name__ == '__main__':
    app.run(debug=True) 