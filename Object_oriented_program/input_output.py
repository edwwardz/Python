# belajar input and output

"""
w = write mode / mode menulis dan menghapus file lama / menimpa file lama, jika file tidak ada maka akan dibuat file baru
r = read only / hanya bisa membaca
a = appending mode /menambahkan data di akhir baris
r+ = write and read mode baca dan menimpa"""

# make file text
file = open("data.txt",'w')

file.write("test menulis ii ")
file.write("\nini adalah baris ke dua")
file.write("\nini adalah baris ke tiga")
file.write("\nini adalah baris ke empat")
file.write("\nIni yang ke kelima")


file.close()

# membaca file text
file2 = open("data.txt",'r')
#print(file2.read()) # -> digunakan untuk menetukan berapa jumalh character yang akan ditulis/ cara pertama
print(file2.readline())
print(file2.readline())

file2.close()

# appending mode

file3 = open("data.txt",'a')

file3.write("\nFile ini dibuat menggunakan mode append") # append akan  selalu ditaruh di paling akhir sebuah data

file3.close()

# write and read mode

file4 = open("data.txt",'r+')

file4.write("ini yang menimpa")
print(file4.read())

file4.close


