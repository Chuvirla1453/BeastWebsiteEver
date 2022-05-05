from flask_wtf import FlaskForm
from wtforms import DateTimeField, RadioField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed, FileField


class AddJobForm(FlaskForm):
    topic = StringField('Тема проекта', validators=[DataRequired()])
    section = RadioField('Выберите секцию', choices=['ИКТ технологии', 'ХВЗ', 'Художка', 'Физ-мат', 'Хим-био'],
                         validators=[DataRequired()])
    project = FileField('Добавить проект', validators=[FileRequired()])
    submit = SubmitField('Добавить')