from flask import Flask,redirect,render_template,request

from users import User

app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("users.html",users=users)


@app.route('/user/<int:id>/')
def user(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    return render_template("user.html",user=user)


@app.route('/new_user/')
def new_user():
    return render_template("new_user.html")


@app.route('/user/edit/<int:id>/')
def edit_user(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    return render_template("edit.html",user=user)


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


@app.route('/update_user/<int:id>',methods=['POST'])
def update_user(id):
    id_usuario = id
    data = {
        "id":id,
        "fname" : request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }

    User.update(data)

    return redirect('/user/'+str(id_usuario)+'/')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5500)