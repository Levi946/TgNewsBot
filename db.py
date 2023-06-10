import sqlite3 as sq

async def db_start():
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()
