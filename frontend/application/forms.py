from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class PlayerForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[DataRequired()])
    last_name = StringField(label="Last Name", validators=[DataRequired()])
    # team = SelectField(label="Team Name", choices=[], validators=[DataRequired()])
    submit = SubmitField("Add Player")

class TeamForm(FlaskForm):
    team_name = StringField(label="Team Name", validators=[DataRequired()])
    game = SelectField(label="Main Game: ", choices=[('League of Legends','League of Legends'), ('DOTA', 'DOTA'), ('CS:GO', 'CS:GO'), ('Overwatch', 'Overwatch')], validators=[DataRequired()])
    submit = SubmitField("Add Team")