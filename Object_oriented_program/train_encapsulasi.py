class Hero :

    # private class variabel
    __jumlah = 0


    def __init__ (self, name, health, attpower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attpower
        self.__armorStandar = armor 
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level # -> ini yang level max
        self.__attPower = self.__attPowerStandar * self.__level # 
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthStandar

        Hero.__jumlah += 1

    @property
    def info (self):
        return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)

    @property
    def gainExp (self):
        pass

    @gainExp.setter
    def gainExp (self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level # -> ini yang level max
            self.__attPower = self.__attPowerStandar * self.__level # 
            self.__armor = self.__armorStandar * self.__level

    def attack (self,enemy):
        self.gainExp = 100

slardar = Hero('Angga', 100, 5, 10)
axe = Hero('axe', 100, 5,10)
print(slardar.info)

slardar.attack(axe)
print(slardar.info)















