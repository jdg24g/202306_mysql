from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',x=3,y=3)

@app.route('/<int:dirx>/')
def dirx(dirx):
    return render_template('index.html',x=dirx,y=3)

@app.route('/<int:dirx>/<int:diry>/')
def dirxy(dirx,diry):
    return render_template('index.html',x=dirx,y=diry)


@app.route('/<int:dirx>/<int:diry>/<string:bg_color1>/<string:bg_color2>')
def dirxycolor(dirx, diry,bg_color1, bg_color2):
    return render_template('index.html', x=dirx, y=diry, bg_color1=bg_color1, bg_color2=bg_color2)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)