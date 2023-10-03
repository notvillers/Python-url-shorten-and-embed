# Python URL shortener

## Calling the shortener.py
The bot can be called with the following syntax (if imported):
```
shortener.shorten(link, url_pref, path_to_directory, IsItMP4)
```
For example:
```
import shortener

result = []

result.append(shortener.shorten("domain.com", "doma.in", "path", False))

for res in result:
    print("Shortened url at: " + res)
```
```
% Shortened url at: doma.in/1
```
> [!WARNING]
> Placing files manually in the shortener's destination folder can cause problems.

> [!NOTE]
> If you plan to integrate it, then be aware of the premissions, because the default Apache2 configuration is not allowing you to paste to the /var/www/html without root premission.
