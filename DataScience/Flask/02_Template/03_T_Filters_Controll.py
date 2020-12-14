from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1> Go To /name </h1>'

@app.route('/<name>')
def mcw(name):
    mcw_role = ['Lee Sae Ryung', 'Sun Ok Nam', 'Cha Ji Won']
    mcw_role.append(name)
    return render_template('03_T_Filters_Controll.html',mcw_role=mcw_role)

if __name__ == '__main__':
    app.run(debug=True)





