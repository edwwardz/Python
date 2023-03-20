class Hero:

    def __init__ (self,name):
        self.__health_pool = [100,200,300,400,500]
        self.__attPower_pool = [10,20,30,40,50]
        self.__armor_pool = [2,4,6,8,10]
        self.name = name
        self.__level = 1
        self.__exp = 0

        self.__health_max = self.__health_pool * self.__level
        self.__attPower = self.__attPower_pool * self.__level
        self.__armor = self.__armor_pool * self.__level

        self.__health = self.__health_pool

        @property
        def info (self):
            print("{} Status: \nHealth: {}/{} \nAttack: {} \nArmor: {}".format(
                self.name,
                self.__health,
                self.__health_max,
                self.__attPower_pool,
                self.__armor_pool 
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
        def gainExp (self):
            pass

        @property
        def levelUp (self):
            pass

        @health_pool.setter
        def health_pool(self,input):
            self.__health_pool = input

        @attPower_pool.setter
        def attPower_pool (self,input):
            self.__attPower_pool = input

        @armor_pool.setter
        def armor_pool(self,input):
            self.__armor_pool = input

        @gainExp.setter
        def gainExp (self, addExp):
            self.__exp += 100
            if (self.__exp >= 100):
                print("You Level Up")
                self.LevelUp = self.__exp//100
                self.__exp &= 100
            
        @levelUp.setter
        def levelUp (self,input):
            self.__level += input