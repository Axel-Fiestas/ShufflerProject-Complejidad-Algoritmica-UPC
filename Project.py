import matplotlib.pyplot as plt
from Function import *
from classes import Song
from classes import Graphs
from ReadCsvToNewCsv import *
from menu_Program import *
import networkx as nx

# Obtenemos las canciones del dataset
playlist_tracks = getSongs()

# Elegimos cancion
song=FirstMenu(playlist_tracks)
try:
    anyValue=song
    option=SecondMenu(song) #Elegimos la opcion
    grafo=nx.Graph() #Creamos el grafo
    generateNodes(grafo, song, playlist_tracks)#Generamos los nodos de canciones
    if(option==1):

        #Se emplearán los Conjuntos disjuntos , para este caso
        listaId = [] #Lista de Ids
        diccionario = {} #Diccionario que tendra el Id de cada diccionario
        diccionario_objetos = {} #Diccionario que tendra el objeto en si para poder acceder a sus variables

        #Definimos la lista de ids (que seran los artistas) y lo demas que servirá como conexión para verificar si una canción
        #comparte conexión (comparten mismo artista) con otra

        for i in range(len(playlist_tracks)):
           diccionario[playlist_tracks[i].name] = i  # Paranoid : 1
           diccionario_objetos[i] = playlist_tracks[i] #ObjetoCancion(Paranoid) : 1
           listaId.append(playlist_tracks[i].artist) # lista[1] = Black Sabbath
           grafo.add_node(playlist_tracks[i].artist) #En el caso de filtración por artistas se añade el artista como un nodo

        #print(diccionario)
        #print(diccionario_objetos)
        #print(listaId)

        #Generar las conexiones de aristas y mostrar el grafo
        for i in range(len(listaId)):
           # i-> valor
           # listaid[i] -> id
           valor = diccionario_objetos[i].artist
           if (valor == listaId[i] and valor==song.artist) :
               grafo.add_edge(diccionario_objetos[i].name,listaId[i])


        songs_of_group=list(grafo.adj[song.artist])
        print(f"Songs Of artist ''{song.artist}'' in the playlist are: ")
        for x in songs_of_group:
           print(x)

        nx.draw(grafo, pos=nx.spring_layout(grafo), with_labels=True)
        plt.show()

except:
    #En caso pasa algo malo
    print("END")




############################################### OPCIONES VERSION ANTERIOR (DE MOMENTO COMENTADO)


#if (option == 1):
#   # Separar por artista a hacer una conexión toda xd
#   separateByArtist(playlist_tracks, grafo)
#   nx.draw(grafo, pos=nx.spring_layout(grafo), with_labels=True)
#   plt.show()
#elif (option == 2):
#   # Realizamos y mostramos el grafo de las canciones con su respectiva similitud
#   AllConection(playlist_tracks, grafo)
#   elarge = [(u, v) for (u, v, d) in grafo.edges(data=True) if d["weight"] > 5]
#   esmall = [(u, v) for (u, v, d) in grafo.edges(data=True) if d["weight"] <= 5]
#   pos = nx.spring_layout(grafo, seed=4)
#   nx.draw_networkx_nodes(grafo, pos, node_size=700)
#   nx.draw_networkx_edges(grafo, pos, edgelist=elarge, width=3)
#   nx.draw_networkx_edges(
#       grafo, pos, edgelist=esmall, width=3, alpha=0.5, edge_color="b", style="dashed"
#   )
#   nx.draw_networkx_labels(grafo, pos, font_size=20, font_family="sans-serif")
#   edge_labels = nx.get_edge_attributes(grafo, "weight")
#   nx.draw_networkx_edge_labels(grafo, pos, edge_labels)
#   ax = plt.gca()
#   ax.margins(0.08)
#   plt.axis("off")
#   plt.tight_layout()
#   plt.show()
#