# perbedaan str dan repr adalah str digunakan ketika program sudah jadi sedangkan repr digunakan saat Debug
# if use magic method __add__ harus memasukan input ke dalam argumen or parameter and magic method add us e to 
# operator arimatika
class Mangga:
    
    # magic method adalah 
    def __init__ (self,name,jumlah):
        self.name = name
        self.jumlah = jumlah

    """def __repr__ (self): #__repr__ kegunaan nya untuk mengembalikan string representasi dari suatu objek
        return "Mangga: {}".format(self.name)"""
    
    def __str__(self):
       return "Mangga: {}".format(self.name)

    def __add__(self, objek):
        return self.jumlah + objek.jumlah




belanja1 = Mangga("Arum maniss", 10)
belanja2 = Mangga("asam", 10)
print(belanja1)
print(belanja2)
print(belanja1+belanja2)