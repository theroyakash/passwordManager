'''
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
'''

import database
from flask import Flask, render_template, request
import vars

app = Flask(__name__)

WEBSITE_URL = 'http://127.0.0.1:6969/'

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/', methods=["GET"])
def index():
	results = database.get_all_passwords()
	total_entries = len(results)
	return render_template('index.html', 
						   user=vars.user_name, 
						   total_entries=total_entries, 
						   results=results)

@app.route('/results', methods=["GET", "POST"])
def results():
	# Search -> Redirects to results
	pass

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
	if request.method == "GET":
		selected_row = database.get_password_from_id(id)
		return render_template("update_password.html", row=selected_row)


@app.route('/delete/<id>')
def delete(id):
	pass

@app.route('/create')
def create():
	pass

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6969)