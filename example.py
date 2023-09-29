#!/usr/bin/env python3
import shortener

result = []

result.append(shortener.shorten("domain.com", "doma.in"))

for res in result:
    print("Shortened url at: " + res)