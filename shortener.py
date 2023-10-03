#!/usr/bin/env python3
import os
import uuid

def create_html(text): # creates the html
    skeleton = [
        '<!DOCTYPE html> <html> <head> <title>SEGGLY redirect</title> <meta http-equiv = "refresh" content = "0; url =  ',
        '" /> </head> <body> <p>Redirecting...</p> </body> </html>'
    ]
    return skeleton[0] + text + skeleton[1]

def create_mp4_emb(text): # creates the html for the webplayer
    skeleton = [
        '<!DOCTYPE html><html><body style="text-align: center"><h1>P(segg)layer</h1><video controls="controls"><source src="',
        '" type="video/mp4" /></video></body></html>'
    ]
    return skeleton[0] + text + skeleton[1]

def shorten(link, url_pref, path, mp4): # main

    if path == "":
        path = os.path.dirname(__file__) # Path to the redirect files, for example with Apache2: /var/www/html/

    if mp4 == False:
        
        next = str(uuid.uuid4())

        with open(path + "/" + next, 'w') as file:
            file.write(create_html(link))
            url = url_pref + "/" + next
    
    elif mp4 == True:

        next = str(uuid.uuid4())

        with open(path + "/" + next, 'w') as file:
            file.write(create_mp4_emb(link))
            url = url_pref + "/" + next

    return url
