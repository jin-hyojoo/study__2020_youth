from flask import Flask , session, redirect, url_for, escape,request

app = Flask(__name__)
app.secret_key="any random string"
@app.route('/')
def index():
    # 세션에 username 있니..?
    if 'username' in session:
        username = session['username'] # 넘어온 세션값을 username변수에 담음
        return 'Logged in as ' + username + '<br>' +\
            "<b><a href = '/logout'> click here to logout </a></b>" #/logout 이동
    # 없으면 로그인이나 해!
    return "You not logged in <br><a href = '/login'> click here to login </a></b>" # /login이동


@app.route('/login' , methods=['GET','POST'])
def login():
    if request.method=='POST': # post요청이 있다면 (화면에서 form이 제출 됐다면)
        session['username'] = request.form['username'] #form의 username값을 세션 username에 넣음 
        return redirect(url_for('index')) # 세션값 품은 채로 /index 화면 이동
    return '''
    <form action = "" method="post">
      <p><input type="text" name="username"/></p>
      <p> <input type="submit" value="Login"/></p>
    </form>	
   '''
@app.route('/logout')
def logout():
    session.pop('username', None) # 세션 끊기
    return redirect(url_for('index')) #다시 인덱스() 화면 띄우기
    
if __name__ == '__main__':
    app.run()