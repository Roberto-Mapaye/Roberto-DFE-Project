from application import app, db
from application.models import Players, Teams
from flask import render_template, request, redirect, url_for, jsonify
from os import getenv

@app.route('/read/allTeams', methods=['GET'])
def read_teams():
    all_teams = Teams.query.all()
    teams_dict = {"teams": []}
    for teams in all_teams:
        teams_dict["teams"].append(
            {
                "id": teams.id,
                "name": teams.name,
                "game": teams.game
            }
        )
    # all_players = Players.query.all()
    # player_dict = {"player": []}
    # for player in all_players:
    #     player_dict["player"].append(
    #         {
    #             "id": player.id,
    #             "first_name": player.first_name,
    #             "last_name": player.last_name
    #         }
    #     )
    return jsonify(teams_dict)

@app.route('/read/teams/<int:id>', methods=['GET'])
def read_team(id):
    team = Teams.query.get(id)
    teams_dict = {
                    "id": teams.id,
                    "name": teams.description,
                    "game": teams.completed
                }
    # player = Players.query.get(id)
    # player_dict = {
    #                 "id": player.id,
    #                 "first_name": player.first_name,
    #                 "last_name": player.last_name
    #             }
    return jsonify(teams_dict)

# == ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==

@app.route('/create/player', methods=['POST'])
def create_player():
    package = request.json
    new_player = Players(first_name=package["first_name"], last_name=package["last_name"])
    db.session.add(new_player)
    db.session.commit()
    return Response(f"Added task with description: {new_player.description}", mimetype='text/plain')

@app.route('/create/teams', methods=['POST'])
def create_teams():
    package = request.json
    new_teams = Teams(team_name=package["team_name"], game=package["game"])
    db.session.add(new_teams)
    db.session.commit()
    return Response(f"Added task with description: {new_teams.description}", mimetype='text/plain')

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