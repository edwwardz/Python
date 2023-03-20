from tkinter import *

class RadioButton (Frame):
    def __init__ (self, parent):
        Frame.__init__(self,parent)
        self.window = parent
        self.v = IntVar()
    
        self.teks()
        self.radioButton()

    def teks (self):
        Label(root, text="Please pick you language", justify=LEFT, padx=20).pack()

    def radioButton (self):
        Radiobutton(root, text="Indonesia", padx=20, variable=self.v, command=self.tampilkan, value=1).pack(anchor=W)
        Radiobutton(root, text="English", padx=20, variable=self.v, command=self.tampilkan, value=2).pack(anchor=W)
        
    def tampilkan (self):
        if self.v.get() == 1:
            print("Indonesia")
        elif self.v.get() == 2:
            print("English")
        
if __name__ == '__main__':
    root = Tk()
    RadioButton(root)
    mainloop()
    