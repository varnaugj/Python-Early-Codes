
from tkinter import *
import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Test 123")
greeting.pack()

def returnEntry(arg=None):

    name = myEntry.get()
    resultLabel.config(text= name)
    myEntry.delete(0,END)

myEntry = tk.Entry(width=20)
myEntry.focus()
myEntry.bind("<Return>", returnEntry)
myEntry.pack()

button = tk.Button(text="Yeet me!", command=returnEntry, width=25, height=5)
button.pack(fill=X)

resultLabel = tk.Label(text="")
resultLabel.pack(fill=X)

window.mainloop()

#val = input("Enter Text here: ")
#print(val)  

#entry = tk.Entry(fg="black",bg="white", width=50)
#entry.pack()


