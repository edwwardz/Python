import tkinter as tk # mengimpor modul tkinter dan menamakannya tk
from tkinter import Label, Text
from tkinter.messagebox import showinfo

class Application(tk.Frame): # membuat class Application sebagai warisan dari class Frame milik tkinter
    def __init__(self, master=None): # ini adalah constructor dari class Frame dan akan dijalankan pertama kali
        tk.Frame.__init__(self, master) # menjalankan contructor
        self.grid() # menampilkan window utama ke screen
        self.createWidgets()
        
        
    def createWidgets(self):
        # first field
        self.field1 = tk.Entry(self,width=20) # membuat field isian bilangan pertama
        self.field1.grid(row=0,column=0) # posisi widget dalam grid
        self.field1.insert(0, "")
        
        Label(root, text='Masukan angka di atas', fg="black", font="Algerian").grid(row=2, column=0)
        
        # ADD button
        self.ADD = tk.Button(self, text="Jalankan") # membuat ADD button
        self.ADD["command"] = self.add_numbers # method yang akan dijalankan jika button di-klik
        self.ADD.grid(row=0,column=1) # posisi widget dalam grid             

    def add_numbers(self): # method untuk menjumlahkan dua angka
        try :
            masukan = self.field1.get() # mengambil angka dari isian pertama
            gudang = []
            penampung = ''
            hasil = 1
            
            for i in range (len(masukan)):
                if masukan[i] == '0' or masukan[i] == '1' or masukan[i] == '2' or masukan[i] == '3' or masukan[i] == '4' or masukan[i] == '5' or masukan[i] == '6' or masukan[i] == '7' or masukan[i] == '8' or masukan[i] == '9'  :
                    penampung += masukan[i]
                else :
                    a = int(penampung)
                    gudang.append(a)
                    gudang.append(masukan[i])
                    penampung = ''
                    
            a = int(penampung)
            gudang.append(a)
                    
            
            i = 0   
            while i < len(gudang) :
                if gudang[i] == '*' :
                    gudang.pop(i)
                    hasil = gudang.pop(i-1)*gudang.pop(i-1)
                    gudang.insert(i-1, hasil)
                    i = 0
                i+=1
            
            i = 0   
            while i < len(gudang) :
                if gudang[i] == '/' :
                    gudang.pop(i)
                    print(gudang[i])
                    hasil = gudang.pop(i-1)/gudang.pop(i-1)
                    gudang.insert(i-1, hasil)
                    i = 0
                print(gudang)
                print(hasil)
                i+=1
            
            i = 0   
            while i < len(gudang) :
                if gudang[i] == '-' :
                    gudang.pop(i)
                    hasil = gudang.pop(i-1)-gudang.pop(i-1)
                    gudang.insert(i-1, hasil)
                    i = 0
                i+=1
            
            i = 0   
            while i < len(gudang) :
                if gudang[i] == '+' :
                    gudang.pop(i)
                    hasil = gudang.pop(i-1)+gudang.pop(i-1)
                    gudang.insert(i-1, hasil)
                    i = 0
                i+=1
            
            hasil = str(gudang.pop())
            hasil = "hasilnya adalah : " + hasil
            showinfo("Hasil", hasil)
        except :
            showinfo("Pesan","Maaf ada yang salah.")

root = tk.Tk()

# modify root window

root.title("Kalkulator string") # title window aplikasi
root.geometry("300x200") # panjang dan tinggi window aplikasi
#root.configure(bg='grey')

app = Application(master=root)
app.mainloop()
