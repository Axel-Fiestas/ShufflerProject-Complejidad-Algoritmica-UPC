from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import messagebox


root=Tk()
root.title("Learn To Code")
root.geometry("700x700")

songsFrame=LabelFrame(root,text="Songs os Playlist")
songsFrame.grid(row=0,column=0)


optionsFrame=LabelFrame(root,text="Options")
optionsFrame.grid(row=0,column=1)



button2=Button(optionsFrame,text="pRESIONAME P").pack()

scrollbar = Scrollbar(songsFrame, orient="vertical")

SelectuserLabel = Label(songsFrame, text="Select").grid(row=0, column=0)
test = Listbox(songsFrame, width=40, height=38, font=("Helvetica", 10))
test.insert(END, 1)
test.insert(END, 2)
test.insert(END, 3)
test.insert(END, 4)
test.insert(END, 5)
test.insert(END, 6)
test.insert(END, 7)
test.insert(END, 8)
test.grid(row=0, column=1)
scrollbar.config(command=test.yview)
scrollbar.grid(row=0, column=2, sticky='ns')

#Button(root,text="PopUp",command=popup).pack()

root.mainloop()