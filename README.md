# ccfirstproject

This app allows the user to make bookings for an imaginary music rehearsal studio. 

controllers
|
| - booking_cont.py contains all of the routes for the app
|
|
db
|
|- rehearsal_bookings.sql contains the schema in which all bookings, users and studios are organised
|- run_sql.py allows the app to run SQL queries 
|
|
models
|
|- bookings.-, studio.-, user.py all contain the classes for Bookings, Studios and Users
|
|
repos
|
|- these files provide methods containing specific SQL queries for each class/table
|
|
static
|
|- img
    |
    |- pictures required for the app are in here. It was necessary to put them in the static folder as       they wouldn't load without it.
|
|- styles.css makes the app pretty!
|
|
templates
|
|- bookings
    |
    |- these html files provide the structure for the app's booking pages
|- studios
    |
    |- these html files provide the structure for the app's studio pages
|
|
tests
|
|- all the tests for the app. 
|
|
.flaskenv - this directs the app to port 4999
|
|
app.py - this allows the app to run with the Flask framework
|
|
console.py - this loads the SQL tables with data
|
|
run_tests.py - this runs the tests written in the tasks folder
