from tkinter import Button,Label,Frame,Tk
import random

char = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Generator (Frame):
    def __init__ (self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.grid()
        self.initUI()
        self.button()
        
    def initUI (self):
        self.parent.title("Password Generator")
        self.parent.geometry("500x500")

    def button (self):
        Label(self, text="Please pick the lenght of you password").grid(row=0,column=0)
        b1 = Button(self, text="7 Charcter", command=self.click)
        b1.grid(row=1,column=0)
        b2 = Button(self, text="8 Charcter", command=self.click1)
        b2.grid(row=2,column=0)
        b3 = Button(self, text="9 Charcter", command=self.click2)
        b3.grid(row=1,column=1)
        b4 = Button(self, text="10 Charcter", command=self.click3)
        b4.grid(row=2,column=1)

    def click (self):
        password = ""
        for x in range (7):
            password_char = random.choice(char)
            password += password_char
        Label(self, text="This is you Password").grid(row=3, column=0)
        Label(self, text=password).grid(row=4, column=0)
 
    def click1 (self):
        password = ""
        for x in range (8):
            password_char = random.choice(char)
            password += password_char
        Label(self, text="This is you Password").grid(row=3, column=0)
        Label(self, text=password).grid(row=4, column=0)

    def click2 (self):
        password = ""
        for x in range (9):
            password_char = random.choice(char)
            password += password_char
        Label(self, text="This is you Password").grid(row=3, column=0)
        Label(self, text=password).grid(row=4, column=0)

    def click3 (self):
        password = ""
        for x in range (10):
            password_char = random.choice(char)
            password += password_char
        Label(self, text="This is you Password").grid(row=3, column=0)
        Label(self, text=password).grid(row=4, column=0)

if __name__ == '__main__':
    root = Tk()
    Generator(root)
    root.mainloop()

    