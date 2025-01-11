class Monster:
    def __init__(self, name, health, damage, is_boss):
        self.name = name
        self.health = health
        self.attackPower = damage
        self.is_boss = is_boss

    def __str__(self):
        return self.name
    
    def is_defeated(self):
            if self.health <= 0:
                print(f"{self.name} has been defeated!")
                self.health = 0
            else:
                return self.health
    
    def attackPlayer(self, player):
        if self.health > 0:
            player.health -= self.attackPower
            print(f"{self.name} has attacked {player.name} for {self.damage} damage!")
        else:
            self.is_defeated()

    
    def combat_take_turn(self, player):
        self.attackPlayer