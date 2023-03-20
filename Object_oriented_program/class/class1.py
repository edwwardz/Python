# method adalah fungction (def) yang menempel pada class
# but if the fungction not in the class the name just fungction

class family():
    name = 'name'
    tgl_lahir = 'tgl_lahir'

angga = family()
reni = family()
budi = family()
castellani = family()

angga.tgl_lahir = "25-07-06"
angga.name = "Edward Anugrah Angga"
reni.name = "Adolvina reni palobo"
budi.name = 'Vitobudibratta'
castellani.name = "maria castellani emerald"

print(angga.name, '-> tanggal lahir' , angga.tgl_lahir) # untuk menggabungkan 2 class
print(reni.name)
print(budi.name)
print(castellani.name)
