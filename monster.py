import random
class Monster:
    def __init__(self, name, health, min_damage, max_damage, is_boss):
        self.name = name
        self.health = health
        self.min_attackPower = min_damage
        self.max_attackPower = max_damage
        self.is_boss = is_boss
        self.loot = []

    def __str__(self):
        return self.name
    
    def is_defeated(self):
            if self.health <= 0:
                print(f"{self.name} has been defeated!")
                self.health = 0
                self.drop_loot()
            else:
                return self.health
    
    def add_loot(self, item):
        self.loot.append(item)
    
    def drop_loot(self):
        if self.loot:
            print(f"{self.name} has dropped: ")
            for item in self.loot:
                print(item.name)
            input("Press Enter to continue...")
        else:
            print(f"{self.name} did not drop any loot.")
            input("Press Enter to continue")
            return []
    
    def random_damage(self):
        return random.randint(self.min_attackPower, self.max_attackPower)
    
    def attackPlayer(self, player):
        if self.health > 0:
            damage = self.random_damage()
            player.health -= damage
            print(f"{self.name} has attacked {player.name} for {damage} damage!")
        else:
            self.is_defeated()
 
    def combat_take_turn(self, player):
        self.attackPlayer(player)