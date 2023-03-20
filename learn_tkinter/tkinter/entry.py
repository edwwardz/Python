from tkinter import *

class MakeKolom (Frame):
    def __init__ (self):
        
        self.makeEntry()
        self.makeTeks()
        
    def makeTeks (self):
        Label(text="First Name").grid(row=0)
        Label(text="Last Name").grid(row=1)
    
    def makeEntry (self):
        Entry().grid(row=0,column=1)
        Entry().grid(row=1,column=1)
        
root = Tk()
MakeKolom()
mainloop()
    
"""description:
row = baris
column = colom"""
        
