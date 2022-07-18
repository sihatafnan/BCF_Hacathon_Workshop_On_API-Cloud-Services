from urllib import response
import requests
from track import Track 
from playlist import Playlist 
import json

class spotifyClient:

    def __init__(self , auth_token , user_id) -> None:
        self.auth_token = auth_token
        self.user_id = user_id 

    def _place_get_api_request(self , url):
        response = requests.get(
            url ,
            headers = {
                "Content-Type":"application/json" , 
                "Authorization":f"Bearer {self.auth_token}"
            }
        )
        return response

    def _place_post_api_request(self , url , data):
        response = requests.post(
            url ,
            data = data ,
            headers = {
                "Content-Type":"application/json" , 
                "Authorization":f"Bearer {self.auth_token}"
            }
        )
        return response

    def get_last_played_tracks(self , limit=3):
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()

        tracks = [Track(track["track"]["name"] , track["track"]["id"] , 
                    track["track"]["artists"]) for track in response_json["items"]]

        return tracks

    def create_playlist(self , name):
        data = json.dumps(
            {
                "name":name ,
                "description":"Tanema's favourite",
                "public":True 
            }
        )

        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = self._place_post_api_request(url , data)
        response_json = response.json()
        playlist_id = response_json["id"]

        playlist = Playlist(name , playlist_id)

        return playlist

    
    def populate_playlist(self , playlist , tracks):
        track_uris = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(track_uris)

        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"

        response = self._place_post_api_request(url , data)
        response_json = response.json()
        return response_json

