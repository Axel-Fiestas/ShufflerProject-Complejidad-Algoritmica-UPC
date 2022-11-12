#LIBRARIES
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
import customtkinter
from Functions.FunctionsGUI import *
from ReadCsvToNewCsv import *
import webbrowser

#PROGRAM--------------------------------------------------------------------
root= tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("Shuffler")
root.configure(bg='#3B9E8B')
playlist_tracks = getSongs()
p1 = PhotoImage(file='images/music_logo.png')
root.iconphoto(False, p1)


#Open Image
my_pic=Image.open("images/Logo.png")
#Resize image
resized=my_pic.resize((100,100))
new_pic=ImageTk.PhotoImage(resized)
my_label=Label(root,image=new_pic)
my_label.pack(pady=10)


data_list=[]
for track in playlist_tracks:

    lista=[track.name,track.artist,track.uri_track,track.album]
    data_list.append(lista)



#Create TreeFrame
tree_frame=Frame(root)
tree_frame.pack(pady=5)

#Create Treeview scrollbar
tree_scroll=Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

#Create Treeview
my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,height=18)
my_tree.pack()


#Configure Scrollbar
tree_scroll.config(command=my_tree.yview)


#Add some style

style=ttk.Style()

style.theme_use("default")

style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=45,
                fieldbackground="#3B9E8B")


style.map("Treeview",background=[("selected","#111111")])


my_tree["columns"]=("Name","Artist","url","Album")

#Formate our columns
my_tree.column("#0",width=80)
my_tree.column("Name",anchor=W,width=500)
my_tree.column("Artist",anchor=CENTER,width=500)
my_tree.column("url",width=0)
my_tree.column("Album",anchor=W,width=500)


#Create Headings
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("Name",text="Song",anchor=W)
my_tree.heading("Artist",text="Artist",anchor=CENTER)
my_tree.heading("url",text="",anchor=W)
my_tree.heading("Album",text="Album",anchor=W)


my_tree["displaycolumns"]=("Name","Artist","Album")

def selected_one():
    selected=my_tree.focus()
    temp=my_tree.item(selected,'values')
    print(temp[2])

def open_song_in_spotify():
    selected=my_tree.focus()
    temp=my_tree.item(selected,'values')
    spotify_uri=temp[2][14:]
    webbrowser.open(f'https://open.spotify.com/track/{spotify_uri}')


#ADD DATA


#my_tree.insert(parent='',index='end',iid=0,text="",values=("John",1,"Peperoni"))

count=0
i=1
lista=[]
for record in data_list:

    image = Image.open(f'AlbumsCover/album_number_{str(i)}.png')
    resized = image.resize((40, 40))
    new_photo = ImageTk.PhotoImage(resized)
    #photo = ImageTk.PhotoImage(image)
    lista.append(new_photo)

    my_tree.insert(parent='', index='end', image=lista[count],iid=count, text="", values=(record[0], record[1], record[2],record[3]))
    count+=1
    i+=1


###LISTEN SPOTIFY BUTTON
#FRAME BUTTONS



principalButtonsFrame=Frame(root,bg="#3B9E8B")
principalButtonsFrame.pack(pady=5)



choose_image=ImageTk.PhotoImage(Image.open("images/music_choose.png").resize((20,20),Image.ANTIALIAS))
button_choose=customtkinter.CTkButton(master=principalButtonsFrame,command=selected_one,image=choose_image,text="Choose Song!",width=100,height=40,compound="left",hover_color="green")
button_choose.grid(row = 0, column = 0)


spotify_image=ImageTk.PhotoImage(Image.open("images/spotify_logo.png").resize((20,20),Image.ANTIALIAS))
button_1=customtkinter.CTkButton(master=principalButtonsFrame,command=open_song_in_spotify,image=spotify_image,text="Listen in Spotify",width=100,height=40,compound="left",hover_color="green")
button_1.grid(row = 0, column = 1,padx= 10)


root.mainloop()





####ANTIGUO PROGRAMA
##SONGS FRAME
#songsFrame=LabelFrame(root,text="Songs of Playlist")
#songsFrame.grid(row=0,column=0)
#showListOfSongs(songsFrame,playlist_tracks)
#
##OPTIONS FRAME
#
#optionsFrame=LabelFrame(root,text="Options")
#optionsFrame.grid(row=0,column=1)
#
#titleApp=tkinter.Label(optionsFrame,text="Shuffler").grid(row=0,column=0)
#secondaryTitle=tkinter.Label(optionsFrame,text="Write a song of this playlist!",bg="yellow").grid(row=1,column=0)
#
#e=Entry(optionsFrame,width=50,bg="green",fg="white",borderwidth=3)
#e.grid(row=2,column=0)
#e.get()
#
##Check the song when you are pressing the botton
#
#def pressButtonArtist(root,song):
#    if pressButonCheck(song):
#        buttonArtist['state']=DISABLED
#        buttonPopularity['state'] = NORMAL
#        buttonSeems['state']=NORMAL
#        ButtonArtist(root, song)
#
#
#def pressButtonSeems(root,song):
#    if pressButonCheck(song):
#        buttonSeems['state']=DISABLED
#        buttonArtist['state']=NORMAL
#        buttonPopularity['state']=NORMAL
#        ButtonSeems(root,song)
#
#def pressButtonPopularity(root,song):
#    if pressButonCheck(song):
#        buttonPopularity['state'] = DISABLED
#        buttonSeems["state"]=NORMAL
#        buttonArtist["state"]=NORMAL
#        ButtonPopularity(root,song)
#
#
#buttonArtist=Button(optionsFrame,text="Filter By Group",command=lambda:pressButtonArtist(optionsFrame,e.get()))
#buttonArtist.grid(row=3,column=0)
#buttonSeems=Button(optionsFrame,text="Filter By Seems", command=lambda :pressButtonSeems(optionsFrame,e.get()))
#buttonSeems.grid(row=4,column=0)
#buttonPopularity=Button(optionsFrame,text="Filter By Popularity",command=lambda: pressButtonPopularity(optionsFrame,e.get()))
#buttonPopularity.grid(row=5,column=0)
#
#
#
#
#
#root.mainloop()


