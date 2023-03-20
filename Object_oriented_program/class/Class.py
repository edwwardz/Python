# Class adalah salah satu cara bagaimana kita membuat sebuah kode yang mempunyai behaviour tertentu dan 
# lebih mudah dalam mengorganisasi berbagai fungsi dasebuah state tanpa harus membuat n state-nya. Dalam 
# sebuah class kamu dapat menyimpan banyak state bila tidak menggunakan class

class mahasiswa (): # Make class
    tgl_lahir = 'Date born'  """Disebut atribut/nilai yang menempel pada class,   (pass -> to make the class empty, 
                                nama(variabel/dll) can use to menulis nama dll)"""
    def belajar (self):
        print ("saya belajar")

angga = mahasiswa() # angga->instenses
castellani = mahasiswa() # mahasiswa->class

angga.tgl_lahir = "25 Juli 2006" # 
castellani.tgl_lahir = "10 November 2014"

print (angga.tgl_lahir)
print (castellani.tgl_lahir)

