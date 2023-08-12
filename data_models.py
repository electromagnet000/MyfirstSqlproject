
class Authors(db.model):
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.String, unique=True, nullable=False)
    birth_date = db.Column("Date_of_birth", db.String)
    death_date = db.Column("Date_of_death", db.String)

