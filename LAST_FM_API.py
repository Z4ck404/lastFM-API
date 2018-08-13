import requests
def contry_music(text):
    params = (
        ('method', 'geo.gettoptracks'),
        ('country', text),
        ('api_key', 'API_TOKEN_HERE'),#your last fm api goes here 
        ('format', 'json'),
    )
    response = requests.get('http://ws.audioscrobbler.com/2.0/', params=params)
    for i in response.json().get("tracks").get("track"):
        print (i["name"],'\t by:',i["artist"]["name"])
def top_singer_songs(cher):
    params = (
        ('method', 'artist.gettoptracks'),
        ('artist', cher),
        ('api_key', 'API_TOKEN_HERE'),
        ('format', 'json'),
    )
    response = requests.get('http://ws.audioscrobbler.com/2.0/', params=params).json().get("toptracks").get("track")
    for i in response:
        print("[+] SONG:",i["name"])
print(""" 
  __ ______ __  __ _    _ _____ __  _____ 
 /_ |____  |  \/  | |  | | ____/_ |/ ____|
  | |   / /| \  / | |  | | |__  | | |     
  | |  / / | |\/| | |  | |___ \ | | |     
  | | / /  | |  | | |__| |___) || | |____ 
  |_|/_/   |_|  |_|\____/|____/ |_|\_____|
                                          
""")
print(" a tool to stream the latest music updates for you")
print("[*] INFO: tell us what you need :")
print("[1]get the most listened music in you country ,[2]get  you favorite artist top tracks")
print("[1 or 2] :")
choice = input()
print("[*] INFO: loading your choice ",choice,":")
if (choice =="1"):
    print("[*] INFO: please print the country :")
    text = input()
    print("[*] INFO:loading the most listened songs in",text ,":")
    contry_music(text)
if (choice =="2"):
    print("[*] INFO: please print your singer :")
    singer = input()
    print("[*] INFO:loading top tracks of",singer,":")
    top_singer_songs(singer)
