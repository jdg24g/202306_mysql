
from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/')
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html',title='Dojo Ninjas',dojos=dojos)

@app.route('/new_dojo/',methods=['POST'])
def new_dojo():
    data = {
        "name": request.form['name']
    }
    Dojo.save(data)

    return redirect('/')

@app.route('/ninja_form/')
def ninja_form():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('ninja_form.html', title='Ninja Form',dojos=dojos)


@app.route('/new_ninja/',methods=['POST'])
def new_ninja():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    Ninja.save(data)

    return redirect('/')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_one(data)
    print(dojo)
    ninjas_from_dojo = Ninja.get_all_from_dojo(data)

    return render_template('dojo_ninja.html',dojo=dojo,ninjas=ninjas_from_dojo,title="Dojo")