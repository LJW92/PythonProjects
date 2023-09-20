from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)
api = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(api)
all_post = response.json()
posts_obj = []
for post in all_post:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts_obj.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", post=posts_obj)


@app.route('/post/<num>')
def post(num):
    int_num = int(num)
    int_num -= 1

    return render_template("post.html", post_obj=posts_obj[int_num])


if __name__ == "__main__":
    app.run(debug=True)
