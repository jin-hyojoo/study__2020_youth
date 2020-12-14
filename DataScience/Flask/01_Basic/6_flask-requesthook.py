from flask import Flask

app = Flask(__name__)
@app.route("/")
def http_my_response():
    return "/"

@app.before_first_request
def before_first_request():
    print("앱 기동하고 맨처음 요청만 응답")
@app.before_request
def before_request():
    print("매 요청마다 실행")

@app.after_request
def after_request(response):
    print ("매 요청 처리되고 나서 실행")
    return response

@app.teardown_request
def teardown_request(exception):
    return "브라우저가 응답하고 실행"

@app.teardown_appcontext
def teardown_request(exception):
    print("HTTP 요청 애플리케이션 컨텍스트가 종료될때 실행")


if __name__ == "__main__":
    app.run()