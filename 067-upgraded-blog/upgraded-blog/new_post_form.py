from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, IntegerField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class NewPostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = URLField(label="Blog Image Url", validators=[DataRequired(), URL()])
    body = CKEditorField(label='Blog Content')
    submit = SubmitField('Submit')
