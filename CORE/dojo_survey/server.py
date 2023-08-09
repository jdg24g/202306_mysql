from flask import Flask, render_template,redirect
from flask import request

app = Flask(__name__)
app.secret_key = "clave"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process',methods=['POST'])
def process():
    print(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')






if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)