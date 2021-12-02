from application import app
from application.forms import PlayerForm, TeamForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

@app.route('/')
@app.route('/home')
def home():
    all_teams = requests.get("http://backend:5000/read/allTeams").json()
    # app.logger.info(f"Teams: {all_teams}")
    return render_template('index.html', all_teams=all_teams["teams"])

# == ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==

@app.route('/create/player', methods=['GET','POST'])
def create_player():
    form = PlayerForm()
    teams = requests.get("http://backend:5000/read/allTeams").json()

    for team in teams["teams"]:
        form.teams.choices.append((team["team_id"], team["team_name"]))

    if request.method == "POST":
        response = requests.post(
            f"http://backend:5000/create/player/{form.teams.data}",
            json={
                "first_name": form.first_name.data,
                "last_name": form.last_name.data,
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_player.html", title="Add a new Player", form=form)

@app.route('/create/teams', methods=['GET','POST'])
def create_teams():
    form = TeamForm()
    

    if request.method == "POST":
        response = requests.post(
            "http://backend:5000/create/teams",
            json={"team_name": form.team_name.data, "game": form.game.data}
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_team.html", title="Add a new Task", form=form)

# == DELETE DATA ROUTES ==== DELETE DATA ROUTES ==== DELETE DATA ROUTES ==== DELETE DATA ROUTES ==

@app.route('/delete/player/<int:id>')
def delete_players(id):
    response = requests.delete(f"http://backend:5000/delete/player/{id}")
    return redirect(url_for('home'))

@app.route('/delete/team/<int:id>')
def delete_teams(id):
    response = requests.delete(f"http://backend:5000/delete/team/{id}")
    return redirect(url_for('home'))

# == UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==

@app.route('/update/player/<int:id>', methods=['GET','POST'])
def update_player(id):
    form = PlayerForm()
    player = requests.get(f"http://backend:5000/read/player/{id}").json()
    # teams = requests.get("http://backend:5000/read/allTeams").json()

    # for team in teams["teams"]:
    #     form.teams.choices.append((team["team_id"], team["team_name"]))

    if request.method == "POST":
        response = requests.put(f"http://backend:5000/update/player/{id}", json={
            "first_name": form.first_name.data,
            "last_name": form.last_name.data
            })
        return redirect(url_for('home'))
    return render_template('update_player.html', player=player, form=form)

@app.route('/update/team/<int:id>', methods=['GET','POST'])
def update_team(id):
    form = TeamForm()
    team = requests.get(f"http://backend:5000/read/team/{id}").json()

    if request.method == "POST":
        response = requests.put(f"http://backend:5000/update/team/{id}",
            json={"team_name": form.team_name.data, "game": form.game.data}
        )
        return redirect(url_for('home'))

    return render_template('update_teams.html', team=team, form=form)