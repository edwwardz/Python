# learn __init__
class mahasiswa ():
    
    def __init__(self, input_name):
        self.name = input_name

    def learn (self, condition):
        print (self.name, "want to learn", condition)
    
    def sleep (self, condition):
        print (self.name, "Want to sleep", condition)

angga = mahasiswa("Edward Anugrah Angga")

print (angga.name)

"""castel = mahasiswa("Maria castellani")
castel.sleep = 

angga.learn("Math")
castel.learn("Very impulisif")"""

