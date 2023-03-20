"""(Jadi fungsi dari “self” ini sebenarnya adalah sebagai sebuah variabel saja yang yang menyatakan kelas itu sendiri. ... 
Untuk memanggil sebuah variabel dan sebuah metode yang ada pada dirinya sendiri haruslah di awali dengan kata “self”)"""

class mahasiswa (): # <- Make class
    
    jurusan = "Komputer"
    __nilai = 0 # private tambahkan (__) double underscore 

    def __init__ (var, input_name, input_nim):
        var.name = input_name # public
        var.nim = input_nim # public

    def uts (var, input_nilai):
        var.__nilai += input_nilai
        
    def uas (var, input_nilai):
        var.__nilai += input_nilai

    def check_status (var):
        if var.__nilai <= 50:
            print (var.name,"tidak lulus")
        else:
            print (var.name, "kamu lulus")

angga = mahasiswa("Edward Anugrah Angga", 250706) # angga-> instenses
castellani = mahasiswa("Maria castellani", 101114)

angga.uts(20)
angga.uas(30)

angga.check_status()