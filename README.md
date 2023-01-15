# ADO

#### Video Demo:  url.


#### Description:

A todo list designed to help me, and others, keep an easy record of tasks, appointments and events.

The site will include a classic pomodoro timer.  User will be able to select a typical 25 minute interval for focussing.  The app includes the classical incremental pomodoro structure, with longer periods to train ability to focus for longer periods.

Initial design is for desktop use only.  The main consideration being that my use of modals, coupled with my inexperience, means that it would take longer to create.

Using the Flask framework, the app will:

- create an account
- logout
- login
- view pending tasks and reminders in a table or grid layout
- create new tasks.
- set existing tasks as complete
- persist a record of all pending and completed tasks (give the user the option to delete all permanently if they want)
- work on their computer using the pomodoro technique.

## /project

### app.py

#### /(root)
* if logged in: show the users tasks, reminders in an ordered fashion that allow them to see what they need to complete that day/week.
* else: show the login screen with option to register.

#### /login
* Get - renders the login screen.

* Post - users login and password are checked on db.  If user exists and password matches, the users id is set as session["user_id"] for all actions.

#### /register
* Get - renders a form to create an account.

* Post - account created.  Werkzeug handling hashing of the password in db.

#### /logout

#### /newTask
* form for creating a customizable task
* date, subject, color-flag, additional notes, category.
* category
  * task, appointment, event, note + other customisable cats*

#### /taskHandler
* updates db from user actions on task-cards.
  * Either change 'complete' to True/False.
  * or Delete the task from the db.

### ado.db

1. USERS:
    ```sql
    CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL);

    ```
2. TASKS:
    ``` sql
        CREATE TABLE tasks (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,task_head TEXT, due DATETIME, created_at DATETIME DEFAULT (datetime('now')), notes TEXT, user_id INTEGER, location TEXT, category TEXT,time TIME, complete BOOLEAN NOT NULL DEFAULT false, updated_at DATETIME, FOREIGN KEY (user_id) REFERENCES users(id));
    ```

### helpers.py
* decorated function to ensure user is logged in
* all db interactions managed in helpers.

## static

1. stylesheet:
* styles.css
  * /components:
  * cards.css
  * forms.css
  * navbar.css
  * pomo-container.css

2. JavaScript Files
* timer.js - manipulates DOM to show countdown for focus time.
* homepageCards.js - to handle drag and drop functions for the users cards
* homepageTaskHandler - to handle changes to card when task completed or deleted.  In addition to updating the db

## templates

1. layout.html
2. login.html
3. newTask.html
4. pomodoroTimer.html
5. register.html
6. todo.html - error page
7. homepage.html - index of all tasks belonging to user

## requirements.txt
* Flask
* Flask-Session
* requests
