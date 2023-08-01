from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo"

@app.route("/dojo")
def dojo():
    return "¡Dojo!"

@app.route("/say/flask")
def say_flask():
    return "¡Hola Flask!"

@app.route("/say/michael")
def say_Michael():
    return "¡Hola Michael!"

@app.route("/say/jhon")
def say_Jhon():
    return "¡Hola Jhon!"



def repetir_mensaje(message, times):
    return f"{message} " * times


@app.route('/repeat/<int:times>/<message>')
def repetir(times, message):
    return repetir_mensaje(message, times)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000,host='0.0.0.0')