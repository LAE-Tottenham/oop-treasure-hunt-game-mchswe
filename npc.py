class NPC:
    def __init__(self, name, items):
        self.name = name
        self.bond_lvl = 0
        self.items = items
    
    def __str__(self):
        return self.name
    
    def increase_bond(self):
        self.bond_lvl += 1
        print(f"Bond Level is now {self.bond_lvl}")