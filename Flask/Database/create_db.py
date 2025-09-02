import sqlite3

conn = sqlite3.connect("site.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS USER (
        email TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        password TEXT UNIQUE NOT NULL
    )
''')

conn.commit()
conn.close()
