from tkinter import Tk, Frame, Menu

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.window = parent
        self.initUI()
        self.membuatMenu()

    def initUI(self):
        self.window.title("Membuat menu bar")
        self.window.geometry("250x150")

    def membuatMenu(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.perintahKeluar)
        menubar.add_cascade(label="File", menu=fileMenu)

    def perintahKeluar(self):
        self.quit()

if __name__ == '__main__':
    root = Tk()
    app = Example(root)
    root.mainloop()

"""Description:
from tkinter import Tk, Frame, Menu  //code ini digunakan untuk mengimport “Tk”, “Frame” dan “Menu” dari tkinter.

class Example(Frame):  //code ini merupakan sebuah class dengan nama “Example” yang di buat untuk menampung semua code program untuk membuat window dan menu bar nya.
    def __init__(self, parent):  //code ini merupakan sebuah construktor yang akan di jalankan pertamakali dan secara otomatis saat class “Example” ini di panggil nantinya.
        Frame.__init__(self, parent)  //code ini digunakan untuk menjadikan class ini sebagai sebuah GUI.

        self.window = parent  //code ini digunakan untuk menguper nilai dari parent ke window.
        self.initUI()  //code ini digunakan untuk memanggil metode dengan nama “initUI”
        self.membuatMenu()  //code ini digunakan untuk memanggil metode dengan nama “membuatMenu”

    def initUI(self):  //code ini digunakan untuk membuat metode dengan nama “initUI” yang akan di isi code program untuk membuat elemen - elemen window nya.
        self.window.title("Membuat menu bar")  //code ni diugnakan untuk mengubah judul window nya.
        self.window.geometry("250x150")  //code ini digunakan untuk mengubah ukuran window nya.

    def membuatMenu(self):  //code ini digunakan untuk membuat  sebuah metode dengan nama “membuatMenu” yang akan di gunakan untuk menampung semua code program untuk membuat menu bar nya.
        menubar = Menu(self.window)  //code ini digunakan untuk memanggil sebuah menu bara dari library tkinter.
        self.window.config(menu=menubar)  //code ini digunakan untuk mengkonfigurasikan menubar dan window nya.

        fileMenu = Menu(menubar)  //coode ini digunakan untuk menjadi kan menubar tadi menjadi sebuah menu.
        fileMenu.add_command(label="Exit", command=self.perintahKeluar)  //code ini digunakan untuk menambahkan sebuah perintah.
        menubar.add_cascade(label="File", menu=fileMenu)  //code ini digunakan untuk memasukkan sebuah menu tadi ke dalam window dengan nama “file”.

    def perintahKeluar(self):  //code ini digunakan untuk membuat metode dengan nama “perintahKeluar” yang akan menampung code program perintah exit.
        self.quit()  //digunaka untuk meng close atau menutup windwo yang di tampilkan.

if __name__ == '__main__':  //code ini digunakan untuk memastikan apakah file nya di jalankan atau tidak.
    root = Tk()  //code ini digunakan untuk memanggil “Tk” dengan menampungnya ke dalam variabel “root”.
    app = Example(root)  //code ini digunakan untuk memanggil class “example” yang sudah kita buat tadi. Dengan memasukkan root sebagai parameter.

    root.mainloop()  //code ini digunakan agar window kita tidak langsung close secara otomatis saat kita panggil nantinya

"""