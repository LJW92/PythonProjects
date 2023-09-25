from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    username = request.form['name']
    user_password = request.form['password']
    return f"<h1> name:{username} password:{user_password} </h1>"


if __name__ == '__main__':
    app.run()
