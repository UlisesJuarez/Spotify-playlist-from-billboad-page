from bs4 import BeautifulSoup
from h11 import CLIENT
import requests
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
CLIENT_ID=os.getenv("spotify_client_id")
CLIENT_SECRET=os.getenv("spotify_client_secret")


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        redirect_uri="http://example.com/playlist",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print("Top 100 hits a lo largo de la historia!!")
date = input("Ingresa la fecha en este formato: YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

soup = BeautifulSoup(response.content, "lxml")

songs_names = soup.find_all('h3',{'class':"c-title"})
song_list=[]

for song in range(6,len(songs_names),4):
    if len(song_list)<100:
        song_list.append(songs_names[song].text.strip("\n"))
# 2012-11-18

for i in range(0,len(song_list)):
    print(f"{i+1}.- {song_list[i]}")