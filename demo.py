from spotifyClient import spotifyClient

user_id = "YOUR USER ID"
auth_tok = "YOUR AUTH TOKEN"

sc = spotifyClient(auth_tok , user_id)

last_played_tracks = sc.get_last_played_tracks(3)

playlist = sc.create_playlist("new playlist")

sc.populate_playlist(playlist , last_played_tracks)
