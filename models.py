from flask_login import UserMixin

from application import db, manager


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)

    def __init__(self, text, tags):
        self.text = text.strip()
        self.tags = [
            Tag(text=tag.strip()) for tag in tags.split(',')
        ]


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', backref=db.backref('tags', lazy=True))


class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


class Admin1kino (db.Model, UserMixin):
    login = db.Column(db.String(128), primary_key=True, nullable=False )
    password = db.Column(db.String(255), nullable=False)


class Genre(db.Model):
    Genre_name = db.Column(db.String(200), primary_key=True)


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FIO = db.Column(db.String(150), nullable=False)
    Data_born = db.Column(db.String(80), nullable=False)
    Data_death = db.Column(db.String(80))


class Reputation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year_preview = db.Column(db.String(80), unique=True, nullable=False)
    name_film = db.Column(db.String(80), unique=True, nullable=False)

    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)
    director = db.relationship('Director', backref=db.backref('reputat', lazy=True))


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FIO = db.Column(db.String(150), nullable=False)
    Data_born = db.Column(db.String(8), nullable=False)
    Data_death = db.Column(db.String(8))
    # CHECK (Дата_жизни < Дата_смерти)


class Name_film(db.Model):
    name = db.Column(db.String(100), primary_key=True, nullable=False)
    year_preview = db.Column(db.String(100), unique=True, nullable=False)
    plot = db.Column(db.Text, nullable=False)
    Year_exit = db.Column(db.String(100), nullable=False)


class Country(db.Model):
    name = db.Column(db.String(80), primary_key=True, nullable=False)


class Filter(db.Model):
    Genre = db.Column(db.Integer, primary_key=True)
    film_name = db.Column(db.String(100), unique=True, nullable=False)
    Year_exit = db.Column(db.String(100), unique=True, nullable=False)


class Rating(db.Model):
    grade = db.Column(db.Integer, primary_key=True)
    Review = db.Column(db.Integer)
    Data_time = db.Column(db.Integer)
    login = db.Column(db.Integer)
    Year_exit = db.Column(db.Integer)
    Name_film = db.Column(db.Integer)


class Ocenka_recenz(db.Model):
    Score = db.Column(db.Integer, primary_key=True)
    Data_time = db.Column(db.Integer)
    login = db.Column(db.Integer)
    Year_exit = db.Column(db.Integer)
    Name_film = db.Column(db.Integer)
    Username_author = db.Column(db.Integer)


class Premiere(db.Model):
    country_creator = db.Column(db.String(80), primary_key=True, nullable=False)
    data_preview = db.Column(db.Integer, nullable=False)
    name_film = db.Column(db.String(120), unique=True, nullable=False)
    year_preview = db.Column(db.String(120), unique=True, nullable=False)


class Maker(db.Model):
    name_film = db.Column(db.String(80), primary_key=True, nullable=False)
    country = db.Column(db.String(80), unique=True, nullable=False)
    year_preview = db.Column(db.String(80), unique=True, nullable=False)


class Professionalism(db.Model):
    id_Actor = db.Column(db.Integer, primary_key=True)
    Genre = db.Column(db.String(80), unique=True, nullable=False)


class Role(db.Model):
    id_Actor = db.Column(db.Integer, primary_key=True, nullable=False)
    name_role = db.Column(db.String(80), unique=True, nullable=False)
    name_film = db.Column(db.String(80), unique=True, nullable=False)
    year_preview = db.Column(db.String, unique=True, nullable=False)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
