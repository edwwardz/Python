class Hero ():

    def __init__ (self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        self.__info = "name {} \n\thealth: {}".format(self.name,self.__health)

# Fungsi property() di Python
# Fungsi property() digunakan untuk mengembalikan atribut properti dari suatu objek.
# bisa mengganti variabel public whatever you want but the self.info just can change in the __init__ 
    @property
    def info  (self):
        return "name {} \n\thealth: {}".format(self.name,self.__health)

    @property
    def armor (self):
        pass

    @armor.getter
    def armor (self):
        return self.__armor

    @armor.setter
    def armor (self, input):
        self.__armor = input
    

sniper = Hero("Sniper", 100, 10)

print("Change info")
print (sniper.info)
sniper.name = "angga"
print (sniper.info)

print ('getter and setter to armor')
print("First = " + str(sniper.armor))
sniper.armor = 50
print("second = " + str(sniper.armor))



