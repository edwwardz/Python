# learn super

class Hero ():
    def __init__ (self, name, health, ):
        self.name = name
        self.health = health
        
    def show_info(self):
        print("{} With health {}".format(self.name,self.health))


class Hero_inteligance (Hero):
    def __init__ (self, name):
        # Hero.__init__(self,name,100) # First 
        super().__init__(name, 100) # second
        super().show_info()
        
class Hero_strenght (Hero):
    def __init__ (self, name):
        super().__init__(name, 100)
        super().show_info()
        

lina = Hero_inteligance("angga")
axe = Hero_strenght("castell")

