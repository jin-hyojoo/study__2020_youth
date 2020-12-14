from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

# html form에서 보낸 데이터 result.html로 전달
# 즉, method post의 결과를 result에 담아 result.html로 전달
@app.route('/result', methods=['POST', 'GET'])
def reulst():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)
