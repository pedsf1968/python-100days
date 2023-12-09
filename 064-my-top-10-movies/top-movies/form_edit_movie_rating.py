from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, ValidationError


def validate_rating(form, field):
    if field.data > 10.0 or field.data < 0.0:
        raise ValidationError("Rating must be between 0 and 10")


class MovieEditRatingForm(FlaskForm):
    rating = FloatField(label="Your Rating  Out of 10 e.g.7.5", validators=[DataRequired(), validate_rating])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label='Done')
