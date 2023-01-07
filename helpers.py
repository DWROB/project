import os
import requests
import urllib.parse
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

from flask import redirect, render_template, request, session
from functools import wraps

conn = sqlite3.connect("ado.db", check_same_thread=False)


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("todo.html", top=code, bottom=escape(message)), code


def usernameTaken(username):

    # SQL query - username taken?
    userQuery = "SELECT * FROM users WHERE username = ?"
    cur = conn.cursor()
    cur.execute(userQuery, (username,))

    query = cur.fetchall()

    if query:
        return True
    return False

def registerNewUser(username, passwordStore):
    # is username available
    if not usernameTaken(conn, username):
        insertQuery = "INSERT INTO users (username, hash) VALUES (?, ?)"

        userInput = [(username, passwordStore)]

        cur = conn.cursor()
        cur.execute(insertQuery, userInput[0])
        conn.commit()
        return True

    return False

def loginCheck(username, password):
    cur = conn.cursor()

    cur.execute("SELECT username FROM users WHERE username = ?", (username,))
    usernameFound = cur.fetchall()

    cur.execute("SELECT hash FROM users WHERE username = ?", (username,))
    passwordCheck = cur.fetchone()


    if len(usernameFound) != 1 or not check_password_hash(passwordCheck[0], password):
        cur.close()
        return None
    else:
        cur.execute("SELECT id FROM users WHERE username = ?", (username,))
        user_id = cur.fetchone()
        cur.close()
        return user_id

def validate_task(task):
    # nothing empty, except notes.
    if not task['name']:
        return False
    if not task['date']:
        return False
    if not task['category']:
        return False
    else:
        return True


def save_new_task(task_new):
    # array of 6. 0name, 1date, 2time, 3location, 4notes, 5category
    insert_query = "INSERT INTO tasks (task_head, due, time, location, notes, category, user_id, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))"
    insert_values = [(task_new['name'], task_new['date'], task_new['time'], task_new['location'],
                     task_new['notes'], task_new['category'], session['user_id'][0])]
    cur = conn.cursor()

    cur.execute(insert_query, insert_values[0])
    conn.commit()
    return True

def get_user_tasks(user_id):
    user_task_query = "SELECT * FROM tasks WHERE user_id = ?"

    cur = conn.cursor()

    cur.execute(user_task_query, (user_id,))

    task_response = cur.fetchall()

    # loop through response and put each task as a dict object
    # 1 - task_name, 2 due, 3 created, 4 notes, 5 location, 6 category
    # 7 time, 8 completed, 9 updated_at
    tasks = []
    for task_entry in task_response:
        task = {}
        task["task_name"] = task_entry[1]
        task["task_due"] = task_entry[2]
        task["task_time"] = task_entry[7]
        task["task_location"] = task_entry[5]
        task["task_category"] = task_entry[6]
        task["task_notes"] = task_entry[4]
        task["task_created"] = task_entry[3]
        task["task_updated_at"] = task_entry[9]

        if task_entry[8] == "0":
            task["task_completed"] = False
        else:
            task["task_completed"] = True
        tasks.append(task)

    return tasks

