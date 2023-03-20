class Hero():

    __jumlah = 0

    def __init__(self, health, attPower, armor):
        #self.name = name
        self.__healthbase = health
        self.__attPower = attPower
        self.__armorbase = armor
        #self.__role = role

        self.level = 1
        self.exp = 0

        self.__healthMax = self.__healthbase * self.level
        self.__armorMax = self.__armorbase * self.level
        self.__attPowerMax = self.__attPower * self.level
        self.__info = "health: {}/{} \nAttack:{}/{} \nArmor: {}/{}".format(self.__healthbase, 
        self.__healthMax,self.__attPower, self.__attPowerMax, self.__armorbase, self.__armorMax)

        Hero.__jumlah += 1

    def info (self):
        print (self.level)

    #@property
    #def role (self):
    #    pass

    #@role.getter
    def role (self):
        print ("Hello welcome to the Role select")
        print ("Please select you Role")
        print ("1. Archer\n2. Fighter\n3. Assasin\n4. Tank")
        role1 = input("Please enter you name role = ")
        if role1 == 'Archer':
            name1 = input("Okay please enter you name charater = ")
            print ("okay now you name is ", name1)
            print ("hello", name1)            
        else:
            print("not found \nPlease try again")
            
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp (self, addExp):
        self.exp += addExp
        if self.exp >= 100:
            print("congrats you level up")
            print("You atribute level up")
            self.level += 1
            self.exp -= 100
            a = input("Please enter info to check you status = ")
            if a == 'info':
                print (self.__info)
            
            self.__healthMax = self.__healthbase * self.level
            self.__armorMax = self.__armorbase * self.level
            self.__attPowerMax = self.__attPower * self.level
            self.__info = "health: {}/{} \nAttack:{}/{} \nArmor: {}/{}".format(self.__healthbase, 
            self.__healthMax,self.__attPower, self.__attPowerMax, self.__armorbase, self.__armorMax)

    
    def attack (self):
        self.gainExp = 100


sniper = Hero(100, 20, 30,)
angga = Hero(100,10,20)
sniper.gainExp = 100
sniper.info() 

#print(sniper.total_hero)    

        
            