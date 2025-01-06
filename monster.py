class Monster:
    def __init__(self, name, health, damage, is_boss):
        self.name = name
        self.health = health
        self.attackPower = damage
        self.is_boss = is_boss

    def attackPlayer(self, player):
        player.health -= self.attackPower
        print(f"{self.name} has attacked {player.name} for {self.damage} damage!")

    def is_defeated(self):
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            self.health = 0
        else:
            return self.health