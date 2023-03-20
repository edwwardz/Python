from tkinter.constants import X, Y
from tkinter.ttk import Frame, Label, Scale
from tkinter import Tk, BOTH, IntVar, LEFT

class pembuatanScale(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.window = parent

        self.initUI()
        self.membuatScale()
        self.membuatTeks()

    def initUI(self):
        self.window.title("Scale")
        self.window.geometry("250x100")

        self.pack(fill=X, expand=1)

    def membuatScale(self):
        scale = Scale(self, from_=0, to=100, command=self.onScale)
        scale.pack(side=LEFT, padx=15)

    def membuatTeks(self):
        self.angka = IntVar()
        self.teks = Label(self, text=0, textvariable=self.angka)
        self.teks.pack(side=LEFT)

    def onScale(self, nilai):
        v = int(float(nilai))
        self.angka.set(v)

if __name__ == '__main__':
    root = Tk()
    ex = pembuatanScale(root)
    root.mainloop()