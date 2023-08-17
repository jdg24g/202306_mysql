from flask import Flask,redirect,render_template,request

from friend import Friend

app = Flask(__name__)

@app.route('/')
def index():

    friends = Friend.get_all()
    print(friends)
    return render_template("index.html",friends=friends)

@app.route('/create_friend',methods=['POST'])
def create_friend():
    data = {
        "fname" : request.form["fname"],
        "lname": request.form["lname"],
        "occ" : request.form["occ"]
    }

    Friend.save(data)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5500)