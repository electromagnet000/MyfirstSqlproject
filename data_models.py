from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):

    __tablename__ = "Authors"

    id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column("Author_name",db.String(100), nullable=False)
    birth_date = db.Column("Birth_date",db.Date)
    date_of_death = db.Column("Death_date",db.Date)
    books = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f'<Author {self.name}>'



class Book(db.Model):

    __tablename__ = "Books"

    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), nullable=False)
    title = db.Column(db.String, nullable=False)
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('Authors.id'))


    def __repr__(self):
        return f'<Book {self.title}>'

