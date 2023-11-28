from spotify import Spotify


class Song:
    def __init__(self, track="", artist="", uri=""):
        self.track = track
        self.artist = artist
        self.uri = uri

    def display(self):
        print(f"Track: {self.track}\tArtist: {self.artist}\tSpotify URI: {self.uri}")


class Songs:
    def __init__(self):
        self.songs = []

    def add_songs(self, songs):
        self.songs.append(songs)

    def display(self):
        for song in self.songs:
            song.display()

    def get_uris(self):
        uris = []
        for song in self.songs:
            if song.uri is not None:
                uris.append(song.uri)
        return uris
