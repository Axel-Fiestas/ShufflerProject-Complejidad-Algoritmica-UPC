#LIBRARIES
import tkinter
from tkinter import *
from ReadCsvToNewCsv import *
from PIL import Image, ImageTk
from menu_Program import *
import networkx as nx

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

def printTheMessage(message):
    new_label=Label(root,text="Look, the message is: "+message)
    new_label.grid(row=2,column=2)




titleApp=tkinter.Label(root,text="Recomend Playlist Project").grid(row=0,column=0)
secondaryTitle=tkinter.Label(root,text="Write a song of this playlist!",bg="yellow").grid(row=1,column=0)

playlist_tracks = getSongs()

e=Entry(root,width=50,bg="green",fg="white",borderwidth=3)
e.grid(row=2,column=0)
e.get()














root.mainloop()


