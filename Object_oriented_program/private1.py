class Hero ():
    
    # class variabel
    jumlah = 0
    
    def __init__(self, name, health):
        self.name = name 
        self.health = health

        # variabel instance private
        self.__private = "private"
        # variabel instance proctected
        self._proctected = "protected" # -> mirip public tapi hanya ada dalam class dan tidak boleh diubah
    
lina = Hero("Angga", 100) # public,     angka dalam variabel public bisa diganti dengan menuliskan: lina.nama = , lina.health = 

print (lina.__dict__)
print(lina._proctected)
print (lina.__dict__)