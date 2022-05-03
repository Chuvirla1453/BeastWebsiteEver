from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired, NumberRange, AnyOf


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    klasse = IntegerField('Класс', validators=[DataRequired(), NumberRange(min=5, max=10,
                                                                           message='целое число от 5 до 10')])
    position = StringField('Должность (ученик или проверяющий)', validators=[DataRequired(),
                                                                             AnyOf(['Ученик', 'Проверяющий'])])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])

    submit = SubmitField('Зарегистрироваться')