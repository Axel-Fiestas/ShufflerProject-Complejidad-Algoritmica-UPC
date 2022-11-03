from tkinter import *
from ReadCsvToNewCsv import *
from PIL import Image, ImageTk
import networkx as nx
import matplotlib.pyplot as plt
from menu_Program import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

def showSongs(root,img_boton,printNameSong):

    botons=[]
    rowIterador=2

    for i in range(len(playlist_tracks)):
        songName=playlist_tracks[i].name
        myLabel=Label(root,text=songName)

        #botonSeleccionador=Button(root,image=img_boton,command= lambda : printNameSong(myLabel.cget("text")))
        myLabel.grid(row=rowIterador,column=0)

        botons.append(Button(root,image=img_boton, padx=0, pady=0,text=songName, command=lambda c=i: printNameSong(botons[c].cget("text"))))
        botons[i].grid(row=rowIterador,column=1) # this packs the buttons

        rowIterador += 1

        #boton = Button(root,image=img_boton, padx=0, pady=0, command=lambda: actualizaBoton(estaSeleccionado.get()))
        #boton.grid(row=rowIterador,column=1)

        #if not isSelected:
        #    boton.configure(image=img_boton)
        #else:
        #    boton.configure(image=img_boton_check, state=DISABLED)
        #botonSeleccionador.grid(row=rowIterador,column=1)

def extracSong(song,playlist_tracks):
    for track in playlist_tracks:
        if song==track.name:
            return track

def pressButtonArtist(songName):

    grafo = nx.Graph()  # Creamos el grafo

    song=extracSong(songName,playlist_tracks)

    generateNodesCaseByArtist(grafo, song, playlist_tracks)  # Generamos los nodos de canciones
    # Se emplearán los Conjuntos disjuntos , para este caso
    listaId = []  # Lista de Ids
    diccionario = {}  # Diccionario que tendra el Id de cada diccionario
    diccionario_objetos = {}  # Diccionario que tendra el objeto en si para poder acceder a sus variables
    # Definimos la lista de ids (que seran los artistas) y lo demas que servirá como conexión para verificar si una canción
    # comparte conexión (comparten mismo artista) con otra
    for i in range(len(playlist_tracks)):
        diccionario[playlist_tracks[i].name] = i  # Paranoid : 1
        diccionario_objetos[i] = playlist_tracks[i]  # ObjetoCancion(Paranoid) : 1
        listaId.append(playlist_tracks[i].artist)  # lista[1] = Black Sabbath
    grafo.add_node(
        song.artist)  # En el caso de filtración por artistas SOLO se añade el artista de la canción elegida como un nodo
    # print(diccionario)
    # print(diccionario_objetos)
    # print(listaId)
    # Generar las conexiones de aristas y mostrar el grafo
    for i in range(len(listaId)):
        # i-> valor
        # listaid[i] -> id
        valor = diccionario_objetos[i].artist
        if (valor == listaId[i] and valor == song.artist):
            grafo.add_edge(diccionario_objetos[i].name, listaId[i])
    songs_of_group = list(grafo.adj[song.artist])
    print(f"Songs Of artist ''{song.artist}'' in the playlist are: ")
    for x in songs_of_group:
        print(x)
    nx.draw(grafo, pos=nx.spring_layout(grafo), with_labels=True)
    plt.show()

def pressButtonSeems(songName):

    grafo = nx.Graph()  # Creamos el grafo
    song=extracSong(songName,playlist_tracks)# Extraemos la cancion

    grafo.add_node(song.name)#Añadimos el nodo de la cancion

    numberOfPlaylist = int(askstring('Quantity', 'How many songs do you need?'))
    #showinfo('Hello!', 'Hi, {}'.format(name))

    generateNodesCaseBySeems(grafo, song, playlist_tracks,numberOfPlaylist)
    #Realizamos y mostramos el grafo de las canciones con su respectiva similitud
    elarge = [(u, v) for (u, v, d) in grafo.edges(data=True) if d["weight"] > 5]
    esmall = [(u, v) for (u, v, d) in grafo.edges(data=True) if d["weight"] <= 5]
    pos = nx.spring_layout(grafo, seed=4)
    nx.draw_networkx_nodes(grafo, pos, node_size=700)
    nx.draw_networkx_edges(grafo, pos, edgelist=elarge, width=3)
    nx.draw_networkx_edges(
        grafo, pos, edgelist=esmall, width=3, alpha=0.5, edge_color="b", style="dashed"
    )
    nx.draw_networkx_labels(grafo, pos, font_size=20, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(grafo, "weight")
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels)
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()


    songs_of_seems = list(grafo.adj[song.name])
    print(f"Songs Of Seems that ''{song.name}'' in the playlist are: ")
    for x in songs_of_seems:
       print(x)

    plt.show()

def pressButtonPopularity(songName):

    grafo = nx.Graph()  # Creamos el grafo
    song=extracSong(songName,playlist_tracks)# Extraemos la cancion

    generateNodesCaseByPopularity(grafo, song, playlist_tracks)
    conectionByPopularity(playlist_tracks,grafo,song)

    songs_of_group=list(grafo.adj[song.name])
    print(f"Songs Of same popularity in the playlist are: ")
    for x in songs_of_group:
       print(x)

    nx.draw(grafo, pos=nx.spring_layout(grafo), with_labels=True)
    plt.show()