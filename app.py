import os
import sqlite3

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, loginCheck, registerNewUser

app = Flask(__name__)
conn = sqlite3.connect("ado.db", check_same_thread=False)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "\xc8\x9cCr\x951\x8f\x8f\xe7\xe8\xbc\x8b"


# homepage
@app.route("/")
@login_required
def homepage():
    """Show the users current lists and tasks"""
    return apology(message="homepage is TODO")

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
        checkedUser = loginCheck(conn, username, password)

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


        if registerNewUser(conn, username, passwordStore):
            return apology(message="success")

        return apology(message="user register failed")

    return render_template("register.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/pomodoroTimer", methods=["GET", "POST"])
@login_required
def pomodoroTimer():
    # POST, user submits to save the time


    # if GET render the timer page. 

    return render_template("pomodoroTimer.html")


@app.route("/createNewTask", methods=["GET", "POST"])
@login_required
def newTask():
    # if POST add new task to con and return to /

    # if GET render the form for creating a new task

    return render_template("newTask.html")

