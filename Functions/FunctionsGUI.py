import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from ReadCsvToNewCsv import *
from Functions.Function import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter import messagebox






def showSongs(root, img_boton, printNameSong):
    botons = []
    rowIterador = 2

    for i in range(len(playlist_tracks)):
        songName = playlist_tracks[i].name
        myLabel = Label(root, text=songName)

        myLabel.grid(row=rowIterador, column=0)
        botons.append(Button(root, image=img_boton, padx=0, pady=0, text=songName,
                             command=lambda c=i: printNameSong(botons[c].cget("text"))))
        botons[i].grid(row=rowIterador, column=1)  # this packs the buttons

        rowIterador += 1



def extracSong(song, playlist_tracks):
    for track in playlist_tracks:
        if song == track.name:
            return track


def messageErrorSongNotFound():
    messagebox.showerror("Shuffler", "La cancion ingresada no es valida")

def messageErrorNothingSong():
    messagebox.showwarning("Shufflger", "No se ha encontrado ninguna cancion que contenga los caracteres")

def messageNothingChoose():
    messagebox.showerror("Shuffler", "No has selccionado ninguna cancion")

def pressButonCheck(song):
    if (checkSong(song, playlist_tracks)):
        return True
    else:
        messageErrorSongNotFound()
        return False




def showListOfSongs(root,listOfSongs):
    scrollbar = Scrollbar(root, orient="vertical")

    SelectuserLabel = Label(root, text="Copy Name of Your Song").grid(row=0, column=0)
    test = Listbox(root, width=40, height=35, font=("Helvetica", 10))
    for song in listOfSongs:
        test.insert(END,song.name)
    test.grid(row=1, column=0)
    scrollbar.config(command=test.yview)
    scrollbar.grid(row=0, column=2, sticky='ns')



def showListOfSelectedSongs(root, listOfSongs):
    scrollbar = Scrollbar(root, orient="vertical")
    test = Listbox(root, width=20, height=5, font=("Helvetica", 10))

    for x in listOfSongs:
        test.insert(END, x)

    test.grid(row=6, column=0)
    scrollbar.config(command=test.yview)
    scrollbar.grid(row=7, column=1, sticky='ns')


lista_images_artist=[]
def tableArtist(my_tree,song,data_list):

    global lista_images_artist
    lista_images_artist=[]
    i=1
    count=0
    for item in my_tree.get_children():
        my_tree.delete(item)
    for record in data_list:
        if song.artist==record[1]:
            image = Image.open(f'AlbumsCover/album_number_{str(i)}.png')
            resized = image.resize((40, 40))
            new_photo = ImageTk.PhotoImage(resized)
            # photo = ImageTk.PhotoImage(image)
            lista_images_artist.append(new_photo)
            my_tree.insert(parent='', index='end', image=lista_images_artist[count], iid=count, text="",
                           values=(record[0], record[1], record[2], record[3]))
            count += 1
        i += 1

def ButtonArtist(root, songName,my_tree,data_list):
    grafo = nx.Graph()  # Creamos el grafo
    song = extracSong(songName, playlist_tracks)
    tableArtist(my_tree,song,data_list)
    generateNodesCaseByArtist(grafo, song, playlist_tracks)  # Generamos los nodos de canciones
    # Se emplearán los Conjuntos disjuntos , para este caso
    listaId = []  # Lista de Ids
    #diccionario = {}  # Diccionario que tendra el Id de cada diccionario
    diccionario_objetos = {}  # Diccionario que tendra el objeto en si para poder acceder a sus variables
    # Definimos la lista de ids (que seran los artistas) y lo demas que servirá como conexión para verificar si una canción
    # comparte conexión (comparten mismo artista) con otra
    for i in range(len(playlist_tracks)):
        #diccionario[playlist_tracks[i].name] = i  # Paranoid : 1
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
    # AQUI SE IMPRIME
    songs_of_group = list(grafo.adj[song.artist])
    # print(f"Songs Of artist ''{song.artist}'' in the playlist are: ")



    #showListOfSelectedSongs(root, songs_of_group)
    nx.draw(grafo, pos=nx.spring_layout(grafo), with_labels=True)
    plt.show()


lista_images_seems = []
def tableSeems(my_tree, data_list,songs_of_seems):
    global lista_images_seems
    lista_images_seems = []

    count = 0

    for item in my_tree.get_children():
        my_tree.delete(item)

    for track in songs_of_seems:
        i = 1

        for record in data_list:
            if track == record[0]:
                image = Image.open(f'AlbumsCover/album_number_{str(i)}.png')
                resized = image.resize((40, 40))
                new_photo = ImageTk.PhotoImage(resized)
                # photo = ImageTk.PhotoImage(image)
                lista_images_seems.append(new_photo)
                my_tree.insert(parent='', index='end', image=lista_images_seems[count], iid=count, text="",
                               values=(record[0], record[1], record[2], record[3]))
                count += 1
                break

            i += 1

def ButtonSeems(root, songName,numberOfPlaylist,my_tree,data_list):

    grafo = nx.Graph()  # Creamos el grafo
    song = extracSong(songName, playlist_tracks)  # Extraemos la cancion
    grafo.add_node(song.name)  # Añadimos el nodo de la cancion
    # showinfo('Hello!', 'Hi, {}'.format(name))
    generateNodesCaseBySeems(grafo, song, playlist_tracks, numberOfPlaylist)
    # Realizamos y mostramos el grafo de las canciones con su respectiva similitud
    elarge = [(u, v) for (u, v, d) in grafo.edges(data=True) if d["weight"] > 5]
    esmall = [(u, v) for (u, v, d) in grafo.edges(data=True) if d["weight"] <= 5]
    pos = nx.spring_layout(grafo, seed=4)
    nx.draw_networkx_nodes(grafo, pos, node_size=700)
    nx.draw_networkx_edges(grafo, pos, edgelist=elarge, width=3)
    nx.draw_networkx_edges(
        grafo, pos, edgelist=esmall, width=3, alpha=0.5, edge_color="b", style="dashed"
    )
    nx.draw_networkx_labels(grafo, pos, font_size=8, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(grafo, "weight")
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels)
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    songs_of_seems = list(grafo.adj[song.name])

    tableSeems(my_tree,data_list,songs_of_seems)

    plt.show()

lista_images_popularity=[]
def tablePopularity(my_tree, data_list,songs_of_popularity):
    global lista_images_popularity
    lista_images_popularity=[]

    count = 0

    for item in my_tree.get_children():
        my_tree.delete(item)

    for track in songs_of_popularity:
        i = 1

        for record in data_list:
            if track == record[0]:
                image = Image.open(f'AlbumsCover/album_number_{str(i)}.png')
                resized = image.resize((40, 40))
                new_photo = ImageTk.PhotoImage(resized)
                # photo = ImageTk.PhotoImage(image)
                lista_images_popularity.append(new_photo)
                my_tree.insert(parent='', index='end', image=lista_images_popularity[count], iid=count, text="",
                               values=(record[0], record[1], record[2], record[3]))
                count += 1
                break

            i += 1

def ButtonPopularity(root, songName,numberOfPlaylist,my_tree,data_list):
    grafo = nx.Graph()  # Creamos el grafo
    song = extracSong(songName, playlist_tracks)  # Extraemos la cancion
    generateNodesCaseByPopularity(grafo, song, playlist_tracks,numberOfPlaylist)
    conectionByPopularity(playlist_tracks, grafo, song,numberOfPlaylist)
    songs_of_group = list(grafo.adj[song.name])

    tableSeems(my_tree,data_list,songs_of_group)

    nx.draw(grafo, pos=nx.spring_layout(grafo), with_labels=True)
    plt.show()

