import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # form의 value들 갖고오기
    features = [int(x) for x in request.form.values()]
    # 2차원 배열
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    target_names = ['setosa', 'versicolor', 'virginica']

    output = target_names[prediction[0]]
    print(output)
    return render_template('index.html', prediction_text='Your IRIS is: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)