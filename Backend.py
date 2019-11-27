import sqlite3

class Back(object):
    def __init__(self):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS movie(id INTEGER PRIMARY KEY, title TEXT, year INTEGER, director TEXT, lead TEXT)")
        db.commit()
        db.close()

    def view_all(self):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("SELECT * FROM movie")
        data = cur.fetchall()
        db.close()
        return data

    def add_element(self, title="", year=2019, director="Johny Derp", lead="Brad Pitt"):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("INSERT INTO movie VALUES(NULL, ?, ?, ?, ?)", (title, year, director, lead))
        db.commit()
        db.close()

    def del_element(self, id):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("DELETE FROM movie WHERE id=?", (title, year, director, lead))
        db.commit()
        db.close()

    def update_element(self, id, title="", year=2019, director="Johny Derp", lead="Brad Pitt"):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("UPDATE movie SET title=?, year=?, director=?, lead=? WHERE id=?)", (title, year, director, lead, id))
        db.commit()
        db.close()


# debug database
if __name__=="__main__":
    bk = Back()
    db = sqlite3.connect("movies.db")
    cur = db.cursor()
    cur.execute("INSERT INTO movie VALUES (NULL, ?, ?, ?, ?)", ("Finding Neverland", 2007, "Andrew Stanton", "Johny Derp"))
    db.commit()
    cur.execute("SELECT * FROM movie")
    data = cur.fetchall()
    for line in data:
        print(line)
    db.close()



