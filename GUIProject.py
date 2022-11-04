#LIBRARIES
import tkinter
from tkinter import *

from ReadCsvToNewCsv import *
from  Function import *
from PIL import Image, ImageTk
from menu_Program import *
from FunctionsGUI import *


#logoChooseImage=Image.open('images/choose_logo.png')
#checkImage=Image.open('images/check_icon.png')

#img_logo_choose=logoChooseImage.resize((30, 30))
#img_check=checkImage.resize((30,30))

#img_boton=ImageTk.PhotoImage(img_logo_choose)
#img_boton_check=ImageTk.PhotoImage(img_check)#

#PROGRAM--------------------------------------------------------------------
root= tkinter.Tk()
root.geometry("700x700")
root.title("Recomend Playlist Project")
playlist_tracks = getSongs()


#SONGS FRAME
songsFrame=LabelFrame(root,text="Songs os Playlist")
songsFrame.grid(row=0,column=0)
showListOfSongs(songsFrame,playlist_tracks)

#OPTIONS FRAME

optionsFrame=LabelFrame(root,text="Options")
optionsFrame.grid(row=0,column=1)

titleApp=tkinter.Label(optionsFrame,text="Recomend Playlist Project").grid(row=0,column=0)
secondaryTitle=tkinter.Label(optionsFrame,text="Write a song of this playlist!",bg="yellow").grid(row=1,column=0)

e=Entry(optionsFrame,width=50,bg="green",fg="white",borderwidth=3)
e.grid(row=2,column=0)
e.get()


buttonArtist=Button(optionsFrame,text="Filter By Group",command=lambda:pressButtonArtist(optionsFrame,e.get())).grid(row=3,column=0)
buttonSeems=Button(optionsFrame,text="Filter By Seems", command=lambda :pressButtonSeems(optionsFrame,e.get())).grid(row=4,column=0)
buttonPopularity=Button(optionsFrame,text="Filter By Popularity",command=lambda: pressButtonPopularity(optionsFrame,e.get())).grid(row=5,column=0)



#Check the song when you are pressing the botton









root.mainloop()


