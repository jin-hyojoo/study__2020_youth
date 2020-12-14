from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/pythondb'
app.config['SECRET_KEY'] = "random string"

# 서로 커뮤니케이션 하는 객체 => app.config 한 내용으로 db연결
db = SQLAlchemy(app)

# 테이블
# => 테이블 이름 DB테이블 이름과 동일하면 따로 지정 안해줘도 됨. 자동연동
# 클래스를 해당되는 테이블의 모델로 잡아야 함, db.Column => 모델에서의 테이블 컬럼만들기
class students(db.Model):
   id = db.Column('students_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200)) 
   pin = db.Column(db.String(10))

   def __init__(self, name, city, addr,pin):
      self.name = name
      self.city = city
      self.addr = addr
      self.pin = pin

# 메인뷰
@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all() )

# new 뷰 (= db insert)
@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
       # form input 빠짐없이 작성하세용
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
          # 메시지 플래싱 => 플래쉬 되는 위치는 html에서 get_flashed_messages()로 받아와 설정
         flash('Please enter all the fields', 'error')
      else:
          # form 인풋 all 작성됐으면 그 정보들 db모델로 ㄱㄱ
         student = students(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])
         
         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all() # DB초기화
   app.run(debug = True)