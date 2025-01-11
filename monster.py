class Monster:
    def __init__(self, name, health, damage, is_boss):
        self.name = name
        self.health = health
        self.attackPower = damage
        self.is_boss = is_boss
        self.loot = []

    def __str__(self):
        return self.name
    
    # def __repr__(self):
    #     return f"Monster(name={self.name}, health={self.health}, attackPower={self.attackPower}, is_boss={self.is_boss})"
    
    def is_defeated(self):
            if self.health <= 0:
                print(f"{self.name} has been defeated!")
                self.health = 0
                self.drop_loot()
            else:
                return self.health
    
    def drop_loot(self):
        if self.loot:
            print(f"{self.name} has dropped {self.loot}")
        else:
            print(f"{self.name} did not drop any loot.")
    
    def attackPlayer(self, player):
        if self.health > 0:
            player.health -= self.attackPower
            print(f"{self.name} has attacked {player.name} for {self.damage} damage!")
        else:
            self.is_defeated()
 
    def combat_take_turn(self, player):
        self.attackPlayer