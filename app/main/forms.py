from ast import Sub
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField("Title",validators=[DataRequired()])
    body = CKEditorField("Body",validators=[DataRequired()])
    submit = SubmitField("Publish",validators=[DataRequired()])