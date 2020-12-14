# request 사용 모듈 추가
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/'

@app.route('/upload')
def index():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename)) # 어느 위치에 저장할 건지
        return 'file upload success'

if __name__ == '__main__':
    app.run(debug=True) 