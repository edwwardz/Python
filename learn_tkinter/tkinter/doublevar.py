from tkinter.ttk import Label, Scale
from tkinter import Tk, LEFT, DoubleVar


root = Tk()

def onScale(nilai):
    v = float(nilai)
    angka.set(v)

scale = Scale(from_=0, to=100, command=onScale)
scale.pack(side=LEFT, padx=15)

angka = DoubleVar()
teks = Label(textvariable=angka)
teks.pack(side=LEFT)

root.geometry("300x50")
root.mainloop()