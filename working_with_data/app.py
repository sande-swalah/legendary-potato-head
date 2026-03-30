import sqlite3
import json
import random

from flask import Flask, request, jsonify, g

# start the flask app
wakadinali = Flask(__name__)

# DATABASE SETUP
DATABASE_NAME = "victim_of_madness"

def get_database():
    """
    Get the connection to a database
    """
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE_NAME)
        # helps in making the tuple more readable
        g.db.row_factory = sqlite3.Row 
    return g.db

@wakadinali.teardown_appcontext
def close_database(e):
    """
    Terminate the connection once the request is done
    """
    db = g.pop("db", None)
    if db is not None:
        db.close()

def start_db():
    """
    Create the tables (DDL)
    Seed the table with initial data(DML)
    commit the execution (TCL)
    """
    db = get_database()

    # DDL
    db.execute("""
    CREATE TABLE IF NOT EXISTS books (
               id        INTEGER PRIMARY KEY AUTOINCREMENT,
               title     TEXT    NOT NULL,
               author    TEXT    NOT NULL,
               genre     TEXT    NOT NULL,
               year_pub  INTEGER NOT NULL,
               available INTEGER NOT NULL DEFAULT 1
               )
    """)
    # DQL
    if db.execute("SELECT COUNT(*) FROM books").fetchone()[0] == 0:
        reading_material = [
            ("The alchemist", "paulo coehlo", "fictional", 1991, 1), 
            ("thinking, fast and slow", "Daniel Kahneman", "Non-fiction", 2011, 1)
        ]

        # Generate a random collection of 100 books
        genres = ["fictional", "Non-fiction", "History", "self help", "academia", "academia", "philopsophy"]
        for item in range(1, 101):
            title = f"Book, {item}"
            author = f"Author {item}"
            genre = random.choice(genres)
            year_pub = random.randint(1980, 2025)
            available = random.choice([0,1])

            reading_material.append((title, author, genre, year_pub, available))


        # DML
        db.executemany("""
                       INSERT INTO books 
                            (title, author, genre, year_pub, available) 
                       VALUES 
                            (?,?,?,?,?)
            """, reading_material
            )

    # TCL
    db.commit()

def row_to_dict(row):
    """
    Convertion of row to dictionary so that we can jsonify
    """
    return dict(row)

# HELPER FUNCTION(utility)
def api_response(data=None, message="", status_code=200):
    """
    return consistent response to the api
    """
    payload = {
        "ok": status_code < 400,
        "status": status_code,
        "message": message
    }

    if data is not None:
        payload["data"] = data
    return jsonify(payload), status_code

def error_response(message, status_code=400):
    """Shortcut for error messages"""
    return api_response(message=message, status_code=status_code)


# ENDPOINTS
# we do a fetch(GET Request) form the books Resource
@wakadinali.route("/api/books", methods=["GET"])
def fetch_books():
    # We make a connection to the database
    db = get_database()

    # we structure out a basic query
    query = "SELECT * FROM books"

    # you execute the query and get the data or none
    row_from_db = db.execute(query).fetchmany()

    # parse the data to a python object
    obj = [dict(item) for item in row_from_db]

    # return the api_response
    return api_response(data=obj, message="Fetch was successful", status_code=200)



# run the app and start the db process
if __name__ == "__main__":
    with wakadinali.app_context():
        start_db()
    wakadinali.run()
