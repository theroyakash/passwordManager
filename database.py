import sqlite3
from typing import Optional
import datetime
import os
from rich.console import Console

HERE = os.getcwd()

"""
Database Schema:
CREATE TABLE "passwords" (
	"id"	INTEGER NOT NULL AUTOINCREMENT,
	"website"	TEXT NOT NULL,
	"username"	TEXT NOT NULL,
	"password"	TEXT,
	"last_updated"	TEXT,
	PRIMARY KEY("id")
);
"""


def create_database_if_not_exists():
    connection = sqlite3.connect(f"{HERE}/db/database.db")
    cursor = connection.cursor()

    with connection:
        cursor.execute(
            """
        CREATE TABLE if not exists "passwords" (
            "id"	INTEGER NOT NULL,
            "website"	TEXT NOT NULL,
            "username"	TEXT NOT NULL,
            "password"	TEXT,
            "last_updated"	TEXT,
            "userid" INTEGER,
            PRIMARY KEY("id")
        );
        """
        )


def get_all_passwords():
    connection = sqlite3.connect(f"{HERE}/db/database.db")
    cursor = connection.cursor()

    with connection:
        cursor.execute("SELECT * FROM passwords")

    fetched_data = cursor.fetchall()

    return fetched_data


def update_password(id: int, password: str):
    connection = sqlite3.connect(f"{HERE}/db/database.db")
    cursor = connection.cursor()

    today: str = datetime.datetime.now().strftime("%Y-%m-%d")

    with connection:
        cursor.execute(f'UPDATE passwords SET password = "{password}" where id = {id}')
        cursor.execute(f'UPDATE passwords SET last_updated ="{today}" where id = {id}')

    fetched_data = cursor.fetchall()

    return fetched_data


def search_password(website: Optional[str], username: Optional[str]):
    connection = sqlite3.connect(f"{HERE}/db/database.db")
    cursor = connection.cursor()

    with connection:
        if website and not username:
            cursor.execute(f"SELECT * FROM passwords WHERE website LIKE '%{website}%'")
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
    connection = sqlite3.connect(f"{HERE}/db/database.db")
    cursor = connection.cursor()

    with connection:
        cursor.execute(f"select * from passwords where id = {id}")

    fetched_data = cursor.fetchall()

    return fetched_data[0]


def delete_by_id(unique_id: int):
    connection = sqlite3.connect(f"{HERE}/db/database.db")
    cursor = connection.cursor()

    with connection:
        cursor.execute(f"delete from passwords where id={unique_id}")


def create_password(
    website: str,
    username: str,
    password: str,
    userid: int,
):
    today: str = datetime.datetime.today().strftime("%d %b, %Y")
    connection = sqlite3.connect(f"{HERE}/db/database.db")
    cursor = connection.cursor()

    with connection:        
        cursor.execute(
            f"insert into passwords (website, username, password, last_updated, userid) values ('{website}', '{username}','{password}', '{today}', {userid})"
        )


def max_id() -> int:
    connection = sqlite3.connect(f"{HERE}/db/database.db")
    cursor = connection.cursor()

    with connection:
        cursor.execute("select max(id) from passwords")

    data = cursor.fetchall()

    return data[0][0]

