from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('04_Home.html')

@app.route('/person/<name>')
def person_name(name):
    return render_template('04_Person.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)
