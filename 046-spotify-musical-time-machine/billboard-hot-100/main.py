from billboard import Billboard
from spotify import Spotify


def main():
    billboard = Billboard()
    # billboard.ask_date()
    billboard.get_billboard()
    # Search song in Billboard 100 and song data in Spotify
    billboard.songs.display()

    spotify = Spotify()
    playlist_name = f"{billboard.endpoint} Billboard 100"
    spotify.create_playlist(playlist_name=playlist_name, songs=billboard.songs)


if __name__ == "__main__":
    main()

