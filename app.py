import sqlite3
from flask import Flask, render_template, request

#create the flask app
app = Flask(__name__)

#name of the SQLite DB
DATABASE = "miniforum.db"

#connect to the database
def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

#create thread table
def setup_database():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS threads(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL
        )
    """)

    conn.commit()

    #check if the tables is empty
    count = conn.execute("SELECT COUNT(*) FROM threads").fetchone()[0]

    #Add sample gaming threads if there are none
    if count == 0:
        sample_threads = [
            ("Best co-op games to play", "General"),
            ("Any good RPGs recommendations?", "RPG"),
            ("Tips for news PC gamers", "PC Gaming")
        ]
        conn.executemany("INSERT INTO threads (title, category) VALUES (?, ?)", sample_threads)

    conn.commit()
    conn.close()    

#define the homepage
@app.route('/')
def home():
    return "Welcome to MiniForum!"

if __name__ == '__main__':
    setup_database()
    app.run(debug=True)