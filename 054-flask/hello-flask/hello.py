# flask --app hello.py run

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/bye")
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run()
