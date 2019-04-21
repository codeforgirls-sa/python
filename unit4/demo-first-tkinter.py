from tkinter import *

window = Tk() #create the base window where ALL widgets go

window.geometry("300x100") #sets the size of the window

lbl = Label(window, text="Hello World") #create label with words/titles

lbl.grid(column=0, row=0) #put the label in the window

window.mainloop() #start the event loop
