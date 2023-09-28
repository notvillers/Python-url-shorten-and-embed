#!/usr/bin/env python3
import sqlite3

def db_name():
    return 'url_short.db'

def create():
    connection = sqlite3.connect(db_name())
    cursor = connection.cursor()

    create_tables = []
    create_tables.append("""
    CREATE TABLE IF NOT EXISTS direction (
        src TEXT,
        dest TEXT
    );
    """)

    for tables in create_tables:
        cursor.execute(tables)
        connection.commit()
    connection.close()