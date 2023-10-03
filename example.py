#!/usr/bin/env python3
import shortener
import videoembed

shortened = []
shortened.append(shortener.run("https://github.com/notvillers/Python-url-shortener", "doma.in", ""))

embed = []
embed.append(videoembed.run("https://cdn.discordapp.com/attachments/1136960219142946867/1158846141467742259/Joren_Falls_Izu_Jap.mp4", "doma.in", ""))

for result in shortened:
    print("Shortened url at: " + result)
    
for result in embed:
    print("Embed video at: " + result)