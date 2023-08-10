from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.form
    session['data'] = data
    print(data)
    return redirect("/result")

@app.route("/result")
def result():
    data = session.get('data', None)
    return render_template("result.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
