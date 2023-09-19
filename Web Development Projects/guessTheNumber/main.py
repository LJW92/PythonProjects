from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0, 9)


@app.route("/")
def main_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route("/<int:user_guess>")
def guess(user_guess):
    if user_guess < number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb21rdWVjNTluanEwdDgycTJ3amV4aWt2dW85MmhvajQ5cTZuZjh4dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fvBEGznNx4VhchaIgb/giphy.gif'></img>"
    elif user_guess > number:
        return "<h1 style='color: blue'>Too high, try again!</h1>" \
               "<img src = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTJncDUxbXprejNraGtjM2JiYmNhdXBydmdtY2l5MnB2Nmg0eXR0aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2JhAgiGSvMordxQs/giphy.gif'></img>"

    else:
        return "<h1>You found me!</h1>" \
               "<img src = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTdxcHA3b3ltZXFmcnJpa3J0aDRuNW40aTYxbGI4ZGdjcTZwdjdxYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/elsol3P5Jt2ASsxLva/giphy-downsized-large.gif'></img>"


if __name__ == "__main__":
    app.run()
