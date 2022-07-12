"""
System Design Doc: https://jamboard.google.com/d/1gRt_IhHOYYFlhAi8ed4FPcVobvjb8b2_7gy-kfCb4i4/edit?usp=sharing

Requirements:
0. Generate a strong password
1. Create a new password
2. Update password
3. Remove password
4. Search password by website

Database Schema:
CREATE TABLE "passwords" (
	"id"	INTEGER NOT NULL,
	"website"	TEXT NOT NULL,
	"username"	TEXT NOT NULL,
	"password"	TEXT,
	"last_updated"	TEXT,
	PRIMARY KEY("id")
);
"""

import database
from flask import Flask, render_template, request, session, redirect
import vars
from flask_session import Session
from tempfile import mkdtemp
from loginrequired import login_required

app = Flask(__name__)

WEBSITE_URL = "http://127.0.0.1:6969/"
PORT:int = 6969

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def index():
    if (session.get("username")):
        return redirect('/vault')

    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = database.get_user(username)
        
        if user == []:
            return f"<h1>User for Username: {username} Not found in the database</h1>"
        
        password_from_database = user[0][2]

        if (password_from_database != password):
            return f"<h1>Password Did not matched, please try login in <a href=\"/login\">here</a></h1>"
        
        if (password == password_from_database):
            session["username"] = username
            session["userid"] = user[0][0]
            return redirect('/vault')

    else:
        return render_template("login.html")

@app.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")

@app.route("/vault", methods=["GET"])
@login_required
def vault():
    username:str = session.get('username')
    currentlySignedUserID = session.get('userid')

    passwords = database.get_all_passwords(currentlySignedUserID)

    return render_template("vault.html", username=username, passwords=passwords)


@app.route("/results", methods=["GET", "POST"])
def results():
    # Search -> Redirects to results
    pass


@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    if request.method == "GET":
        selected_row = database.get_password_from_id(id)
        return render_template("update_password.html", row=selected_row)


@app.route("/delete/<id>")
def delete(id):
    pass


@app.route("/create", methods=["POST"])
@login_required
def create():
    if request.method == "POST":
        website = request.form.get("website")
        username = request.form.get("username")
        password = request.form.get("password")

        userid = session.get('userid')

        database.create_password(website, username, password, userid)

        return redirect('/vault')


if __name__ == "__main__":
    database.create_database_if_not_exists()
    database.create_user_table_if_not_exists()
    app.run(debug=True, host="0.0.0.0", port=PORT)
