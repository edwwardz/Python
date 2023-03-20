# untuk mengurutkan button/yg lain menggunkan value
from tkinter import *
root = Tk()
root.geometry("200x100")

v = IntVar()
v.set(2)


def ShowChoice():
    print (v.get())

Radiobutton(root,
                text="Pilihan 1",
                variable=v,
                command=ShowChoice,
                value=1).pack()

Radiobutton(root,
                text="Pilihan 2",
                variable=v,
                command=ShowChoice,
                value=5).pack()

mainloop()
