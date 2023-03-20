# lambda digunakan untuk membuat fungsi dalam satu baris ekspresi. Lambda bisa memiliki lebih dari satu argumen 
# atau parameter, tapi hanya bisa memiliki satu ekspresi atau isi. Karena fungsi lambda tidak punya nama, 
# jadi kita butuh variabel untuk menyimpannya

def jumlah(a,b):
    c =a+b
    return c
hasil = jumlah(4,5)
print(hasil)



# membuat anonymus dangan lamda
kali = lambda x,y: x*y
print(kali(2,5)) # cara 1
hasil = kali(3,4) # contoh 2
print (hasil)

