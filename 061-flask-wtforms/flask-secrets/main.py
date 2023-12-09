# python -m pip install -r requirements.txt

from flask import Flask, render_template, redirect, request
from form import LoginForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = 'my super secret key'.encode('utf8')
bootstrap = Bootstrap5(app)


def valid_credentials(email, password):
    if email == "admin@email.com" and password == "12345678":
        return True
    return False


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login_endpoint():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if valid_credentials(login_form.email.data, login_form.password.data):
            return redirect("/success")
        else:
            return redirect("/denied")
    return render_template(template_name_or_list="login.html", form=login_form)

@app.route("/success")
def success_endpoint():
    return render_template(template_name_or_list="success.html")


@app.route("/denied")
def denied_endpoint():
    return render_template(template_name_or_list="denied.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
