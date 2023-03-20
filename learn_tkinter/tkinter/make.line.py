from tkinter import Tk, Canvas, Frame, BOTH

class MembuatGaris(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.window = parent
        self.initUI()

    def initUI(self):
        self.window.title("Lines")
        self.pack(fill=BOTH, expand=1)
        self.window.geometry("400x250")

        self.buatGaris()
   
    def buatGaris(self):
        kanvas = Canvas(self)
        kanvas.create_line(300, 35, 300, 200, dash=(4, 2))

        kanvas.pack(fill=BOTH, expand=1)

if __name__ == '__main__':
    root = Tk()
    ex = MembuatGaris(root)
    root.mainloop()