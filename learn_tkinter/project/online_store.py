from tkinter import *
trolilist = []

class Store (Frame):
    def __init__ (self, parent):
        self.parent = parent
        self.initUI()

    def initUI (self):
        self.parent.title("Online Store")
        self.parent.geometry("500x500")
        #self.pack(fill=BOTH, expand=1)
        
        self.chose()
    
    def chose (self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu1 = Menu(menubar)
        
        subMenu = Menu(fileMenu)
        subMenu.add_command(label="Sprite -> Rp.5.000", command=self.drink1)
        subMenu.add_command(label="Coca Cola -> Rp.6.500", command=self.drink2)
        subMenu.add_command(label="Fanta -> Rp.7.000", command=self.drink3)
        fileMenu.add_cascade(label='Drink', menu=subMenu, underline=1)

        fileMenu.add_separator()

        subMenu1 = Menu(fileMenu)
        fileMenu.add_cascade(label="Food", menu=subMenu1, underline=0)
        subMenu1.add_command(label="French fries -> Rp.7.000")
        subMenu1.add_command(label="Fried chicken -> Rp.10.000")
        subMenu1.add_command(label="Bread -> Rp.5.000")
        menubar.add_cascade(label='Shop', menu=fileMenu)
        
        menubar.add_cascade(label='Troli', menu=fileMenu1)
        fileMenu1.add_command(label="You Spand", command=self.spand)

    
    def drink1 (self):
        Lab1 = Label(root, text="You want to buy sprite at the price Rp.5.000 Y/N?")
        Lab1.place(x=5, y=10)
        but1 = Button(root, text="Yes", command=self.troli).place(x=5, y=30)
        but2 = Button(root, text="NO", command=root.destroy).place(x=35, y=30)

    def drink2 (self):
        Lab1 = Label(root, text="You want to buy coca cola at the price Rp.6.500 Y/N?")
        Lab1.place(x=5, y=10)
        but1 = Button(root, text="Yes", command=self.troli1).place(x=5, y=30)
        but2 = Button(root, text="NO", command=root.destroy).place(x=35, y=30)

    def drink3 (self):
        Lab1 = Label(root, text="You want to buy Fanta at the price Rp.7.000 Y/N?")
        Lab1.place(x=5, y=10)
        but1 = Button(root, text="Yes", command=self.troli2).place(x=5, y=30)
        but2 = Button(root, text="NO", command=root.destroy).place(x=35, y=30)

    
    def troli (self):
        a = "Sprite -> Rp.5.000"
        Label(root, text="Succes To enter troli").place(x=5, y=55)
        trolilist.append(a)
    
    def troli1 (self):
        b = "Coca cola -> Rp.6.500"
        Label(root, text="Succes To enter troli").place(x=5, y=55)
        trolilist.append(b)
    
    def troli2 (self):
        c = "Fanta -> Rp.7.000"
        Label(root, text="Succes To enter troli").place(x=5, y=55)
        trolilist.append(c)
    

    def spand (self):
        Label(root, text="This is you Drink:").place(x=150, y=55)
        Label(root, text=trolilist).place(x=150, y=75)
        
if __name__ == '__main__':
    root = Tk()
    Store(root)
    root.mainloop()
