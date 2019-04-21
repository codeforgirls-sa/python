from tkinter import *
 
window = Tk()
window.title("°C to °F converter")
window.geometry('350x200')

celsius = Entry(window, width=10, text=100)
celsius.grid(column=0, row=0)

lbl = Label(window, text="°C")
lbl.grid(column=1, row=0)

fahrenheit = Label(window, text="°F")
fahrenheit.grid(column=1, row=1)

def clicked():
	convert = float(celsius.get()) * 1.8 + 32
	res = str(convert) + "°F"
	fahrenheit.configure(text=res)
 
btn = Button(window, text="Calculate", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()