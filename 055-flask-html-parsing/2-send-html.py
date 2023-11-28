# https://giphy.com/
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


# Send directly HTML with CSS
@app.route("/hello")
def hello():
    return ('<h1 style="text-align: center">Hello,World</h1>'
             '<p>This is a paragraph.</p>'
             '<img src="https://media0.giphy.com/media/1xONIE9kieqf4VTX50/giphy.webp?cid=ecf05e471hjc1wy0nlwrue3ks8ua6412jak6pks6xv533k5w&ep=v1_gifs_search&rid=giphy.webp&ct=g" width=200>')


if __name__ == '__main__':
    app.run(debug=True)