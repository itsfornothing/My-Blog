from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = response.json()
    return render_template('index.html', posts=all_blogs)


@app.route("/blog")
def my_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = response.json()
    for blog in all_blogs:
        if blog["id"] == 1:
            title = blog["title"]
            subtitle = blog["subtitle"]
            body = blog["body"]
            return render_template('posts.html',blog_title=title,subtitle=subtitle,body=body)

        elif blog["id"] == 2:
            title = blog["title"]
            subtitle = blog["subtitle"]
            body = blog["body"]
            return render_template('posts.html', blog_title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True,port=5001)
