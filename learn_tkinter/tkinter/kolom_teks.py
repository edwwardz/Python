from tkinter import *

class Kolomteks ():
    def __init__ (self):
        
        self.kolomteks()
        self.scrollbar()

    def kolomteks (self):
        self.T = Text(width=30, height=5)
        self.T.pack()
        self.T.insert(END, "Angga\n\n\nn\n\n\\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAngga")

    def scrollbar (self):
        s = Scrollbar()
        s.pack(fill=Y, side=RIGHT)
        self.T.pack(fill=Y, side=LEFT)
        s.config(command=self.T.yview)
        self.T.config(yscrollcommand=s.set)

root = Tk()
root.geometry("350x150")
Kolomteks()
root.mainloop()
