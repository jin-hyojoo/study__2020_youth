'''
    COOKIE : 클라이언트의 PC에 텍스트 파일 형태로 저장. 일정시간 지나면 소멸
    SESSION : 서버 메모리에 저장 
'''
from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

# 브라우저에 저장
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
        # 이름 nm인 form 찾아와 값 저장 
        user = request.form['nm']
   
   # make_response() => 사용자에게 반환할 뷰 함수를 생성후, 그대로 묶어둠 (뷰 로딩 전, 쿠키를 생성해야 하기 때문에)
   # - 딕셔너리를 튜플로 전송할 수 있게 함 (데이터 오류 방지)
   # - user의 응답내용을 쿠키로 생성하기 전에 해당 페이지에 담아두려고 묶어두기(?) 
   resp = make_response(render_template('readcookie.html'))
   
   # 묶어놓은 페이지에 쿠키값 세팅 (userID라는 이름으로)
   resp.set_cookie('userID', user)
   return resp # 리턴하게되면 묶어놓은 페이지에 쿠키값 담긴 채로 !


# 쿠키 갖고오기
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'
   
if __name__ == '__main__':
   app.run(debug = True)