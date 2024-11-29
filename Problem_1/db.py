import sqlite3

DB_FILE='my_products.db'

def db_connection():
    connect= sqlite3.connect(DB_FILE)
    connect.execute(
        ''' 
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL)
    '''
    )
    return connect