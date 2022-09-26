import os
import sqlite3

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import login_required

app = Flask(__name__)
con = sqlite3.connect("ado.db")

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# homepage
@app.route("/")
@login_required
def homepage():
    """Show the users current lists and tasks"""
    return render_template("layout.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    # forget any user_id
    session.clear()

    if request.method == "POST":
        # user submitted the name and password

        # verify user and password are correct.
        return redirect("todo.html") 

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/pomodoroTimer")
def pomodoroTimer():
    # POST, timer is zero


    # if GET render the timer page. 

    return render_template("pomodoroTimer.html")


@app.route("/createNewTask", methods=["GET", "POST"])
def newTask():
    # if POST add new task to db and return to /

    # if GET render the form for creating a new task

    return render_template("newTask.html")

