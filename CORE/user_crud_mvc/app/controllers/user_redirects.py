# burgers.py
from app import app
from flask import render_template,redirect,request,session,flash
from app.models.users import User



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


@app.route('/delete_user/<int:id>/')
def delete_user(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect('/')