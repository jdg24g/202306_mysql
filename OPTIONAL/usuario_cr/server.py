from flask import Flask,redirect,render_template,request

from users import User

app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("users.html",users=users)

@app.route('/new_user/')
def new_user():
    return render_template("new_user.html")


@app.route('/add_user',methods=['POST'])
def add_user():
    print(request.form)
    data = {
        "fname" : request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }

    User.save(data)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5500)