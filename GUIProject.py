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

def printTheMessage(message):
    new_label=Label(root,text="Look, the message is: "+message)
    new_label.grid(row=2,column=2)


titleApp=tkinter.Label(root,text="Recomend Playlist Project").grid(row=0,column=0)
secondaryTitle=tkinter.Label(root,text="Write a song of this playlist!",bg="yellow").grid(row=1,column=0)

playlist_tracks = getSongs()

e=Entry(root,width=50,bg="green",fg="white",borderwidth=3)
e.grid(row=2,column=0)
e.get()


buttonArtist=Button(root,text="Filter By Group",command=lambda:pressButtonArtist(e.get())).grid(row=3,column=0)
buttonSeems=Button(root,text="Filter By Seems", command=lambda :pressButtonSeems(e.get())).grid(row=3,column=1)
buttonPopularity=Button(root,text="Filter By Popularity",command=lambda: pressButtonPopularity(e.get())).grid(row=3,column=2)


#buttonExample=Button(root,text="ButtonExampleCheck",command=lambda: pressButon(e.get())).grid(row=3,column=0)



def pressButon(song):
    labelWarning = tkinter.Label(root, text="Something was wrong", bg="red")
    if(not checkSong(song,playlist_tracks)):
        labelWarning.grid(row=2,column=1)
        return False

    labelWarning.grid_remove()

    print("Hola!")

#Check the song when you are pressing the botton









root.mainloop()


