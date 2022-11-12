import tkinter
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, PhotoImage

root= tkinter.Tk()
root.geometry("1920x1080")
root.title("Shuffler")

#Create TreeFrame
tree_frame=Frame(root)
tree_frame.pack(pady=20)

#Create TreeFrame
tree_frame=Frame(root)
tree_frame.pack(pady=20)

#Create Treeview scrollbar
tree_scroll=Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

#Create Treeview
my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,height=35)
my_tree.pack()


#Configure Scrollbar
tree_scroll.config(command=my_tree.yview)


#Add some style

style=ttk.Style()

style.theme_use("default")

style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=50,
                fieldbackground="#D3D3D3")


style.map("Treeview",background=[("selected","green")])


my_tree["columns"]=("Name","ID","Favorite Pizza")

#Formate our columns
#my_tree.column("#0",width=0,stretch=NO)
my_tree.column("#0",width=80)
my_tree.column("Name",anchor=W,width=500)
my_tree.column("ID",anchor=CENTER,width=500)
my_tree.column("Favorite Pizza",anchor=W,width=500)


#Create Headings
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("Name",text="Name",anchor=W)
my_tree.heading("ID",text="ID",anchor=CENTER)
my_tree.heading("Favorite Pizza",text="Favorite Pizza",anchor=W)

def selected_one():
    selected=my_tree.focus()
    temp=my_tree.item(selected,'values')
    print(temp[2])



printRecord=Button(root,text="Print Record",command=selected_one)
printRecord.pack()
#ADD DATA

data=[
    ["John",1,"Pepperoni"],
    ["Mary",2,"Cheese"],
    ["Tim",3,"Mushroom"],
    ["Erin",4,"Ham"],
    ["Bob",5,"Onion"],
    ["Bob",5,"Onion"],

]
#my_tree.insert(parent='',index='end',iid=0,text="",values=("John",1,"Peperoni"))
count=0
i=1
lista=[]
for record in data:

    image = Image.open(f'AlbumsCover/album_number_{str(i)}.png')
    resized = image.resize((40, 40))
    new_photo = ImageTk.PhotoImage(resized)
    #photo = ImageTk.PhotoImage(image)
    lista.append(new_photo)

    my_tree.insert(parent='', index='end', image=lista[count],iid=count, text="", values=(record[0], record[1], record[2]))
    count+=1
    i+=1










root.mainloop()