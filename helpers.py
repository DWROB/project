import os
import requests
import urllib.parse
from werkzeug.security import check_password_hash, generate_password_hash

from flask import redirect, render_template, request, session
from functools import wraps



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


def usernameTaken(conn, username):
    
    # SQL query - username taken?
    userQuery = "SELECT * FROM users WHERE username = ?"
    cur = conn.cursor()
    cur.execute(userQuery, (username,))

    query = cur.fetchall()

    if query:
        return True
    return False

def registerNewUser(conn, username, passwordStore):
    # is username available
    if not usernameTaken(conn, username):
        insertQuery = "INSERT INTO users (username, hash) VALUES (?, ?)"

        userInput = [(username, passwordStore)]

        cur = conn.cursor()
        cur.execute(insertQuery, userInput[0])
        conn.commit()
        return True

    return False
    
def loginCheck(conn, username, password):
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