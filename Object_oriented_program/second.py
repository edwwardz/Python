class Hero():

    def __init__ (self, name, health, attackpower, defend):
        self.name = name
        self.health = health
        self.attackpower = attackpower
        self.defend = defend

    def attack (self, enemy):
        print(self.name + " Attack ", enemy.name)
        enemy.attacked(self, self.attackpower)

    def attacked (self, enemy, attackpower_enemy):
        in_damage = attackpower_enemy / self.defend
        print("Total attack from " + self.name + " is " + str(in_damage))
        self.health -= in_damage
        print("The rest health from " + enemy.name + " is " + str(self.health))

angga = Hero("Angga", 100, 80, 20)
castellani = Hero ("Castellani", 200, 30, 30)

angga.attack(castellani)