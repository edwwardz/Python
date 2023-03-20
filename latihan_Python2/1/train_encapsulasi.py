class Hero:

    def __init__ (self,name):
        self.healthPool = [0,100,200,300,400,500]
        self.attPower_pool = [0,10,20,30,40,50]
        self.armor_pool = [0,1,2,3,4,5]
        self.__name = name
        self.__exp = 0
        self.__level = 0
        
    def show_info (self):
        print(" {} \nLevel: {} \nHealth: {} \nAttPower: {} \narmor: {}". format(
            self.__name,
            self.__level,
            self.__health,
            self.__attPower,
            self.__armor
        )
    )

    @property
    def health_pool (self):
        pass

    @property
    def attPower_pool (self):
        pass

    @property
    def armor_pool (self):
        pass

    @property
    def LevelUp (self):
        pass

    @property
    def gainExp (self):
        pass

    @health_pool.setter
    def health_pool (self,input):
        self.__healthPool = input

    @attPower_pool.setter
    def attPower_pool (self,input):
        self.__attPower_pool = input

    @armor_pool.setter
    def armor_pool(self,input):
        self.__armor_pool = input

    @gainExp.setter
    def gainExp(self,input):
        self.__exp += input
        if (self.__exp >= 100):
            self.LevelUp = self.__exp//100
            self.__exp %= 100

    @LevelUp.setter
    def LevelUp(self,input):
        self.__level += input
        self.__health = self.__healthPool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]

class Herointeligance (Hero):
    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,50,100,150,200,250]
        self.attPower_pool = [0,20,40,60,80,100]
        self.armor_pool = [0,0.5,1,1.5,2,2.5]
        self.LevelUp = 1


class HeroStreght (Hero):
    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,200,300,400,500,600]
        self.attPower_pool = [0,20,40,60,80,100]
        self.armor_pool = [0,2,3,4,6,8,10]
        self.LevelUp = 1

Angga = Herointeligance("Angga")
Angga.show_info()
Angga.gainExp = 100
Angga.show_info()







