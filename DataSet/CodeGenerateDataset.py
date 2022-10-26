import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

client_id = "3dee3d8ea57c4586b454a51dc1b78a88"
client_secret = "edcf663c85ce4864a49c24acd8b7915a"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = "Axekran"
playlist_link=input("Enter the playlist link: ")
playlist_URI = playlist_link.split("/")[-1].split("?")[0]

def get_playlist_tracks():
    sp_playlist = sp.user_playlist_tracks(username, playlist_id=playlist_URI)
    tracks = sp_playlist['items']
    while sp_playlist['next']:
        sp_playlist = sp.next(sp_playlist)
        tracks.extend(sp_playlist['items'])
    return tracks

def get_list_songs(tracks_ids):
    list_listas=[]

    i=0

    for song in tracks_ids:

        if(i<1):
            name_track = song["track"]["name"]
            artist_track = song["track"]["artists"][0]["name"]
            uri_track = song["track"]["uri"]

            features = sp.audio_features(uri_track)[0]

            danceability = round(features["danceability"]*100)
            popularity=song["track"]["popularity"]

            lista = [name_track, artist_track, uri_track,popularity,danceability]

            list_listas.append(lista)

            print(json.dumps(song,indent=2))

            i+=1
        else:
            break

    return list_listas


track_list  = get_playlist_tracks()#
list_songs  = get_list_songs(track_list)
#headers=["name_track","artist_track","uri_track","popularity","danceability"]


#print(len(list_songs))
#print(list_songs)

#Generación del dataset usando la librería csv
#with open("songs_list_1.csv","w",encoding="utf-8") as file:
#    song=csv.writer(file)
#    song.writerow(headers)
#    song.writerows(list_songs)
