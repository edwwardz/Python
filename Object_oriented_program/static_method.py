class Hero ():
     
    __jumlah = 0

    def __init__ (self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method encapsulasi hanya berlaku untuk object dan tidak bisa untuk class variabel
    """
    def getJumlah (self):
        return Hero.__jumlah
        """
    # tidak berlaku untuk objek tapi berlaku untuk class   
    def getJumlah1 ():
        return Hero.__jumlah
    
    # method static (decorator)
    # bisa digunkan untuk objek maupun class
    # tapi static method tidak bisa mengambil argumen example:
    @staticmethod
    def getJumlah2 ():
        return Hero.__jumlah
    
    # same with staticmethod but the difrent is argumen
    # in class method you can get argumen in the fungction. example:
    @classmethod
    def getJumlah3 (cls):
       return cls.__jumlah

sniper = Hero ('Sniper ')
print (Hero.getJumlah2())
rikimaru = Hero('rikimaru')
print (sniper.getJumlah2())
drowranger = Hero('drowranger')
print (drowranger.getJumlah3())


