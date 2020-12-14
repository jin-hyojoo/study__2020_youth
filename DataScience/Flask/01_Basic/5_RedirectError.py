

#HTTP_300_MULTIPLE_CHOICES
#HTTP_301_MOVED_PERMANENTLY
#HTTP_302_FOUND
#HTTP_303_SEE_OTHER
#HTTP_304_NOT_MODIFIED
#HTTP_305_USE_PROXY
#HTTP_306_RESERVED
#HTTP_307_TEMPORARY_REDIRECT




from flask import Flask, redirect, url_for, render_template, request
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('log_in.html')

@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST' and request.form['username'] == 'admin' :
      return redirect(url_for('success'))
   else:
      return redirect(url_for('index'))

@app.route('/success')
def success():
   return 'logged in successfully'
	
if __name__ == '__main__':
   app.run(debug = True)