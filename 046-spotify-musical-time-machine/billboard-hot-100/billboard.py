# import song classes
from song import Song, Songs
# others imports
import requests
from bs4 import BeautifulSoup
import datetime

# constants
BILLBOARD_DATE = "1979-07-11"
BILLBOARD_HOT_100_URL = "https://www.billboard.com/charts/hot-100"


class Billboard:

    def __init__(self):
        self.url = BILLBOARD_HOT_100_URL
        self.endpoint = BILLBOARD_DATE
        self.songs = Songs()

    def add_song(self, song):
        self.songs.add_songs(song)

    def ask_date(self):
        self.endpoint = input("Witch year do you want to tracel to? Type the date in this format YYYY-MM-DD ")
        try:
            datetime.date.fromisoformat(self.endpoint)
        except ValueError:
            self.ask_date()

    def get_billboard(self):
        response = requests.get(f"{self.url}/{self.endpoint}")
        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.select("li ul li h3")
        interprets = soup.find_all(name="span", class_="a-no-trucate")
        for title, interpret in zip(titles, interprets):
            new_song = Song(track=title.getText().strip(),
                            artist=interpret.getText().strip())
            self.add_song(new_song)
