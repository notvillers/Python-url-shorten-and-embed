#!/usr/bin/env python3
import shortener

result = []

result.append(shortener.shorten("https://github.com/notvillers/Python-url-shortener", "doma.in", "", True))

for res in result:
    print("Shortened url at: " + res)