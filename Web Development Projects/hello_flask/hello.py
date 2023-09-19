from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold():
        bolded = f'<b>{function()}</b>'
        return bolded
    return bold


def make_em(function):
    def em():
        emed = f'<em>{function()}</em>'
        return emed
    return em


def make_ul(function):
    def ul():
        uled = f'<u>{function()}</u>'
        return uled
    return ul


@app.route("/")
@make_bold
@make_em
@make_ul
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/username/<name>")
def greet(name):
    return f"hello {name}"


if __name__ == "__main__":
    app.run()
