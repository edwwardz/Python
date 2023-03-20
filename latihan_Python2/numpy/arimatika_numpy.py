import numpy as np

a = [1,2,3,4,5]
b = [6,7,8,9,10]

anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

#ELEMENWISE operation 

# penjumlahan 
#hasil = a+b # ketika list python biasa dijumlahkan akan bergabung di belakangnya 
hasil = anp+bnp # ketika array numpy yang dijumlahkan dia akan dijumalhankan per angka mislakan 1 + 6 

# pengurangan
#hasil = a-b # list tidak bisa di kurangkan
hasil = anp - bnp

# perkalian 
#hasil = a * b -> list tidak bisa di kali
hasil = anp * bnp

# pembagian 
#hasil = a / b -> tidak bisa
hasil = anp / bnp

#kuadrat 
hasil = anp**2

# multidemensi
c = np.array(([1,2,3], [4,5,6]))
d = np.array(([7,8,9], [-1,-2,-3]))
hasil = c + d


print(hasil)
