from application import db

class Organisation(db.Model):
    org_id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column('team_id', db.Integer, db.ForeignKey('Teams.team_id'))
    player_id = db.Column('player_id', db.Integer, db.ForeignKey('Players.player_id'))
    description = db.Column(db.String(30), nullable=False)

class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class Teams(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    games_played = db.Column(db.Boolean, nullable=False, default=False)
