class mahasiswa ():
    
    jumlah_mahasiswa = 0

    def __init__(self, input_name):
        self.name = input_name
        
        mahasiswa.jumlah_mahasiswa += 1

angga = mahasiswa("Edward Anugrah Angga")
castel = mahasiswa("Maria castellani")

print ("sekarang jumlah mahasiswa adalah", mahasiswa.jumlah_mahasiswa)


# class variabel adalah variabel yang dimiliki class 
# segala sesuatu yang ada self adalah milik instenses
# dictionary (__dict__) adalah mengambil semua data yang dimiliki sebuah variabel contohnya:
# print (nama_variabel.__dict__) dia akan mencari semua informasi tentang nama variabel di dalam file tersebut 
# bisa itu nama, bisa itu kelas, bisa itu tanggal lahir