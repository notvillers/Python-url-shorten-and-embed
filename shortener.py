#!/usr/bin/env python3
import os
import random_id

def create_html(text): # creates the html
    skeleton = [
        '<!DOCTYPE html> <html> <head> <title>',
        '</title> <meta http-equiv = "refresh" content = "0; url =  ',
        '" /> </head> <body> <p>Redirecting...</p> </body> </html>'
    ]
    title = 'Title'
    return skeleton[0] + title + skeleton[1] + text + skeleton[2]

def run(link, url_pref, path): # main

    if path == "":
        path = os.path.dirname(__file__) # Path to the redirect files, for example with Apache2: /var/www/html/
        
    next = str(random_id.generate())

    with open(path + "/" + next, 'w') as file:
        file.write(create_html(link))
        url = url_pref + "/" + next

    return url
