from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
name = askstring('Name', 'What is your name?')
showinfo('Hello!', 'Hi, {}'.format(name))