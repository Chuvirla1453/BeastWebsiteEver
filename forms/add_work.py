from flask_wtf import FlaskForm
from wtforms import DateTimeField, BooleanField, SubmitField, IntegerField, StringField, FileField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    topic = StringField('Тема проекта', validators=[DataRequired()])
    project = FileField('Добавить проект', validators=[DataRequired()])
