import requests
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

HASH_METHOD = 'pbkdf2:sha256'
HASH_SALT_LENGTH = 8

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# Manage user login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if email exist
        result = db.session.execute(db.select(User).where(User.email == request.form["email"]))
        user = result.scalar()
        if user:
            # User exist
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        encrypted_password = generate_password_hash(password=request.form["password"],
                                      method=HASH_METHOD,
                                      salt_length=HASH_SALT_LENGTH)
        new_user = User(
            email=request.form["email"],
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            password=encrypted_password
        )
        db.session.add(new_user)
        db.session.commit()

        # Add user detail to session
        login_user(new_user)

        return redirect(url_for("secrets", user_id=new_user.id))
    else:
        return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for("secrets", user_id=user.id))
    else:
        return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    user_id = request.args.get('user_id')
    user = db.get_or_404(User, user_id)
    return render_template("secrets.html", user=user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
