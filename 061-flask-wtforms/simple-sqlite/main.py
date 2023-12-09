# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/
import sqlite3
from flask import Flask
from  flask_sqlalchemy import SQLAlchemy



def main():
    # db = sqlite3.connect("books-collection.db")
    # cursor = db.cursor()
    # cursor.execute(
    #     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
    # cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
    # db.commit()

    # create the extension
    new_db = SQLAlchemy()
    # create the app
    app = Flask(__name__)
    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
    # initialize the app with the extension
    new_db.init_app(app)

    # Create class of the table
    class Book(new_db.Model):
        id = new_db.Column(new_db.Integer, primary_key=True)
        title = new_db.Column(new_db.String, unique=True, nullable=False)
        author = new_db.Column(new_db.String, nullable=False)
        rating = new_db.Column(new_db.Float, nullable=False)

    # Create table
    with app.app_context():
        new_db.create_all()

    # Create record in the table
    with app.app_context():
        new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
        new_db.session.add(new_book)
        new_db.session.commit()

    # Read all records
    with app.app_context():
        result = new_db.session.execute(new_db.select(Book).order_by(Book.title))
        all_books = result.scalars()

    # Query
    with app.app_context():
        book = new_db.session.execute(new_db.select(Book).where(Book.title == "Harry Potter")).scalar()

    # Update by query
    with app.app_context():
        book_to_update = new_db.session.execute(new_db.select(Book).where(Book.title == "Harry Potter")).scalar()
        book_to_update.title = "Harry Potter and the Chamber of Secrets"
        new_db.session.commit()

    # Update by Primary Key
    book_id = 1
    with app.app_context():
        book_to_update = new_db.session.execute(new_db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_update = db.get_or_404(Book, book_id)
        book_to_update.title = "Harry Potter and the Goblet of Fire"
        new_db.session.commit()

    # delete by PK
    book_id = 1
    with app.app_context():
        book_to_delete = new_db.session.execute(new_db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        new_db.session.delete(book_to_delete)
        new_db.session.commit()


if __name__ == "__main__":
    main()
