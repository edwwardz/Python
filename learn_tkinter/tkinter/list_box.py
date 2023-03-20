from tkinter.ttk import Frame, Label
from tkinter import Tk, BOTH, Listbox, StringVar, END


class membuatListbox(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.window = parent

        self.initUI()
        self.buatListbox()

    def initUI(self):
        self.window.title("Listbox")
        self.window.geometry("300x250")
        self.pack(fill=BOTH, expand=1)
    
    def buatListbox(self):
        daftarNama = ['Moham', 'Moh. nikmat',
                'nama ke 3', 'nama ke 4', 'Dan seterusnya..']

        listBox = Listbox(self)
        for i in daftarNama:
            listBox.insert(END, i)
    
    
        listBox.bind("<<ListboxSelect>>", self.onSelect)

        listBox.pack(pady=15)

        self.nilai = StringVar()
        self.teks = Label(self, text=0, textvariable=self.nilai)
        self.teks.pack()

    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        nilaiPerubahan = sender.get(idx)

        self.nilai.set(nilaiPerubahan)

if __name__ == '__main__':
    root = Tk()
    ex = membuatListbox(root)
    root.mainloop()