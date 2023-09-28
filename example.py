import shortener

result = []
result.append(shortener.shortener("youtube.com", "https://seggly.uk/short"))
result.append(shortener.shortener("google.com", "https://seggly.uk/short"))

for res in result:
    print("Shortened url at: " + res)

result = []

result.append(shortener.shortener("domain.com", "doma.in"))

for res in result:
    print("Shortened url at: " + res)