from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError


def validate_password(form, field):
    if len(field.data) < 8:
        raise ValidationError('Field must be at least 8 characters!')


def validate_email(form, field):
    if '@' not in str(field.data):
        raise ValidationError('Field must be a valid email!')


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), validate_email])
    password = PasswordField(label='Password', validators=[DataRequired(), validate_password])
    submit = SubmitField(label='Log In')


