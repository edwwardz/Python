"""from collections import Counter 
angka = [1,2,3,4,5,1,2,4,1,6,2,8,24,7,3,2,5,6]
hitung = Counter(angka)
print(hitung)
for item in hitung.items():
    print ("angka:",item[0], "muncul:", item[1],"kali")"""

from collections import Counter
angka = [1,1,1,1,2,2,3,3,3,4,4,5,5]
hitung = Counter(angka)
print(hitung)
for item in hitung.items():
    print ("Angka",item[0],"Muncul",item[1],'kali')