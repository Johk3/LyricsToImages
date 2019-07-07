import lyricsgenius
import pickle
import urllib.request
from bs4 import BeautifulSoup

class LyricsToImages:
    def __init__(self):
        self.lyrics = pickle.load(open("lyrics.p", "rb"))
        self.songs = ["Shotta Flow", "Shotta Flow 2", "IDK"]
        self.lyrdic = None
        pass

    def getLyrics(self, creator):
        # Get lyrics
        lyrics = []

        with open("creds/client", "r+") as file:
            genius = lyricsgenius.Genius(file.readline())
        artist = genius.search_artist(creator, max_songs=3, sort="popularity")

        for song in artist.songs:
            self.songs.append(song)
            lyrics.append(song.lyrics)
        pickle.dump(lyrics, open("lyrics.p", "wb"))
        print("Dumped lyrics")
        print("Done")

    def getImages(self):
        # Get images randomly from google images
        lyrdic = {}

        for song in self.songs:
            lyrdic[song] = []

        i = 0
        for lyrics in self.lyrics:
            lyrics = lyrics.split("\n")
            for line in lyrics:
                if line != "" and line != " " and "[" not in line:
                    lyrdic[self.songs[i]].append(line.split(" "))
            i += 1
        self.lyrdic = lyrdic
        print("Lyrics ready!")

    def getAudio(self):
        # Get the audio of the music from some source
        for song in self.songs:
            textToSearch = song
            query = urllib.parse.quote(textToSearch)
            url = "https://www.youtube.com/results?search_query=" + query
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                print('https://www.youtube.com' + vid['href'])
            break

    def compileVideo(self):
        # Merge the lyrics and images in sync together to form a one solid video
        pass