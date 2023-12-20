from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField

class DateForm(FlaskForm):
    date = DateField('Выберите дату')
    submit = SubmitField('Узнать')