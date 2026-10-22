from flask import Flask, render_template, request, url_for, redirect
import sqlite3
import time
print(time.strftime("%Y-%m-%d %H:%M"))

app = Flask(__name__)
DB="forum.db"

def init_db():
    conn=sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS posts (
                    post_id INTEGER PRIMARY KEY,
                    author TEXT NOT NULL,
                    message TEXT NOT NULL)""")
    conn.commit()
    conn.close()
init_db()

def get_db():
    conn=sqlite3.connect(DB)
    conn.row_factory=sqlite3.Row
    return conn




@app.route("/")
def home():
    return render_template("base.html")


@app.route("/forum")
def forum():
    conn=get_db()
    posts=conn.execute("SELECT * FROM posts ORDER BY post_id DESC").fetchall()
    conn.close()
    return render_template("forum.html", posts=posts)

@app.route("/new", methods=["POST"])
def new_post():
    author=request.form["author"].strip()
    message=request.form["message"].strip()
    if author =="" or message =="":
        return redirect(url_for("forum"))
    conn=get_db()
    conn.execute("INSERT INTO posts (author, message) VALUES (?,?)",
                  (author, message))
    conn.commit()
    conn.close()
    return redirect(url_for("forum"))

if __name__ == "__main__":
    app.run(debug=True)