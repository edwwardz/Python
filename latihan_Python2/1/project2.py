class Hero:
    def __init__ (self,name):
        self.__health_pool = [0,100,200,300,400,500]
        self.__attPower_pool = [0,10,20,30,40,50]
        self.__armor_pool = [0,2,4,6,8,10]
        self.__name = input("Plese enter yo name = ")
        self.name = input("Please enter you Bot name = ")
        
        self.__level = 0
        self.__exp = 0

    def showinfo (self):
        print("{} \nLevel: {} \nhealth: {} \nAttPower: {} \nArmor: {}".format(
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
        self.__health_pool = input

    @attPower_pool.setter
    def attPower_pool (self,input):
        self.__attPower_pool = input

    @armor_pool.setter
    def armor_pool (self,input):
        self.__armor_pool = input
    
    @gainExp.setter
    def gainExp (self,input):
        self.__exp += input
        if (self.__exp >= 100):
            self.__level = self.__exp//100
            self.__exp %= 100

    @LevelUp.setter
    def LevelUp (self,input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]
        
class HeroStrenght (Hero):
    def __init__ (self):
        super().__init__(input)
        self.health_pool = [0,200,300,400,500,600]
        self.attPower_pool = [20,40,60,80,100]
        self.armor_pool = [2,4,6,8,10]
        self.LevelUp = 1

Angga = HeroStrenght()
Angga.showinfo()





















