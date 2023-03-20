# return adalah mengambil fungsi dengan perhitungan dan mengunakannya lebih lanjut(fuction tidak meberikan nilai apapun)
# return meberikan nilai bailk (fungction yang memberikan nilai balik)
# return adalah statemen yang berfungsi untuk mengeluarkan (mengembalikan, mengoutputkan) 
# nilai dari sebuah fungsi yang dimana nilai yang sudah dihasilkan tadi akan diproses oleh bagian lain daripada program.
print ('-'*100) # buat pembatas

# fungsi dengan return value
def kuadrat (argumen):
    total = argumen**2 # (**) -> sama dengan pangkat
    print ('nilai kuadrat dari', argumen, 'adalah', total)
    return total # mengeluarkan hasilnya

print(kuadrat(3))


# print(kuadrat(3)) #simple
# print(kuadrat(4)) # medium


# print('_'*100)#membuat pembatas +(100)

# # dungsi dengan return value multiplr argumen
# def tambah(argumen1, argumen2):
#     total = argumen1 + argumen2
#     print(argumen1,'+', argumen2,'=',total)
#     return total 
# a = tambah(3,4)
# print(a)