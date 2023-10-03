# Python URL shortener and video embedder

## Calling the scripts

### shortener.py
Syntax:
```
shortener.run(link, url_pref, path_to_directory)
```
For example:
```
import shortener

shortened = []
shortened.append(shortener.run("https://github.com/notvillers/Python-url-shortener", "doma.in", ""))

for result in shortened:
    print("Shortened url at: " + result)
```
```
% Shortened url at: doma.in/c99397ce-1715-4885-aaa4-973677c141f8
```

### videoembed.py
Syntax:
```
videoembed.run(link.mp4, url_pred, path_to_directory)
```
For example:
```
import videoembed

embed = []
embed.append(videoembed.run("https://cdn.discordapp.com/attachments/1136960219142946867/1158846141467742259/Joren_Falls_Izu_Jap.mp4", "doma.in", ""))

for result in embed:
    print("Embed video at: " + result)
```
```
% Embed video at: doma.in/fa5b8e62-f5ab-45ee-8067-91f6bfd1e4c9
```

> [!NOTE]
> If you plan to integrate it, then be aware of the premissions, because the default Apache2 configuration is not allowing you to paste to the /var/www/html without root premission.
