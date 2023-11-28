# to edit web page on browser document.body.contentEditable=true

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello(name=None):
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
