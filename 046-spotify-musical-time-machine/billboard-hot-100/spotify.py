# import song classes
from song import Song, Songs

# others imports
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from os import environ
import base64

# constants
SPOTIFY_USER_ID = "31l7m423o7rhfodl5x2oex53nqoy"
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_BASE_URL = 'https://api.spotify.com/v1/'
SPOTIFY_CACHE_PATH = ".spotify"
SPOTIFY_REDIRECT_URI = "http://example.com",


class Spotify:
    def __init__(self):
        self.client_id =  environ.get("SPOTIFY_CLIENT_ID")
        self.client_secret = environ.get("SPOTIFY_CLIENT_SECRET")
        self.user_id = ""
        self.cache_path = SPOTIFY_CACHE_PATH
        self.auth_manager = ""

    def init_auth_manager(self, type="ClientCredentials"):
        if type == "ClientCredentials":
            return SpotifyClientCredentials(client_id=self.client_id,
                                            client_secret=self.client_secret)
        elif type == "OAuth":
            return SpotifyOAuth(scope="playlist-modify-private",
                                redirect_uri=SPOTIFY_REDIRECT_URI,
                                client_id=self.client_id,
                                client_secret=self.client_secret,
                                show_dialog=True,
                                cache_path=self.cache_path)
        return None

    def search_uri(self, song):
        self.init_auth_manager("ClientCredentials")
        spotify = spotipy.Spotify(auth_manager=self.auth_manager)
        query = f"track:{song.track} artist:{song.artist}"
        results = spotify.search(q=query, type='track', market='GB', limit=10, offset=5)
        try:
            song.uri = results["tracks"]["items"][0]["uri"]
        except IndexError:
            song.uri = None
            print(f"{song.track} doesn't exist in Spotify. Skipped.")


    def create_playlist(self, playlist_name, songs):
        songs.display()
        spotify = spotipy.Spotify(auth_manager=self.auth_manager)

        self.user_id = spotify.current_user()["id"]
        playlist = spotify.user_playlist_create(user=self.user_id, name=playlist_name, public=False)
        uris = songs.get_uris()
        spotify.playlist_add_items(playlist_id=playlist["id"], items=uris)

    # def search_by_name(name="bts"):
    #     spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
    #                                                                     client_secret=SPOTIFY_CLIENT_SECRET))
    #
    #     results = spotify.search(q='artist:' + name, type='artist')
    #     items = results['artists']['items']
    #     print(items)
    #     if len(items) > 0:
    #         artist = items[0]
    #         print(artist['name'], artist['images'][0]['url'])
    #
    #


    # def spotify_get_token():
    #     security = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    #     encoded = base64.b64encode(security.encode("ascii"))
    #     encoded = str(encoded, encoding="utf-8")
    #
    #     headers = {
    #         "Authorization": f"Basic {encoded}",
    #         "Content-Type": "application/x-www-form-urlencoded"
    #     }
    #     param = {
    #         "grant_type": "client_credentials"
    #     }
    #     token = requests.post(url=SPOTIFY_TOKEN_URL, headers=headers, params=param).json()
    #     return token["access_token"]
    #

