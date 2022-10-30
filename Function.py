from ConvertFunctions import *

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

def generateNodes(grafo,songSelected,playlist_tracks,case):

    if case == "FilterByArtist":
        for track in playlist_tracks:
            if(track.artist==songSelected.artist):
                grafo.add_node(track.name)
    elif case=="FilterBySeems":
        for track in playlist_tracks:
            peso=value(songSelected,track)
            if(peso<=2):
                grafo.add_node(track.name)




def value(song1,song2):

    value1=1
    #if not EqualArtist(song1,song2): value1+=1
    for genero in song1.genres:
        if genero not in song2.genres:
            if (value1 <=10):
                value1+=1

    pS1=getPopularityValue(song1.popularity)
    pS2=getPopularityValue(song2.popularity)
    final=pS1-pS2
    final_final=max(final,-final)

    value1+=final_final

    return value1



def AllConection(playlist_tracks,grafo,songSelected):
    #for i in range(len(playlist_tracks)):
    #    for j in range(len(playlist_tracks)-1):
    #        if (playlist_tracks[i].name != playlist_tracks[j].name):
    #            peso=value(playlist_tracks[i],playlist_tracks[j])
    #            if(peso<=3):
    #                grafo.add_edge(playlist_tracks[i].name,playlist_tracks[j].name,weight=peso)
    #            else:
    #                grafo.remove_node(playlist_tracks[j].name)
    for i in range(len(playlist_tracks)):
        if(songSelected.name!=playlist_tracks[i].name):
            peso=value(songSelected,playlist_tracks[i])
            if(peso<=1):
                grafo.add_edge(songSelected.name,playlist_tracks[i].name,weight=peso)
                #grafo.remove_node(1)

    print(grafo)
    print(list(grafo.nodes))