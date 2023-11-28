# Guess age and gender of a name
# https://updateyourfooter.com/
# Jinja : https://jinja.palletsprojects.com/en/2.11.x/templates/
# Flask : https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing
import random
import requests
import json
from flask import Flask, render_template
from datetime import datetime

# Agify : https://agify.io/
AGIFY_URL = "https://api.agify.io"
AGIFY_COUNTRY = "FR"

# Genderize : https://genderize.io/
GENDERIZE_URL = "https://api.genderize.io/"
GENDERIZE_COUNTRY = AGIFY_COUNTRY

app = Flask(__name__)


@app.route('/')
def home_endpoint():
    return render_template("index.html",
                           random_number=random.randint(1, 10),
                           current_year=datetime.now().year)


@app.route('/guess/<user_name>')
def guess_gender(user_name):
    endpoint = f"{AGIFY_URL}?name={user_name}&country_id={AGIFY_COUNTRY}"
    user_age = requests.get(url=endpoint).json()

    endpoint = f"{GENDERIZE_URL}?name={user_name}&country_id={GENDERIZE_COUNTRY}"
    user_gender = requests.get(url=endpoint).json()
    return render_template("guess.html",
                           name=user_name,
                           age=user_age,
                           gender=user_gender,
                           current_year=datetime.now().year)


@app.route('/blog')
def get_blog():
    # Blog : https://www.npoint.io/
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()

    return render_template("blog.html",
                           posts=all_posts,
                           current_year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)
