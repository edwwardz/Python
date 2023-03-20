# Boolean var = perentara untuk menentukan True atau false
from tkinter import *

root = Tk()

def diKlik():
    if penentu.get() == True:
        root.title("lihat disini..")
    else:
        root.title("")

root.geometry("250x150")
penentu = BooleanVar()

checkBox = Checkbutton(text="judul", variable=penentu, command=diKlik)
checkBox.place(x=50, y=50)

root.mainloop()