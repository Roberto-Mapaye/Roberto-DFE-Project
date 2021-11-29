from application import app
from application.forms import PlayerForm, TeamForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

@app.route('/')
@app.route('/home')
def home():
    all_task = requests.get("http://todo-app-backend:5000/read/allTasks").json()
    app.logger.info(f"Tasks: {all_task}")
    return render_template('index.html', title="Home", all_tasks=all_task["tasks"])

# == ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==== ADD DATA ROUTES ==

@app.route('/create/task', methods=['GET','POST'])
def create_task():
    form = TaskForm()

    if request.method == "POST":
        response = requests.post("http://todo-app-backend:5000/create/task", json={"description": form.description.data})
        return redirect(url_for('home'))

    return render_template("create_task.html", title="Add a new Task", form=form)

@app.route('/create/task', methods=['GET','POST'])
def create_task():
    form = TaskForm()

    if request.method == "POST":
        response = requests.post("http://todo-app-backend:5000/create/task", json={"description": form.description.data})
        return redirect(url_for('home'))

    return render_template("create_task.html", title="Add a new Task", form=form)

# == UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==== UPDATE DATA ROUTES ==

@app.route('/update/task/<int:id>', methods=['GET','POST'])
def update_task(id):
    form = TaskForm()
    task = requests.get(f"http://todo-app-backend:5000/read/task/{id}").json()

    if request.method == "POST":
        response = requests.put(f"http://todo-app-backend:5000/update/task/{id}", json={"description": form.description.data})
        return redirect(url_for('home'))
    return render_template('update_task.html', task=task, form=form)

# == DELETE DATA ROUTES ==== DELETE DATA ROUTES ==== DELETE DATA ROUTES ==== DELETE DATA ROUTES ==

@app.route('/delete/task/<int:id>')
def delete_task(id):
    response = requests.delete(f"http://todo-app-backend:5000/update/task/{id}")
    return redirect(url_for('home'))