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
        kanvas.create_line(15, 25, 200, 25) #-> 15 = x, 25 = y, 200 = x(panjang garis), 25 = y[y from top, and x from left]
        
        kanvas.pack(fill=BOTH, expand=True)

if __name__ == '__main__':
    root = Tk()
    ex = MembuatGaris(root)
    root.mainloop()