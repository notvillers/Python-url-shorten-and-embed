#!/usr/bin/env python3
import os
import sqlite3
import create_db

db_file = create_db.db_name() # creates .db if not found
if not os.path.exists(db_file):
    create_db.create()
connection = sqlite3.connect(db_file)
cursor = connection.cursor()

path = os.path.dirname(__file__) # Path to the redirect files, for example with Apache2: /var/www/html/

def select(text): # selects from the .db
    cursor.execute(text)
    return cursor.fetchall()

def insert(text): # inserts into the .db
    cursor.execute(text)
    connection.commit()

def create_html(text): # creates the html
    skeleton = [
        '<!DOCTYPE html> <html> <head> <title>SEGGLY redirect</title> <meta http-equiv = "refresh" content = "0; url = ',
        '" /> </head> <body> <p>Redirecting...</p> </body> </html>'
    ]
    return skeleton[0] + text + skeleton[1]

def shorten(link, url_pref): # main

    shorts = []

    for row in select("select * from direction"):
        shorts.append(row)

    max = 0
    for short in shorts:
        if int(short[1]) > int(max):
            max = int(short[1])

    next = max + 1
    shorts.append([link, str(next)])
    insert("INSERT INTO direction (src, dest) values ('" + link + "', " + str(next) + ")")

    short_nums = []

    for file in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]:
        if file.endswith('.html'):
            short_nums.append(file.replace('.html',''))

    url = ""

    for short in shorts:
        if short[1] not in short_nums:
            with open(path + "/" + short[1], 'w') as file:
                file.write(create_html(short[0]))
                url = url_pref + "/" + short[1]
    
    return url
