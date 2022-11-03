from tkinter import *
from ReadCsvToNewCsv import *
from PIL import Image, ImageTk

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

