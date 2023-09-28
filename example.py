import shortener

result = []
result.append(shortener.shortener("youtube.com"))
result.append(shortener.shortener("google.com"))

for res in result:
    print("Shortened url at: " + res[0])