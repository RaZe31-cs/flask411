from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField, IntegerField, RadioField
from wtforms.validators import DataRequired


class AddJob(FlaskForm):
    job = TextAreaField('Описание работы')
    team_leader = StringField('Имя лидера', validators=[DataRequired()])
    work_size = IntegerField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Сотрудники', validators=[DataRequired()])
    hazard = RadioField('Категория опасности?', choices=['Безопасно', 'Средняя опасность', 'Опасно'])
    is_finished = BooleanField('Завершена?')
    submit = SubmitField('Сохранить')