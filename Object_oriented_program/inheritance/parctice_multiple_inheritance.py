class Team():
    def setteam (self,team):
        self.team = team
    def Showteam (self):
        print (self.team) 

class Tipe_Hero():
    def settipe (self,tipe):
        self.tipe = tipe

    def showtipe (self):
        print (self.tipe)


class Hero (Team,Tipe_Hero):
    
    def __init__ (self,name,health):
        self.name = name
        self.health = health 

Ucup = Hero("Angga", 200)

Ucup.setteam("Red")
Ucup.settipe("Tank")

Ucup.showtipe()
Ucup.Showteam()
