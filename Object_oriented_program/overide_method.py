# kalau sebuah method atau fungction ada tanda kurung atau () saat ia dipanggil lagi menggunakan tanda kurung dibelakang
# overidae method adalah menimpa sebuah method

class Hero():
    def __init__ (self,name,health):
        self.name = name
        self.health = health

    def show_info (self):
        print("Ini merupakan show_info Hero")
        print ("{} health: {}". format(self.name, self.health))

class Hero_inteligence (Hero):
    def __init__ (self,name):
        super().__init__(name,100)

    def show_info (self):
        print("ini merupakan show info di hero_inteligance")
        print("\n{} \nTipe: inteligance \nhealth: {}".format(self.name, self.health))

class Hero_strenght (Hero):
    def __init__ (self,name):
        super().__init__(name,200)


lina = Hero_inteligence("angga")
axe = Hero_strenght("Castellani")

lina.show_info()
axe.show_info()






