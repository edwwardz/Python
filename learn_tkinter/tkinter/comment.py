# fill = BOTH = Full screen, Y = Rata tengah, X = Rata Tengah
# pady jarak antar kolom
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, RAISED
from tkinter.constants import W, Y
from tkinter.ttk import Frame, Label, Entry, Button


class membuatKomentar(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.window = parent
        self.initUI()

    def initUI(self):
        self.window.title("komentar")
        self.pack(fill=BOTH,expand=True)

        self.elemen1()
        self.elemen2()
        self.elemen3()
        self.tombol()
               
    def elemen1(self) :
        teksField1 = Frame(self)
        teksField1.pack(fill=X)

        teks1 = Label(teksField1, text="judul :", width=6)
        teks1.pack(side=LEFT, padx=5, pady=5)

        masukkanKeWindow1 = Entry(teksField1)
        masukkanKeWindow1.pack(fill=X, padx=5, expand=True)
     
    def elemen2(self):
        teksField2 = Frame(self)
        teksField2.pack(fill=X)

        teks2 = Label(teksField2, text="jenis :", width=6)
        teks2.pack(side=LEFT, padx=5, pady=5)

        masukkanKeWindow2 = Entry(teksField2)
        masukkanKeWindow2.pack(fill=X, padx=5, expand=True)
 
    def elemen3(self):
        teksField3 = Frame(self)
        teksField3.pack(fill=BOTH, expand=True)

        teks3 = Label(teksField3, text="ulasan:", width=6)
        teks3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        masukkanKeWindow2 = Text(teksField3)
        masukkanKeWindow2.pack(fill=BOTH, pady=5, padx=5, expand=True)
 
    def tombol(self):
        tombolTutup = Button(self, text="Tutup", command=self.quit)
        tombolTutup.pack(side=RIGHT, padx=5, pady=5)
     
        tombolOke = Button(self, text="Oke", command=self.quit)
        tombolOke.pack(side=RIGHT)


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x450")
    app = membuatKomentar(root)
    root.mainloop()