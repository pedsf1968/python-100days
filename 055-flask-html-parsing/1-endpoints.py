from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/hello")
def hello():
    return "Hello,World"


@app.route('/username/<username>')
def greet_user(username):
    return f"Hello {username}!"


@app.route('/username/<username>/1')
def endpoint_with_string(username):
    return f"Hello {username} with path /1!"


@app.route('/number/<int:int_number>')
def endpoint_with_integer(int_number):
    return f"The integer is: {int_number}!"


@app.route('/subpath/<path:sub_path>')
def endpoint_with_path(sub_path):
    return f"The path is: {sub_path}!"


@app.route('/age/<username>/<int:number>')
def endpoint_with_two_variables(username,number):
    return f"Hello {username} you are {number} old!"


if __name__ == '__main__':
    app.run(debug=True)
