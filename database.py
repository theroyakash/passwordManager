import sqlite3
from typing import Optional
import datetime

"""
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

def get_all_passwords():
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	with connection:
		cursor.execute(
                "SELECT * FROM passwords"
        )

	fetched_data = cursor.fetchall()

	return fetched_data

def update_password(id: int, password: str):
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	with connection:
		cursor.execute(
			f"UPDATE passwords SET password = '{password}' where id = {id}"
		)
	
	fetched_data = cursor.fetchall()

	return fetched_data

def search_password(website: Optional[str], username: Optional[str]):
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	with connection:
		if website and not username:
			cursor.execute(
				f"SELECT * FROM passwords WHERE website LIKE '%{website}%'"
			)
		if not website and username:
			cursor.execute(
				f"SELECT * FROM passwords WHERE username LIKE '%{username}%'"
			)
		if website and username:
			cursor.execute(
				f"SELECT * FROM passwords WHERE username LIKE '%{username}%' OR '%{website}%'"
			)

	fetched_data = cursor.fetchall()

	return fetched_data

def get_password_from_id(id: int):
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	with connection:
		cursor.execute(
			f"select * from passwords where id = {id}"
		)
	
	fetched_data = cursor.fetchall()

	return fetched_data[0]

def delete_by_id(id: int):
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	with connection:
		cursor.execute(
			f"delete from passwords where id := id", {"id": id}
		)

def create_password(
	website: str,
	username: str,
	password: str,
):
	today:str = datetime.datetime.today().strftime("%d %b, %Y")
	max_id_so_far: int = max_id()

	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	with connection:
		newid = max_id_so_far + 1
		cursor.execute(
			f"insert into passwords (id, website, username, password, last_updated) values ({newid}, '{website}', '{username}','{password}', '{today}')"	
		)

def max_id() -> int:
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()

	with connection:
		cursor.execute("select max(id) from passwords")

	data = cursor.fetchall()

	return data[0][0]
	

if __name__ == "__main__":
	# result = get_all_passwords()
	# print(result)

	# update_password(1, "hola mami, wanna fuck?")

	# result = get_all_passwords()
	# print(result)

	create_password("pornhub.com", "massiveBigDickWithSmallTits", "guywith 10 inch long dick")