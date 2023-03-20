from tkinter import Tk, Frame, Menu, Button, LEFT, TOP, X, FLAT, RAISED

class membuatToolbar(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.window = parent

        self.initUI()

    def initUI(self):
        self.window.title("Toolbar")
        self.window.geometry("250x150")

        self.buatToolBar()
        self.konfigurasiToolbardanMenuBar()

    def buatToolBar(self):
        self.toolbar = Frame(self.window, bd=1, relief=RAISED)
        exitButton = Button(self.toolbar, text="exit", relief=FLAT,command=self.quit)
        exitButton.pack(side=LEFT, padx=2, pady=2)

    def konfigurasiToolbardanMenuBar(self):
        self.toolbar.pack(side=TOP, fill=X)
        self.pack()

if __name__ == '__main__':
    root = Tk()
    app = membuatToolbar(root)
    root.mainloop()