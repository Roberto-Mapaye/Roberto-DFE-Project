from flask import url_for
from flask_testing import TestCase
from application import app
from application.routes import backend
import requests_mock

test_team = {
                "team_id": 1,
                "team_name": "Esports",
                "game": "CS:GO"
            }

test_player = {
                "player_id": 1,
                "team_id": 1,
                "first_name": "SomeGuy",
                "last_name": "Smith",
            }

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

class TestViews(TestBase):
    def test_home_get(self):
        with requests_mock.Mocker() as m:
            all_teams = { "teams": [test_team] }
            m.get(f"http://{backend}/read/allTeams", json=all_teams)
            response = self.client.get(url_for('home'))
            self.assert200(response)
    
    def test_create_team_get(self):
        response = self.client.get(url_for('create_teams'))
        self.assert200(response)
    
    def test_create_player_get(self):
        response = self.client.get(url_for('create_player'))
        self.assert200(response)

    def test_update_team_get(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend}/read/team/1", json=test_team)
            response = self.client.get(url_for('update_team', id=1))
            self.assert200(response)

    def test_update_player_get(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend}/read/player/1", json=test_player)
            response = self.client.get(url_for('update_player', id=1))
            self.assert200(response)

class TestRead(TestBase):
    def test_read_home_teams(self):
        with requests_mock.Mocker() as m:
            all_teams = { "teams": [test_team] }
            m.get(f"http://{backend}/read/allTeams", json=all_teams)
            response = self.client.get(url_for('home'))
            self.assertIn(b"Test the frontend", response.data)

class TestCreate(TestBase):

    def test_create_team(self):
        with requests_mock.Mocker() as m:
            all_players = { "teams": 
                [
                    test_team,
                    {
                        "player_id": 2,
                        "team_id": 1,
                        "first_name": "Sarah",
                        "last_name": "Johnson",
                    }
                ] 
            }
            m.post(f"http://{backend}/create/teams", text="Test response")
            m.get(f"http://{backend}/read/allTeams", json=all_players)
            response = self.client.post(
                url_for('create_player'),
                json={"first_name": "Sarah"},
                follow_redirects=True
            )
            self.assertIn(b"Testing create player functionality", response.data)

    def test_create_player(self):
        with requests_mock.Mocker() as m:
            all_teams = { "players": 
                [
                    test_player,
                    {
                        "team_id": 2,
                        "team_name": "ZSports",
                        "game": "DOTA"
                    }
                ] 
            }
            m.post(f"http://{backend}/create/teams", text="Test response")
            m.get(f"http://{backend}/read/allTeams", json=all_teams)
            response = self.client.post(
                url_for('create_team'),
                json={"team_name": "ZSports"},
                follow_redirects=True
            )
            self.assertIn(b"Testing create team functionality", response.data)
    
class TestUpdate(TestBase):

    def test_update_team_name(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend}/read/team/1", json=test_team)
            m.put(f"http://{backend}/update/team/1", text="Test response")
            test_team["team_name"] = "No Sports"
            m.get(f"http://{backend}/read/allTeams", json={ "teams": [test_team] })
            response = self.client.post(
                url_for('update_teams', id=1),
                data={"team_name": "No Sports"},
                follow_redirects=True
            )
            self.assertIn(b"Testing update team name functionality", response.data)
    
    def test_update_team_sports(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend}/read/team/1", json=test_team)
            m.put(f"http://{backend}/update/team/1", text="Test response")
            test_team["game"] = "Overwatch"
            m.get(f"http://{backend}/read/allTeams", json={ "teams": [test_team] })
            response = self.client.post(
                url_for('update_teams', id=1),
                data={"game": "Overwatch"},
                follow_redirects=True
            )
            self.assertIn(b"Testing update team game functionality", response.data)
    
        

class TestDelete(TestBase):

    def test_delete_team(self):
        with requests_mock.Mocker() as m:
            m.delete(f"http://{backend}/delete/team/1")
            m.get(f"http://{backend}/read/allTeams", json={ "teams": [] })
            response = self.client.get(
                url_for('delete_teams', id=1),
                follow_redirects=True
            )
            self.assertNotIn(b"Test the team delete", response.data)
    
    def test_delete_player(self):
        with requests_mock.Mocker() as m:
            m.delete(f"http://{backend}/delete/player/1")
            m.get(f"http://{backend}/read/allTeams", json={ "teams": [] })
            response = self.client.get(
                url_for('delete_players', id=1),
                follow_redirects=True
            )
            self.assertNotIn(b"Test the player delete", response.data)