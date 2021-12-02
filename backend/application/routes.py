from application import app, db
from application.models import Players, Teams
from flask import render_template, request, redirect, url_for, jsonify, Response
from os import getenv

@app.route('/read/allTeams', methods=['GET'])
def read_all_teams():
    all_teams = Teams.query.all()
    teams_dict = {"teams": []}
    for teams in all_teams:
        players = []
        for player in teams.org:
            players.append(
                {
                    "player_id": player.player_id,
                    "first_name": player.first_name,
                    "last_name": player.last_name
                }
            )
        teams_dict["teams"].append(
            {
                "team_id": teams.team_id,
                "team_name": teams.team_name,
                "game": teams.game,
                "org": players
            }
        )
    return jsonify(teams_dict)

@app.route('/read/allPlayers', methods=['GET'])
def read_all_players():
    all_teams = Teams.query.all()
    teams_dict = {"teams": []}
    for teams in all_teams:
        players = []
        for player in teams.org:
            players.append(
                {
                    "player_id": player.player_id,
                    "first_name": player.first_name,
                    "last_name": player.last_name
                }
            )
        teams_dict["teams"].append(
            {
                "team_id": teams.team_id,
                "team_name": teams.team_name,
                "game": teams.game,
                "org": players
            }
        )
    return jsonify(players)

@app.route('/read/team/<int:id>', methods=['GET'])
def read_team(id):
    teams = Teams.query.get(id)
    teams_dict = {
                    "team_id": teams.team_id,
                    "team_name": teams.team_name,
                    "game": teams.game
                }
    return jsonify(teams_dict)

@app.route('/read/player/<int:id>', methods=['GET'])
def read_players(id):
    player = Players.query.get(id)
    player_dict = {
        "player_id": player.player_id,
        "team_id": player.team_id,
        "first_name": player.first_name,
        "last_name": player.last_name
    }
    return jsonify(player_dict)


# == ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==

@app.route('/create/player/<int:team_id>', methods=['POST'])
def create_player(team_id):
    package = request.json
    new_player = Players(first_name=package["first_name"], last_name=package["last_name"], team_id=team_id)
    db.session.add(new_player)
    db.session.commit()
    return f"Moon '{new_player.first_name}' added to database"

@app.route('/create/teams', methods=['POST'])
def create_teams():
    package = request.json
    new_teams = Teams(team_name=package["team_name"], game=package["game"])
    db.session.add(new_teams)
    db.session.commit()
    return f"Planet '{new_teams.team_name}' added to database"

# == DELETE DATA ROUTES ==== DELETE DATA ROUTES ==== DELETE DATA ROUTES ==== DELETE DATA ROUTES ==

@app.route('/delete/player/<int:id>', methods=['DELETE'])
def delete_players(id):
    player = Players.query.get(id)
    db.session.delete(player)
    db.session.commit()
    return Response(f"Deleted task with ID: {id}", mimetype='text/plain')

@app.route('/delete/team/<int:id>', methods=['DELETE'])
def delete_teams(id):
    teams = Teams.query.get(id)
    db.session.delete(teams)
    db.session.commit()
    return Response(f"Deleted task with ID: {id}", mimetype='text/plain')

# == UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==

@app.route('/update/player/<int:id>', methods=['PUT'])
def update_player(id):
    package = request.json
    change_player = Players.query.get(id)
    change_player.first_name = package["first_name"]
    change_player.last_name = package["last_name"]
    # change_player.team_id = team_id
    db.session.commit()
    return Response(f"Updated task (ID: {id}) with description: {change_player.first_name}", mimetype='text/plain')

@app.route('/update/team/<int:id>', methods=['PUT'])
def update_team(id):
    package = request.json
    team = Teams.query.get(id)
    team.team_name = package["team_name"]
    team.game = package["game"]
    db.session.commit()
    return Response(f"Updated task (ID: {id}) with description: {team.team_name}", mimetype='text/plain')