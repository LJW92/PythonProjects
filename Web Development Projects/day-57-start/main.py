from flask import Flask, render_template
from datetime import datetime
import requests

AGIFY_URL = 'https://api.agify.io?name='
GENDER_URL = 'https://api.genderize.io?name='

app = Flask(__name__)


@app.route('/')
def home():
    year_now = datetime.now().year
    return render_template("index.html", year=year_now)


@app.route('/guess/<name_input>')
def guess(name_input):
    name_given = name_input.title()
    age_guess = requests.get(f"{AGIFY_URL}{name_input}").json()['age']
    gender_guess = requests.get(f"{GENDER_URL}{name_input}").json()['gender']
    return render_template("guess.html", name=name_given, age=age_guess, gender=gender_guess)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    print(num)
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
