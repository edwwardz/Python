# vektor adalah array dengan 1 kolom
# matrix adalah array dengan 2 kolom atau lebih

import numpy as np

# membuat matrix dengan tipe data tertentu, (keyword) = dtype
a = np.array(( [1,2,3,4], [5,6,7,8]), dtype= float)

# membuat matrix menggunakan fungction

def  kuadrat (baris,kolom):
    return kolom**2

def jumlah(baris,kolom):
    return(kolom - baris)

b = np.fromfunction(kuadrat, (1,10), dtype= int) # urutan -> kuadrat, ukuran matrix, tipe, (2 = baris, 10 = kolom)
c = np.fromfunction(jumlah, (3,6), dtype= float)

print(c)
