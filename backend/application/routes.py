from application import app, db
from application.models import Organisation, Players, Teams
from application.forms import PlayerForm, TeamForm
from flask import render_template, request, redirect, url_for, jsonify
from os import getenv

@app.route('/')
@app.route('/home')
def home():
    all_teams = Tasks.query.all()
    return render_template('index.html', title="Home", all_tasks=all_tasks)


# == ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==

@app.route('/add/player', methods=['GET','POST'])
def create_task():
    form = PlayerForm()

    if request.method == "POST":
        new_player = Players(first_name=form.first_name.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("create_task.html", title="Add a new Task", form=form)

@app.route('/add/team', methods=['GET','POST'])
def create_task():
    form = TeamForm()

    if request.method == "POST":
        new_task = Tasks(description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("create_task.html", title="Add a new Task", form=form)

# == UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==

@app.route('/update/task/<int:id>', methods=['GET','POST'])
def update_task(id):
    form = TaskForm()
    task = Tasks.query.get(id)

    if request.method == "POST":
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update_task.html', task=task, form=form)

# == DELETE DATA ROUTES ==== DELETE DATA ROUTES ==== DELETE DATA ROUTES ==== DELETE DATA ROUTES ==

@app.route('/delete/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return Response(f"Deleted task with ID: {id}", mimetype='text/plain')