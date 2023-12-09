from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from form_edit_movie_rating import MovieEditRatingForm
from form_add_movie import MovieAddForm
from form_find_movie import MovieFindForm
from tmdb import tmdb_get_movies, tmdb_get_movie_details
from pprint import pprint

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, primary_key=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


def create(title: str, year: int, description: str, rating: float, ranking: int, review: str, img_url: str):
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        rating=rating,
        ranking=ranking,
        review=review,
        img_url=img_url
    )
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    rank = 1
    for movie in all_movies[::-1]:
        movie.ranking = rank
        rank += 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["POST", "GET"])
def add_movie():
    add_form = MovieFindForm()

    if add_form.validate_on_submit():
        movie_title = add_form.title.data
        data = tmdb_get_movies(movie_title)
        return render_template("select.html", options=data)
    return render_template("add.html", form=add_form)


@app.route("/find")
def find_movie():
    tmdb_movie_id = request.args.get("id")
    if tmdb_movie_id:
        movie_data = tmdb_get_movie_details(movie_id=tmdb_movie_id)
        new_movie = Movie(title=movie_data['title'],
                          year=movie_data['release_date'].split('-')[0],
                          description=movie_data['overview'],
                          img_url=f"https://image.tmdb.org/t/p/w500/{movie_data['poster_path']}",
                          )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit_rating', id=new_movie.id))

@app.route("/edit", methods=["GET", "POST"])
def edit_rating():
    rating_form = MovieEditRatingForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if rating_form.validate_on_submit():
        movie.rating = float(rating_form.rating.data)
        movie.review = rating_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=rating_form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    # create(title="Phone Booth",
    #        year=2002,
    #        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #        rating=7.3,
    #        ranking=10,
    #        review="My favourite character was the caller.",
    #        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")
    # create(title="Avatar The Way of Water",
    #        year=2022,
    #        description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #        rating=7.3,
    #        ranking=9,
    #        review="I liked the water.",
    #        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg")
    app.run(debug=True)

