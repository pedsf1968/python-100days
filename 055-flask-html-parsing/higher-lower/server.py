from flask import Flask
from number import Number


app = Flask(__name__)
number = Number()


@app.route("/")
def home():
    return number.reset_number()


@app.route("/<int:value>")
def guess(value):
    return number.verify(number=value)


@app.route("/reset/<int:value>")
def reset(value):
    return number.reset_number(max_range=value)


if __name__ == "__main__":
    app.run()
