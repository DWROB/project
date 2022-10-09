# MaDho

#### Video Demo:  url.


#### Description:

A todo list designed to help me, and others, keep an easy record of tasks, appointments and events.

The site will include a classic pomodoro timer.  User will be able to select a typical 25 minute interval for focussing.  The app includes the classical incremental pomodoro structure, with longer periods to train ability to focus for longer periods.    

Initial design is for desktop use only.

Using the Flask framework, the app will:

- create an account
- logout
- login
- view pending tasks and reminders in a table or grid layout
- create new tasks.
- set existing tasks as complete
- persist a record of all pending and completed tasks (give the user the option to delete all permanently if they want)
- work on their computer using the pomodoro technique.
- keep a record of the time they have dedicated to focussing with the timer.

## /project

### app.py

#### /login
> Get - renders the login screen.    

> Post - users login and password are checked on db.  If user exists and password matches, the users id is set as session["user_id"] for all actions.  


#### /logout

#### /  (homepage)
 > show the users tasks, reminders in an ordered fashion that allow them to see what they need to complete that day/week.

#### /createNewTask
 > form for creating a customizable task 
 > date, subject, color-flag, additional notes, category.
 > category
    *task, appointment, event, note + other customisable cats*

#### /pomodoroTimer
 > structured in the trad sense. 
 > should record the levels of focus used. 

### ado.db

1. USERS:
    ```sql
    CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL);
    REATE TABLE sqlite_sequence(name,seq);
    ```
2. TASKS: 
    ``` sql
    CREATE TABLE tasks (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, task_head TEXT, due DATETIME, created DATETIME DEFAULT (datetime('now')), completed DATETIME, notes TEXT, user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id));
    ```
3. POMO_ARCHIVE:
    ``` sql
    CREATE TABLE pomo (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, pom_type NUMERIC, user_date DATETIME, user_id INTEGER, 
    FOREIGN KEY (user_id) REFERENCES users(id));
    ```

### helpers.py
- decorated function to ensure user is logged in

## static

1. images:
   > project_logo.png

2. stylesheet:
    > styles.css 

3. JavaScript Files
    > timer.js

## templates

1. >layout.html
2. >login.html
3. >newTask.html
4. >pomodoroTimer.html
5. >register.html
6. >todo.html

## requirements.txt 
- Flask
- Flask-Session
- requests
