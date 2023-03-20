class Hero:
    
    def __init__ (self,name):
        self.healthPool = [0,100,200,300,400,500]
        self.attPower_pool = [0,10,20,30,40,50]
        self.armor_pool = [0,1,2,3,4,5]
        self.__name = input("Please Enter you name = ")
        self.name = input("\nPlease enter you name bot = ")
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
    @property
    def attack (self):
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
            print("Congrasts you level up")
            Angga.show_info()
            
    @attack.setter
    def attack (self,enemy):
        in_damage = self.__attPower / self.__armor
        print("Total damage = ", in_damage)
        rest_Hp = self.__health - in_damage
        print ("Sisa Hp", self.name, "=", rest_Hp)
        print(self.__name, "Attack", self.name)
        self.gainExp = 100
        
    @LevelUp.setter
    def LevelUp(self,input):
        self.__level += input
        self.__health = self.__healthPool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]

"""class Herointeligance (Hero):
    def __init__(self):
        super().__init__(input)
        self.health_pool = [0,50,100,150,200,250]
        self.attPower_pool = [0,20,40,60,80,100]
        self.armor_pool = [0,0.5,1,1.5,2,2.5]
        self.LevelUp = 1"""


class HeroStreght (Hero):
    def __init__(self):
        super().__init__(input)
        self.health_pool = [0,200,300,400,500,600]
        self.attPower_pool = [0,20,40,60,80,100]
        self.armor_pool = [0,2,3,4,6,8,10]
        self.LevelUp = 1

Angga = HeroStreght()
#Castellani = HeroStreght()
Angga.show_info()
enter = input("\nPlease enter you Command = ")    
if enter == "Status":
    Angga.show_info()
elif enter == "Attack":
    Angga.attack = input
else:
    print("Sorry Not found")




