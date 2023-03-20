# inheritance adalah turunan jadi semua data dalam class satu bisa diambil dengan inheritance
# untuk menggunakan inheritance cukup buat class baru. Example 
# class newclass (masukan nama class yang mau di inheritance/dibuat turunan)
""""kita juga bisa mengoveride sebuah class dengan turunan 
 kita cukup buat fungction yang sama seperti pada class lama dan print. Example
 def cek_id_abang(self):
    print ("Bisa dimasukan apa saja")"""
    

class Ojek:
    def __init__(self, name, transmisi, daerah): 
        self.name = name
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_abang(self):
        print('nama',self.name, '\nmotor:', self.transmisi, '\ndaerah:', self.daerah)

    
class Gojek(Ojek):
    
    def cek_id_abang(self):
        print("Cek aplikasi aja")

ojek1 = Ojek('mario', 'manual', 'bandung')
ojek2 = Gojek('oni', 'matic', 'jakarta')

(ojek1.cek_id_abang())
print('\n')
(ojek2.cek_id_abang())

# DRY -> aturan programing 
# don't repeat yourself
