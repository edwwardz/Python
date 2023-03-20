class school():

    def __init__(self, name, kelas):
        self.name = name
        self.kelas = kelas
    
    def belajar (self, learn):
        self.learn = learn

    def apa (self):
        if self.learn == "matematika" or self.learn == 'pkn':
            print ("Now you just learn")
        else:
            print("You not learn") 

angga = school("Angga", 97)

angga.belajar(input("Enter you lesson = "))

angga.apa()


