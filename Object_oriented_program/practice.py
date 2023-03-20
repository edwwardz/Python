class Hero():

    def __init__(self, name, health, attackpower, armorNumber):
        self.health = health
        self.name = name
        self.attackpower = attackpower
        self.armorNumber = armorNumber

    def serang (self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackpower)

    def diserang (self, lawan, attackpower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackpower_lawan/self.armorNumber
        print('Serangan masuk = ' + str(attack_diterima))
        self.health -= attack_diterima
        print('Darah ' + self.name + ' tersisa ' + str(self.health))
        

sniper = Hero('sniper', 100,10,5) # health-> 100,   atckpower-> 10,    armorNumber-> 5
rikimaru = Hero('rikamaru', 100,20,10)

sniper.serang(rikimaru)
print('\n') 
rikimaru.serang(sniper)
print('\n') 
rikimaru.serang(sniper)
print('\n') 
rikimaru.serang(sniper)
print('\n') 
rikimaru.serang(sniper)
print('\n') 
rikimaru.serang(sniper)





# Description:
# sniper.serang(rikimaru) = sniper -> self,     serang -> fungction,    rikimaru -> lawan(argumen)
# jadi konsepnya lawan = rikimaru,      diserang(self) -> fungction diserang,       self name self yaitu sniper 
# -= -> adalah operator dikuarangi sama dengan
# sisa_hp = self.health-attack_diterima 
        #print("Sisa Health adalah ", sisa_hp)