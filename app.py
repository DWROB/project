import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, loginCheck, registerNewUser, save_new_task, validate_task, get_user_tasks

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "\xc8\x9cCr\x951\x8f\x8f\xe7\xe8\xbc\x8b"

# flask-session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

TASK_CATEGORIES = [
    "Task",
    "Appointment",
    "Event",
    "Note"
]

# homepage
@app.route("/")
@login_required
def homepage():
    """Show the users current lists and tasks"""
    tasks = get_user_tasks(session["user_id"][0])

    return render_template("homepage.html", tasks=tasks)

@app.route("/login", methods=["GET", "POST"])
def login():

    # forget any user_id
    session.clear()

    if request.method == "POST":
        # user submitted the name and password
        username = request.form.get("username").lower()
        password = request.form.get("password")

        # ensure the form inputs are not blank
        if not username:
            return apology(message="username entry is blank")
        elif not password:
            return apology(message="password entry is blank")


        # ensure password and user are correct
        checkedUser = loginCheck(username, password)

        # if ok, log the session
        if checkedUser != None:
            # log the session
            session["user_id"] = checkedUser
            return redirect("/")
        else:
            return apology(message="username or password is incorrect")

    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        # validate input name not empty
        username = request.form.get("username").lower()
        if not username:
            return apology(message="user name is blank")

        # validate password and confirmation are the same or not blank
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not password or not confirmation:
            return apology(message="password fields are blank")

        if password != confirmation:
            return apology(message="passwords don't match")

        # encrypt user password
        passwordStore = generate_password_hash(password)


        if registerNewUser(username, passwordStore):
            return redirect("/")

        return apology(message="user register failed")

    return render_template("register.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/newTask", methods=["GET", "POST"])
@login_required
def newTask():
    # if POST add new task to db and return to /
    if request.method == "POST":
        task = {}
        task['name'] = request.form.get("taskSubject")
        task['date'] = request.form.get("taskDate")
        task['time'] = request.form.get("taskTime")
        task['location'] = request.form.get("taskLocation")
        task['notes'] = request.form.get("taskNotes")
        task['category'] = request.form.get("taskCategory")

        if validate_task(task):
            if save_new_task(task):
                return redirect("/")
            # return to home
            return apology("Failed to save")

        return apology(message="task not valid, try again")
    # if GET render the form for creating a new task
    return render_template("newTask.html", task_categories=TASK_CATEGORIES)

@app.route("/taskHandler", "POST")
@login_required
def taskHandler():
    return True
