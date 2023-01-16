# ADO

#### Video Demo:  url.


#### Description:

A todo list designed to help me, and others, keep an easy record of tasks, appointments and events.

The site will include a classic pomodoro timer.  User will be able to select a typical 25 minute interval for focusing.  The app includes the classical incremental pomodoro structure, with longer periods to train ability to focus for longer periods.

The design will be responsive to all screen sizes. A max of 5 cards in a row on the biggest screens and 1 card per row for the smallest.

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
clears session.

#### /newTask
* form for creating a customizable task
* date, subject, color-flag, additional notes, category.
* category
  * task, appointment, event, note + other customisable cats*

#### /task_handler
Methods DELETE || PUT only.
AJAX method called by Js.
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

#### apology
* standard error function with dynamic string parameter to provide detailed feedback on nature of errors.

#### usernameTaken
Accepts one parameter, a username provided by user when creating an accounts.
Returns False is the username already exists in the database.

#### registerNewUser
Accepts two parameters - username and passwordStore (a password already hashed by calling function).
calls userNameTaken() and if False - username available - creates new user in db.

#### loginCheck
Accepts two parameter, username and password (entered by user on login form) verifies the user name and the user's password via hash.

#### validate_task
accepts one parameter a task dict.  Verifies that task has required data and not null.

#### save_new_task
accepts one parameter a task dict.  Inserts all data - alrerady validated - into db with user_id as its FK.

#### get_user_tasks
index function.  With parameter user_id fetch all tasks in db that belong to the user_id.

Normally a user has more than one task.  Therefore looping through the fetch response and creating a dict object of each task.

#### update_task_status
accepts one parameter, task_id.  Fetches the task pertaining to this task_id.  Will toggle value between 0 and 1.

#### delete_task
Same process as update but simpler as it simply deletes the record; therefore no need to fetch the record with SELECT query.

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
* homepageTaskHandler
  * handle changes to card when task completed or deleted by removing or altering the class within the DOM
  * In addition triggering a AJAX function to make relevant changes in the db without refreshing the page.  

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
