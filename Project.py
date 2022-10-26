import matplotlib.pyplot as plt
from Function import *
from classes import Song
from classes import Graphs
from ReadCsvToNewCsv import *
from menu_Program import *
import networkx as nx

# Obtenemos las canciones del dataset
playlist_tracks = getSongs()

# Imprimimos las canciones
printSongs(playlist_tracks)

# Imprimimos el menú
array = menu()
option = int(array[0])
song = array[1]

# Le damos al usuario la opcion de elegir la canción
songChoosedInformation = checkSong(song, playlist_tracks)

# Creamos el grafo con ayuda de la librería
grafo = nx.Graph()
# Generamos los nodos del grafo de canciones
generateNodes(grafo, songChoosedInformation, playlist_tracks)

#PARA FILTRACION POR ARTISTA
#Se supone que en el arreglo iran las canciones , el Id respectivo será el artista, tal vez se pueda hacer un diccionario
lista = [] #Lista de Ids
diccionario = {} #Diccionario que tendra el Id de cada diccionario
diccionario_objetos = {} #Diccionario que tendra el objeto en si para poder acceder a sus variables
# Definimos la lista de ids (que seran los artistas) y la otra vaina
for i in range(len(playlist_tracks)):

    diccionario[playlist_tracks[i].name] = i  # Paranoid : 1
    diccionario_objetos[i] = playlist_tracks[i] #ObjetoCancion(Paranoid) : 1
    lista.append(playlist_tracks[i].artist) # lista[1] = Black Sabbath

    grafo.add_node(playlist_tracks[i].artist) #En el caso de filtración por artistas se añade el artista como un nodo

#print(lista)
#print(diccionario)


# Tengo que hallar una forma de pasar de string de cancion a su numero ID
def connected(array, song1, song2):
    # p and q -> name song
    p = diccionario[song1]
    q = diccionario[song2]
    # Tengo que hallar la posicion de su arreglo
    return array[p] == array[q]
    # v = "Shine On"


# Generar las conexiones de aristas y mostrar el grafo
for i in range(len(lista)):
    # i-> valor
    # lista[i] -> id
    valor = diccionario_objetos[i].artist
    if valor == lista[i]:
        grafo.add_edge(diccionario_objetos[i].name,lista[i])


lista_canciones_del_grupo=list(grafo.adj["R.E.M."])
print("Las canciones del grupo en el playlist son: ")
for x in lista_canciones_del_grupo:
    print(x)

nx.draw(grafo, pos=nx.spring_layout(grafo), with_labels=True)
plt.show()



##AQUI TERMINA
############################################### OPCIONES (DE MOMENTO COMENTADO)


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