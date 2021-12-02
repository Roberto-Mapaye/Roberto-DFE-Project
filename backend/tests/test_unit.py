from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Teams, Players

test_team = {
                "team_id": 1,
                "team_name": "Back Esports",
                "game": "CS:GO",
                "org": []
            }

test_player = {
                "player_id": 1,
                "team_id": 1,
                "first_name": "Back SomeGuy",
                "last_name": "Back Smith",
            }

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()
        db.session.add(Teams(team_name="Back Esports", game="CS:GO"))
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):

    def test_read_all_teams(self):
        response = self.client.get(url_for('read_all_teams'))
        all_teams = { "teams": [test_team] }
        self.assertEquals(all_teams, response.json)
    
    def test_read_team(self):
        response = self.client.get(url_for('read_team', id=1))
        self.assertEquals(test_team, response.json)
    
    def test_read_all_players(self):
        response = self.client.get(url_for('read_all_players'))
        all_players = { "players": [test_player] }
        self.assertEquals(all_players, response.json)
    
    def test_read_player(self):
        response = self.client.get(url_for('read_players', player_id=1))
        self.assertEquals(test_player, response.json)

class TestCreate(TestBase):

    def test_create_team(self):
        response = self.client.post(
            url_for('create_teams'),
            json={"team_name": "SLC", "game": "Overwatch"},
            follow_redirects=True
        )
        self.assertEquals(b"Added task with description: Testing create team functionality", response.data)
        self.assertEquals(Teams.query.get(2).team_name, "SLC")

    def test_create_player(self):
        response = self.client.post(
            url_for('create_player', team_id=1),
            json={"first_name": "Bruce", "last_name": "Wayne", "team_id":1},
            follow_redirects=True
        )
        self.assertEquals(b"Added task with description: Testing create player functionality", response.data)
        self.assertEquals(Players.query.get(2).first_name, "Bruce")

class TestUpdate(TestBase):

    def test_update_team(self):
        response = self.client.put(
            url_for('update_team', id=1),
            json={"team_name": "ChangedName Esports", "game": "CS:GO"}
        )
        self.assertEquals(b"Updated task (ID: 1) with description: ChangedName Esports", response.data)
        self.assertEquals(Teams.query.get(1).team_name, "ChangedName Esports")

    def test_update_player(self):
        response = self.client.put(
            url_for('update_player', id=1),
            json={"first_name": "ChangedName Sasha"}
        )
        self.assertEquals(b"Updated task (ID: 1) with another first name: ChangedName Sasha", response.data)
        self.assertEquals(Players.query.get(1).first_name, "ChangedName Sasha")     

class TestDelete(TestBase):

    def test_delete_team(self):
        response = self.client.delete(url_for('delete_teams', id=1))
        self.assertEquals(b"Deleted task with ID: 1", response.data)
        self.assertIsNone(Teams.query.get(1))
    
    def test_delete_player(self):
        response = self.client.delete(url_for('delete_players', id=1))
        self.assertEquals(b"Deleted task with ID: 1", response.data)
        self.assertIsNone(Players.query.get(1))