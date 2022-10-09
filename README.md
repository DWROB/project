# MaDho

#### Video Demo:  url.


#### Description:

A todo list designed to help me, and others, keep an easy record of tasks, appointments and events.

The site will include a classic pomodoro timer.  User will be able to select a typical 25 minute interval for focussing.  The app includes the classical incremental pomodoro structure, with longer periods to train ability to focus for longer periods.    

Initial design is for desktop use only.

## /project

1. **app.py**
- /login

- /logout

 - homepage
 > show the users tasks, reminders in an ordered fashion that allow them to see what they need to complete that day/week.

 - /createNewTask
 > form for creating a customizable task 
 > date, subject, color-flag, additional notes, category.
 > **category**
*task, appointment, event, note + other customisable cats*

 - /pomodoroTimer
 > structured in the trad sense. 
 > should record the levels of focus used. 

2. **ado.db**

3. **helpers.py**
- decorated function to ensure user is logged in

## /static

1. **images:**
   > project_logo.png

2. **stylesheet:**
    > styles.css 

## /templates

1. >layout.html
2. >login.html
3. >newTask.html
4. >pomodoroTimer.html
5. >todo.html [default under-construction page only]

**requirements**
- Flask
- Flask-Session
- requests
