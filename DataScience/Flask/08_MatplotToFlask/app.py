import io
import random
from flask import Flask, Response, request, render_template

# 파이썬에서 차트를 위젯으로 사용하기 위해 위젯 클래스 갖고오기
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

app = Flask(__name__)

@app.route('/')
def index():
    num_x_points = int(request.args.get('num_x_points',50))
    return render_template('index.html', num_x_points=num_x_points )

@app.route('/matplot-as-image-<int:num_x_points>.png')
def plot_png(num_x_points=50):
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    x_points = range(num_x_points)
    axis.plot(x_points,[random.randint(1,30) for x in x_points])

    # 페이지 끼리 데이터 주고받기 위해선 바이트타입으로의 변환필요
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
