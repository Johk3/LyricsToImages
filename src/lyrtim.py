from __future__ import unicode_literals
import lyricsgenius
import pickle
import urllib.request
from bs4 import BeautifulSoup
import youtube_dl
import glob
from os import system

class LyricsToImages:
    def __init__(self):
        self.lyrics = pickle.load(open("lyrics.p", "rb"))
        self.songs = ["Shotta Flow", "Shotta Flow 2", "IDK"]
        self.lyrdic = None
        self.urls = ["https://www.youtube.com/watch?v=3W0e7aI0gAg",
                    "https://www.youtube.com/watch?v=_Pnam7Fg5jQ",
                    "https://www.youtube.com/watch?v=lFPWcn68nz0"]
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
        # Lyrdic stores all the lyrics corresponding to each song
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
            tempUrls = []
            textToSearch = song
            query = urllib.parse.quote(textToSearch)
            url = "https://www.youtube.com/results?search_query=" + query
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            i = 0
            print(song)
            for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                print('{}. https://www.youtube.com'.format(i) + vid['href'])
                tempUrls.append('https://www.youtube.com' + vid['href'])
                i += 1
            select = int(input(": "))
            self.urls.append(tempUrls[select])


    def compileVideo(self):
        # Merge the lyrics and images in sync together to form a one solid video
        # Translate the whole audio of the music into text (Include time stamps)
        # Try to match up the genius lyrics with the songs lyrics
        i = 0
        for song in self.urls:
            break
            # Download the song
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([song])
            print("Downloaded {}.mp3".format(self.songs[i]))
            move = glob.glob("*.mp3")[0]
            system('mv "{}" songs'.format(move))
            i += 1
            break
