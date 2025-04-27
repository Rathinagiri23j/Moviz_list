from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    hash = db.Column(db.String(150), nullable=False)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(50))
    genre = db.Column(db.String(100))
    category = db.Column(db.String(100))
    review = db.Column(db.String(300))
    poster = db.Column(db.String(300))
