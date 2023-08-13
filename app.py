import sqlalchemy
import jinja2
from flask import Flask, render_template, request, redirect, url_for, session, g, flash
from datetime import datetime
from data_models import Author, db, Book



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Sergiu Howie/PycharmProjects/pythonProject8/MyfirstSqlproject/data/library.sqlite'

db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def home():

    books_query = Book.query.all()
    sort_option = "default"

    if request.method == 'POST':
        search_query = request.form['search_query']
        books_query = Book.query.filter(Book.title.ilike(f"%{search_query}%"))
        sort_option = request.form.get('sort_option', 'default')

        if sort_option == 'title_asc':
            books_query = books_query.order_by(Book.title.asc())
        elif sort_option == 'title_desc':
            books_query = books_query.order_by(Book.title.desc())

        books = books_query.all()

        return render_template('home.html', books=books, sort_option=sort_option)

    books = books_query

    return render_template('home.html', books=books, sort_option=sort_option)


@app.route("/add_author", methods=["GET", "POST"])
def add_author():
    """ gets list of all authors objects in database"""
    authors = Author.query.all()
    if request.method == "POST":
        """ makes Author object """
        new_author = Author(
            name=request.form['name'],
            birth_date= datetime.strptime(request.form['birth_date'], '%Y-%m-%d').date()
        )
        """ if no date on death then object will appoint none otherwise date will be filled in """
        if request.form['date_of_death']:
            new_author.date_of_death = datetime.strptime(request.form['date_of_death'], '%Y-%m-%d').date()
        else:
            new_author.date_of_death = None

        db.session.add(new_author)
        db.session.commit()

        authors = Author.query.all()
        return render_template("add_author.html", message="successfully added author", authors=authors)
    return render_template("add_author.html", authors=authors)

@app.route("/add_books", methods=["GET", "POST"])
def add_books():

    books = Book.query.all()
    authors = Author.query.all()

    if request.method == "POST":

        book_obj = Book(
            title=request.form['title'],
            isbn=request.form['isbn'],
            publication_year=request.form['publication_year'],
            author_id=request.form['author_id']
        )

        db.session.add(book_obj)
        db.session.commit()

        books = Book.query.all()
        authors = Author.query.all()

        return render_template("add_books.html", books=books, message="successfully added book", authors=authors)
    return render_template("add_books.html", books=books, authors=authors)

@app.route("/book/<int:book_id>/delete", methods=["POST"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)




