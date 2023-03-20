class Hero:
    def __init__(self,name,health,attPower,armor):
        self.__name = name
        self.__healthBase = health
        self.__attPowerBase = attPower
        self.__armorBase = armor

        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthBase * self.__level
        self.__attPowerMax = self.__attPowerBase * self.__level
        self.__armorMax = self.__armorBase * self.__level

        
        self.__health = self.__healthBase
        
        #self.__info = print("{}: \nHealth {}/{} \nAttack Power: {} \nArmor: {}". 
        #format(self.__name,self.__health, self.__healthMax, self.__attPower, self.__armor))

    @property
    def gainExp (self):
        pass

    @property
    def info (self):
        return "{}: \nHealth {}/{} \nAttack Power: {} \nArmor: {}". format (self.__name,self.__health, self.__healthMax, self.__attPowerMax, self.__armorMax)


    @gainExp.setter
    def gainExp (self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print("You level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthBase * self.__level
            self.__attPowerMax = self.__attPowerBase * self.__level
            self.__armorMax = self.__armorBase * self.__level
        
    def attack (self, enemy):
        self.gainExp = 100
            

Angga = Hero('Angga', 100, 20, 30)
Castellani = Hero("Castellani", 100, 30, 20)
Angga.attack(Castellani)

print(Angga.info)
    