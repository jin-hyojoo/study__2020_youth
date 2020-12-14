from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Go To /mcw/name </h1>'


@app.route('/mcw/<name>')
def mcw_name(name):
    return render_template('02_TemplateVariables.html', name=name)


# 종류별로 데이터 넘겨보기 (리스트, 딕셔너리 까지)
@app.route('/mcw_name/<name>')
def mcw_role(name):
    mcw_list = list(name)
    mcw_dict = {'mcw_name': name}

    return render_template('02_T_Variables.html',
                           name=name, myList=mcw_list, myDict=mcw_dict)


if __name__ == '__main__':
    app.run(debug=True)