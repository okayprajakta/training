import sqlite3

DATABASE_FILE = 'products.db'

def dbConnection():
    connects = sqlite3.connect(DATABASE_FILE)
    connects.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    ''')
    return connects