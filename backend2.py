import sqlite3

def connect():
    conn = sqlite3.connect("astra.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS academia (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("astra.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO academia VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("astra.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM academia")
    row = cur.fetchall()
    conn.close()
    return row

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("astra.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM academia WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    row = cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn = sqlite3.connect("astra.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM academia WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("astra.db")
    cur = conn.cursor()
    cur.execute("UPDATE academia SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
#insert("The Star", "John Smith", 1907, 12986756)
#delete(2)
#update(3, "The Moon", "John Smooth", 1905, 98712356)
#print(view())
#print(search(author="John Smith"))