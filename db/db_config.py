from flask import g
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'produtos.db')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE_PATH)
        g.db.row_factory = sqlite3.Row 
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
