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
