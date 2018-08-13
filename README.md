# lastFM-API
using last fm API to extract top tracks in a country or most listened songs in a country
-Please before start using the script,visit [last fm developer platforme](https://secure.last.fm/login?next=/api/account/create). and create a developer account in order to get your api_token.
-Past you token in the code :
```
    params = (
        ('method', 'artist.gettoptracks'),
        ('artist', cher),
        ('api_key', 'API_TOKEN_HERE'),
        ('format', 'json'),
    )
```
## requirements:
- python 3
- "requests" liberary 
```
pip install requests
```
## preview
[using the script to extratctop songs of phillip phillips](https://ibb.co/g10wO9)
![17 music](https://user-images.githubusercontent.com/35115877/44030641-4faa5de4-9ef9-11e8-8698-2c6e2d725d9f.PNG)

