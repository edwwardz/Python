# fungsi yang menggunakan 2 argumen(1)
# kalo mau membuat fungsi dengan 2 argumen atau lebih gunakan = pada argumen 
# def persegi(x=3,y=4):
    # total = x * y
    # print ("jadi total dari",x,'*',y,"sama dengan",total)
    # return totals
# a = persegi()
# print (a)
# biarpun argumen telah ditulis jumlahnya tapi tetap panggil fungction menggunakan "nama fungction()"


def sekolah(nama,alamat):
    print("nama sekolah ku adalah = ",nama)
    print("alamat sekolah ku adalah = ",alamat)
# (2)
sekolah(nama = 'Sekolah indah', alamat = 'jl halim perdana kusuma')  #<-----------#cara pertama untuk menggunakan 
sekolah("sekolah indah", "Jl halim perdana kusuma")# cara yang kedua             #2 argumen dalam 1 function
# untuk menggunakan cara yang kedua tidak boleh terbalik 
# sekolah("Jl halim perdana kusuma","sekolah indah")# cara yang salah
print('\n')





# fungction yang menggunakan default
def security(shift='malam',nama='rudi',sifat='baik'): # cara 3 mengunakan 2 argumen dalam 2 function
    print("security ini bernama",nama)
    print("security ini mempunyai shift",shift)
    print("Sifat Pak",nama,"adalah", sifat)
security() # karena sudah ada semua jadi dikosongkan
print('\n')






# cara yang kedua
def security(nama,shift='siang',sifat='baik'): # walupun nama di dalam argumen rudi tapi dipanggil oleh fungsi yaitu
    print("security ini bernama",nama)                # Budi jadi tidak mengikuti default
    print("security ini mempunyai shift",shift)
    print("Sifat Pak",nama,"adalah", sifat)
security(shift='malam',nama='Budi') # karena sifat tidak ditulis functionnya jadi default dan menggikuti sifat di atas
print('\n')
security(nama='dadang', sifat='galak') # karena shift tidak ditulis functionnya jadi default dan menggikuti shift di atas
#security(shift='malam', sifat='galak') # karena di function atas tidak ada nama, jadinya nama tidak bisa dipanggil
                                       # dan argumen menjadi missing 1 dan terjadi error

