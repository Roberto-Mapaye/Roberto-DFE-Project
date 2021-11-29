from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PlayerForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    second_name = StringField("Second Name", validators=[DataRequired()])
    team = StringField("Team Name", validators=[DataRequired()])
    submit = SubmitField("Add Task")

class TeamForm(FlaskForm):
    team_name = StringField("Team Name", validators=[DataRequired()])
    submit = SubmitField("Add Task")