from application import db

class Teams(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(30), nullable=False)
    game = db.Column(db.String(50), nullable=False)
    org = db.relationship('Players', backref='org', lazy=True)

class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)