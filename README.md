# Python URL shortener

## Calling the shortener
The bot can be called with the following syntax (if imported):
```
shortener.shortener(link, url_pref)
```
For example:
```
import shortener

result = []

result.append(shortener.shortener("domain.com", "doma.in"))

for res in result:
    print("Shortened url at: " + res)
```
```
Shortened url at: doma.in/1
```
> [!WARNING]
> Placing files manually in the shortener url can cause problems.
> [!NOTE]
> If you plan to integrate it, then be aware of the premissions, because the default Apache2 configuration is not allowing you to paste to the /var/www/html without root premission.