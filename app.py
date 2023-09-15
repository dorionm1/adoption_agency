"""Adoption Agency application."""

from flask import Flask, render_template, redirect
from models import db, connect_db, Pet
from flask_sqlalchemy import SQLAlchemy
from forms import AddPetForm


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.secret_key = "secret_key"

connect_db(app)

with app.app_context():
    db.create_all()


@app.route("/")
def show_list():
    """Shows list of all pets"""
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)


@app.route("/add")
def add_pet_form():
    """Show for for adding pet"""
    form = AddPetForm()

    return render_template("add_pet.html", form=form)


@app.route("/add_pet", methods=["GET", "POST"])
def create_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            age=form.age.data,
            photo_url=form.photo_url.data,
            notes=form.notes.data,
        )

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")

    return render_template("add_pet.html", form=form)
