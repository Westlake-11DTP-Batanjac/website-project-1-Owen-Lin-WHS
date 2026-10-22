import sqlite3
conn=sqlite3.connect("sports.db")
print("Done")
cursor= conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS teams(
                    team_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    sport TEXT,
                    players INTEGER)""")
conn.commit()

cursor.execute("""INSERT INTO teams 
            (name, sport, players) 
            VALUES (?, ?, ?)""", 
            (1, 'a', 3))
conn.commit()

cursor.execute("""INSERT INTO teams 
            (name, sport, players) 
            VALUES (?, ?, ?)""", 
            (2, 'a', 4))
conn.commit()


cursor.execute("SELECT * FROM teams")
conn.close()