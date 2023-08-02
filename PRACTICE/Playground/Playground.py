from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def print_hola():
    return 'Hola Mundo!'

@app.route('/play/')
def nivel_uno():
    return render_template("index.html",num=3,color="red",tittle="Nivel Uno")


@app.route("/play/<int:num>/")
def nivel_dos(num):
    return render_template("index.html", num=num, color="red",tittle="Nivel Dos")


@app.route("/play/<int:num>/<string:color>/")
def nivel_tres(num, color):
    return render_template("index.html", num=num, color=color,tittle="Nivel Tres")

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html')


if __name__ == '__main__':
    app.run( debug=True,host='0.0.0.0',port=5000)