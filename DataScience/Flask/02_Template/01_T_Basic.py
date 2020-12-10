''' 
    render_template =>  템플릿을 실행하라
    현 플젝 위치에 template폴더가 있어야 하고 그 폴더에 render할 파일이 있어야 찾아서 읽을 수 있음
    static폴더엔 보통 수정할 일 없는 리소스 파일을 넣음
 '''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('01_T_Basic.html')
    
if __name__ == '__main__':
    app.run(debug=True)