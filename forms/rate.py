from flask_wtf import FlaskForm
from wtforms import DateTimeField, RadioField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, NumberRange


class RateForm(FlaskForm):
    a1 = IntegerField('Обоснованность темы работы', validators=[DataRequired(), NumberRange(min=0, max=2)])
    a2 = IntegerField('Конкретность, ясность формулировки цели и задач', validators=[DataRequired(), NumberRange(min=0, max=2)])
    a3 = IntegerField('Обоснованность выбора методики работы  ', validators=[DataRequired(), NumberRange(min=0, max=4)])
    a4 = IntegerField('Исследовательский характер работы', validators=[DataRequired(), NumberRange(min=0, max=5)])
    a5 = IntegerField('Наглядность  представления результатов', validators=[DataRequired(), NumberRange(min=0, max=1)])
    a6 = IntegerField('Конкретность выводов и уровень обобщения ', validators=[DataRequired(), NumberRange(min=0, max=2)])
    a7 = IntegerField('Оригинальность позиции автора ', validators=[DataRequired(), NumberRange(min=0, max=2)])
    a8 = IntegerField('Соответствие выводов содержанию цели и задач', validators=[DataRequired(), NumberRange(min=0, max=2)])
    a9 = IntegerField('Оформление работы', validators=[DataRequired(), NumberRange(min=0, max=2)])
    a10 = IntegerField('Библиография', validators=[DataRequired(), NumberRange(min=0, max=1)])
    submit = SubmitField('Добавить')