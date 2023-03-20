#Argumen adalah sebuah nilai inputan fungsi pada saat fungsi itu dipanggil(Variabel)
#Parameter adalah sebutan untuk nilai inputan fungsi pada saat funggsi itu didefinisikan
#cara menggunakan menulis 2 arugmen dalam satu fungsi adalah mengguanakan keyword (=)/ sama dengan
# contoh:
# 
#def guru (nama,pelajaran):
#    print("guru ini bernama",nama)
#    print("guru ini mengajar",pelajaran)

# guru(nama [=]'angga',pelajaran [=]'Matematika')
# description:
# [=] -> adalah keyword untuk menggunakan 2 argumen dalam 1 function


def siswa (nama):
    print("siswa ini bernama",nama)

siswa('susi')

def guru (nama,pelajaran):
    a = input("enter the name = ")
    print("guru ini bernama",nama)
    print("guru ini mengajar",pelajaran)

guru(nama ='angga',pelajaran='Matematika')

