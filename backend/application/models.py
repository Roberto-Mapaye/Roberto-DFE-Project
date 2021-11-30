from application import db

class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column('team_id', db.Integer, db.ForeignKey('teams.team_id'))
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    
class Teams(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(30), nullable=False)
    game = db.Column(db.String(30), nullable=False)
