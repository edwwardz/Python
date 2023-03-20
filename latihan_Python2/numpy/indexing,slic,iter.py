# cara mengambil nilai dalam sebuah array numpy

import numpy as np

a = np.arange(10)**2

print(a)

#mengambil nilai
#print("first elemen for a is ", a[0])
#print("Seventh elemen form a is ", a[6])
#print("Last elemen froom a is ", a[-1])

#slicing
#print('elemen dari 1-6 adalah ', a[1:6]) # [start.end]
#print("elemen dari keempat sampai akhir ", a[3:])
#print("elemen dari awal sampai 5", a[:5])

# iterasi

for i in a:
    print('value =',i)
