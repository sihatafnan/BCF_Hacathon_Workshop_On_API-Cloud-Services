class Track:

    def __init__(self , name , id , artist) -> None:
        self.name = name
        self.id = id 
        self.artist = artist 

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"