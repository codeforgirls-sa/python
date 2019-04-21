from tkinter import *
from random import choice

greeting = ["hi", "hello"]
response = ["hi", "hello", "Hello too"]
error = ["sorry, i don't know", "what u said?" ]

root = Tk()
user = StringVar()
bot = StringVar()

root.title("My First ChatBot")
Label(root, text=" User: ").pack(side=LEFT)
Entry(root, textvariable=user).pack(side=LEFT)
Label(root, text=" Bot: ").pack(side=LEFT)
Entry(root, textvariable=bot).pack(side=LEFT)

def main():
    question = user.get()
    if question in greeting:
        bot.set(choice(response))
    else:
        bot.set(choice(error))

Button(root, text="speak", command=main).pack(side=LEFT)

mainloop()