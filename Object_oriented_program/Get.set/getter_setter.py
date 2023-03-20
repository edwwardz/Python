#Decorator python:
#Property -> merubah sebuah method menjadi variabel
#static method
#class method
#If you use the print don't use @property 
# but if you use return you must use @property
# keuunggulan dari property adalah bisa langsung update variabel public sedangkan kalo tanpa property tidak bisa
# langsung update
# setter digunaakn untuk mengubah sebuah variabel cara menggunakannya @armor.setter()
class Hero ():
    
    def __init__ (self, name, health, armor):
        self.__name = name
        self.__health = health
        self.__armor = armor
        self.__info = 'name {} :\n\thealth : {}'.format(self.__name, self.__health)
    
    @property
    def info (self):
        return self.__info

sniper = Hero("angga", 100, 10)
info = "angga"
print (sniper.info)
print (sniper.__dict__)
    