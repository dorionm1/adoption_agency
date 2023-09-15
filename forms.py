from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, ValidationError
from wtforms.validators import InputRequired, URL, Optional


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    def validate_age(form, field):
        if (field.data) > 30 or (field.data) < 0:
            raise ValidationError("Age must be between 0 and 30")

    name = StringField("Name", validators=[InputRequired(message="*")])
    species = SelectField(
        "Speices",
        validators=[InputRequired(message="*")],
        choices=[("Cat"), ("Dog"), ("Porcupine")],
    )
    photo_url = StringField(
        "Photo URL", validators=[URL(require_tld=True), Optional(strip_whitespace=True)]
    )
    age = FloatField("Age", validators=[InputRequired(message="*"), validate_age])
    notes = StringField("Notes", validators=[InputRequired(message="*")])
