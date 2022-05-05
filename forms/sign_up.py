from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired


class SignUpForm(FlaskForm):
    section = RadioField('Выберите секцию', choices=['ИКТ технологии', 'ХВЗ', 'Художка', 'Физ-мат', 'Хим-био'],
                         validators=[DataRequired()])
    submit = SubmitField('Выбрать')
