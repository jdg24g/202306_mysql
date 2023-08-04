from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'holamundo'


@app.route('/')
def index():
    if 'contador' in session:
        return render_template('index.html', numero=session['contador'])
    else:
        return render_template('index.html', numero=0)

@app.route('/sumar')
def sumar():
    if 'contador' in session:
        session['contador'] += 1
    else:
        session['contador'] = 1
    return redirect('/')

@app.route('/x2')
def x2():
    if 'contador' in session:
        session['contador'] += 2
    else:
        session['contador'] = 2
    return redirect('/')

@app.route('/reset')
def borrar():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')