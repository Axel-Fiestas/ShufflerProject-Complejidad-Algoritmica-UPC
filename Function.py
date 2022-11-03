from ConvertFunctions import *

def equalArtist(songSelected,songCompare):
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


def generateNodesCaseByArtist(grafo,songSelected,playlist_tracks):
    for track in playlist_tracks:
        isTheSameArtist = equalArtist(songSelected, track)
        if (isTheSameArtist):
            grafo.add_node(track.name)

def generateNodesCaseBySeems(grafo,songSelected,playlist_tracks,numberOfPlaylist):
    tamanioDelGrafo=0
    pesoIndicador=0
    while(tamanioDelGrafo<numberOfPlaylist):
        pesoIndicador += 1

        for track in playlist_tracks:

            if (tamanioDelGrafo == numberOfPlaylist): break

            peso = value(songSelected, track)
            if (peso == pesoIndicador and songSelected.name!=track.name):
                grafo.add_node(track.name)
                grafo.add_edge(songSelected.name, track.name, weight=peso)
                tamanioDelGrafo+=1


def generateNodesCaseByPopularity(grafo,songSelected,playlist_tracks):
    for track in playlist_tracks:
        if(getPopularityValue(track.popularity)==getPopularityValue(songSelected.popularity)):
            grafo.add_node(track.name)

def value(song1,song2):

    value1=1

    for genero in song1.genres:

        if(value1<=10):
            if(genero in song2.genres):
                value1+=0
            else:
                value1+=1

    bS1=getTempoValue(song1.tempo)
    bS2=getTempoValue(song2.tempo)
    final2=bS1-bS2
    final_final2=max(final2,-final2)

    value1 += final_final2

    return value1



def AllConection(playlist_tracks,grafo,songSelected,limitDistance):
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
            if(peso<=limitDistance):
                grafo.add_edge(songSelected.name, playlist_tracks[i].name, weight=peso)
                #grafo.remove_node(1)

    print(grafo)
    print(list(grafo.nodes))

def conectionByPopularity(playlist_tracks,grafo,songSelected):
    for i in range(len(playlist_tracks)):
        if(songSelected.name!=playlist_tracks[i].name):
            if(getPopularityValue(songSelected.popularity)==getPopularityValue(playlist_tracks[i].popularity)):
                grafo.add_edge(songSelected.name,playlist_tracks[i].name)