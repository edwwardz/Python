from tkinter import Tk,Checkbutton,Frame,BOTH

class Example(Frame):
    def __init__ (self,parent):
        Frame.__init__(self,parent)
        self.parent = parent

        self.initUI()
        self.CheckButton()

    def initUI (self):
        self.parent.title("Check")
        self.pack(fill=BOTH, expand=True)
        self.parent.geometry("250x100")

    def CheckButton (self):
        cb = Checkbutton(self, text="This is first")
        cb.place(x=50, y=10)

        cb = Checkbutton(self, text="This is second")
        cb.place(x=50, y=30)

        cb = Checkbutton(self, text='Check Button')
        cb.place(x=50, y=50)

if __name__ == '__main__':
    root = Tk()
    app = Example(root)
    root.mainloop()

"""x = jarak spasi
y = jarak colomn"""
