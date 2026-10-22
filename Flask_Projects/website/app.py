from flask import Flask, render_template, request, url_for, redirect
import sqlite3
app = Flask(__name__)
import time

DB="contact.db"

def init_db():
    conn=sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS posts (
                    post_id INTEGER PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    message TEXT NOT NULL,
                    time TEXT NOT NULL)""")

    conn.execute("""CREATE TABLE IF NOT EXISTS games (
                game_id INTEGER PRIMARY KEY,
                game_name TEXT NOT NULL,
                game_text TEXT NOT NULL,
                game_square_image
                game_image_gameplay)""")
    conn.commit()
    conn.close()
init_db()

def get_db():
    conn=sqlite3.connect(DB)
    conn.row_factory=sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/block tales")
def block_tales():
    return render_template("block_tales.html")


@app.route("/geometry dash")
def geometry_dash():
    return render_template("geometry_dash.html")


@app.route("/silksong")
def silksong():
    return render_template("silksong.html")


@app.route("/tetrio")
def tetrio():
    return render_template("tetrio.html")


@app.route("/contactus")
def contactus():
    conn=get_db()
    posts=conn.execute("SELECT * FROM posts ORDER BY post_id DESC").fetchall()
    conn.close()
    return render_template("contactus.html", posts=posts)

@app.route("/new", methods=["POST"])
def new_contact_message():
    fname=request.form["fname"].strip()
    message=request.form["message"].strip()
    lname=request.form["lname"].strip()
    email=request.form["email"].strip()
    if fname =="" or message =="" or lname=="" or email=="":
        return redirect(url_for("forum"))
    conn=get_db()
    conn.execute("INSERT INTO posts (first_name, last_name, email, message, time) VALUES (?,?,?,?,?)",
                  (fname, lname, email, message, time.strftime("%d-%m-%Y %H:%M")))
    conn.commit()
    conn.close()
    return redirect(url_for("contactus"))

if __name__ =="__main__":
    app.run(debug=True)