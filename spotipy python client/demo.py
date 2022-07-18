from textwrap import indent
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json 

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_APP_CLIENT_ID",
                                               client_secret="YOUR_APP_CLIENT_SECRET",
                                               redirect_uri="YOUR_APP_REDIRECT_URI",
                                               scope="user-library-read"))

#search
results = sp.search("radiohead")
#print(json.dumps(results , indent=4))

#create playlist
user_id = sp.me()["id"]
playlist_name = "my_fav"
sp.user_playlist_create(user_id , playlist_name)

#find playlist_id
playlist_id = ""
playlists = sp.user_playlists(user_id)
for playlist in playlists['items']:
    if (playlist['name'] == playlist_name):
        playlist_id = playlist['id']
        break

#append search results to that playlist
track_ids = [el['id'] for el in results["tracks"]["items"]]
#print(track_ids)
sp.playlist_add_items(playlist_id , track_ids)




