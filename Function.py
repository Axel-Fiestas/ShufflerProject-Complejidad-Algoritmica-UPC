def EqualArtist(songSelected,songCompare):
    if(songSelected.artist==songCompare.artist):
        return True
    else:
        return False

def printSongs(playlist_tracks):
    for i in range(len(playlist_tracks)):
        print(f"[{i}].{playlist_tracks[i].name}")

def checkSong(song,playlist_tracks):
    for i in range(len(playlist_tracks)):
        if (song == playlist_tracks[i].name):
            return playlist_tracks[i]
    return False

def generateNodes(grafo,songSelected,playlist_tracks):
    for track in playlist_tracks:
        #if (songSelected.name != track.name):
        grafo.add_node(track.name)
            # print(track.artist,EqualArtist(songChoosedInformation,track))
#0-20 -> 1
#20-40 -> 2
#40-60 -> 3
#60-80 -> 4
#80-100 ->5
def getPopularityValue(popularity):
    popularity=int(popularity)
    if 0<=popularity<=20:return 1
    elif 20<popularity<=40:return 2
    elif 40<popularity<=60:return 3
    elif 60<popularity<=80:return 4
    elif 80<popularity<=100:return 5

def separateByArtist(playlist_tracks,grafo):
    for i in range(len(playlist_tracks)):
        for j in range(len(playlist_tracks)-1):
            if(playlist_tracks[i].artist==playlist_tracks[j].artist):
                if(playlist_tracks[i].name!=playlist_tracks[j].name):
                    grafo.add_edge(playlist_tracks[i].name,playlist_tracks[j].name)


def value(song1,song2):

    value1=1
    if not EqualArtist(song1,song2): value1+=1

    for genero in song1.genres:
        if genero not in song2.genres:
            if (value1 <=10):
                value1+=1

    pS1=getPopularityValue(song1.popularity)
    pS2=getPopularityValue(song2.popularity)
    final=pS1-pS2
    final_final=max(final,-final)
    print(pS1, pS2, final_final)

    value1+=final_final

    return value1



def AllConection(playlist_tracks,grafo):
    for i in range(len(playlist_tracks)):
        for j in range(len(playlist_tracks)-1):
            if (playlist_tracks[i].name != playlist_tracks[j].name):
                peso=value(playlist_tracks[i],playlist_tracks[j])
                if(peso<=5):
                    grafo.add_edge(playlist_tracks[i].name,playlist_tracks[j].name,weight=peso)