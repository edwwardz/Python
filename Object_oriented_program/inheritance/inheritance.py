# arti inheritance adalah pewarisan atau sesuatu yang diwariskan 
# contoh class1 wariskan ke kelas yang ke 2, class 1 disebut super class dan class 2 disebut subclass
# 

class Hero:

    def __init__ (self,name,health):
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    pass

class Hero_Speed (Hero):
    pass

lina = Hero ('lina', 100)
angga = Hero_intelligent("angga", 200)
castel = Hero_Speed("Castellani", 100)

print (lina.name)
print (angga.name)
print (castel.name)









