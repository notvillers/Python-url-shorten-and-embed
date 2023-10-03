import os
import uuid

def create_html(text): # creates the html for the webplayer
    skeleton = [
        '<!DOCTYPE html><html><body style="text-align: center"><h1>',
        '</h1><video controls="controls"><source src="',
        '" type="video/mp4" /></video></body></html>'
    ]
    title = 'Title'
    return skeleton[0] + title + skeleton[1] + text + skeleton[2]

def run(link, url_pref, path):
    
    if path == "":
        path = os.path.dirname(__file__) # Path to the redirect files, for example with Apache2: /var/www/html/
    
    next = str(uuid.uuid4())

    with open(path + "/" + next, 'w') as file:
        file.write(create_html(link))
        url = url_pref + "/" + next
    
    return url