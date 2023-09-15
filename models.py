from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


"""Models for Adoption Agency."""


class Pet(db.Model):
    def __repr__(self):
        """Show info about Pet"""
        u = self
        return f"Pet"

    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(
        db.Text,
        nullable=False,
    )
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=False)
    available = db.Column(db.Boolean, default=True)
