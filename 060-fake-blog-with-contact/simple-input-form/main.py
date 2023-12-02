# https://www.w3schools.com/tags/att_form_method.asp
# https://www.w3schools.com/tags/att_form_action.asp
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#http-methods
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#the-request-object
# https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home_endpoint():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login_endpoint():
    if request.method == 'POST':
        name = request.form["username"]
        password = request.form["password"]
        return f"<h1>Name: {name}, Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
