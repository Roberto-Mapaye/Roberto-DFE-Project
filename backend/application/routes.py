from application import app, db
from application.models import Players, Teams
from flask import render_template, request, redirect, url_for, jsonify
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
def read_all_players(id):
    all_players = Players.query.all()
    players_dict = {"players": []}
    for players in all_players:
        players_dict["players"].append(
            {
                "player_id": players.player_id,
                "team_id": players.team_id,
                "first_name": players.first_name,
                "last_name": players.last_name
            }
        )
    return jsonify(player_dict)

@app.route('/read/teams/<int:id>', methods=['GET'])
def read_team(id):
    teams = Teams.query.get(id)
    teams_dict = {
                    "team_id": teams.team_id,
                    "team_name": teams.team_name,
                    "game": teams.game,
                }
    return jsonify(teams_dict)

@app.route('/read/teams/<int:id>/players', methods=['GET'])
def read_players(id):
    player = Players.query.get(id)
    players_dict = {"players": []}
    for players in player:
        players_dict["players"].append({
            "player_id": players.player_id,
            "team_id": players.team_id,
            "first_name": players.first_name,
            "last_name": players.last_name
        })
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

# == UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==

# @app.route('/update/player/<int:id>', methods=['GET','POST'])
# def update_player(id):
#     form = PlayerForm()
#     u_player = Players.query.get(player_id)

#     if request.method == "POST":
#         u_player.team = form.team.data
#         db.session.commit()
#         return redirect(url_for('home'))

#     return render_template('update_task.html', player=u_player, form=form)

# @app.route('/update/team/<int:id>', methods=['GET','POST'])
# def update_team(id):
#     form = TeamForm()
#     u_team = Teams.query.get(team_id)

#     if request.method == "POST":
#         u_team.team = form.team.data
#         db.session.commit()
#         return redirect(url_for('home'))

#     return render_template('update_task.html', team=u_team, form=form)

# == DELETE DATA ROUTES ==== DELETE DATA ROUTES ==== DELETE DATA ROUTES ==== DELETE DATA ROUTES ==

# @app.route('/delete/task/<int:id>', methods=['DELETE'])
# def delete_player(id):
#     player = Players.query.get(id)
#     db.session.delete(task)
#     db.session.commit()
#     return Response(f"Deleted task with ID: {id}", mimetype='text/plain')