from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddJob(FlaskForm):
    job = TextAreaField('Описание работы')
    team_leader = StringField('Имя лидера', validators=[DataRequired()])
    work_size = IntegerField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Сотрудники', validators=[DataRequired()])
    is_finished = BooleanField('Завершена?')
    submit = SubmitField('Сохранить')