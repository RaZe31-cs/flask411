from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    chief = StringField('Главный', validators=[DataRequired()])
    members = StringField('Сотрудники', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Сохранить')