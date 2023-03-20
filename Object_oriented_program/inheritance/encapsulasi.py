# encapsulasi adalah: 
# buat semua variabel private 
# untuk menggambil semua data yang dibutuhkan menggunakan gatter dan setter
# getter untuk mengambil variabel -> tidak bisa dirubah
# setter untuk menseting variabel -> bisa disetiing

class Hero ():
    def __init__ (self, name, health, attackpower):
        self.__name = name
        self.__health = health
        self.__attPower = attackpower

    # gatter
    def getName (self):
        return ("The name of hero is = " + self.__name)
    
    def getHealth (self):
        return ("The health hero is = " + str(self.__health))
    
    def getAttpower (self):
        return ("The attack power of hero is = " + str(self.__attPower))
    
    # setter 

    def attacked (self,powerattack):
        self.__health -= powerattack

    def setAttPower (self, new_score):
        self.__attPower = new_score


# start
earthShaker = Hero("Angga", 50, 5)

print(earthShaker.__dict__)

# running
print (earthShaker.getName())
print (earthShaker.getHealth())
print (earthShaker.getAttpower())
earthShaker.attacked(40)
print (earthShaker.getHealth())


