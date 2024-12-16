class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.energy = 100
        self.inventory_max_weight = 50
        self.inventory = []
        self.intelligence = 10
        self.dexterity = 15
        self.strength = 5
        # add more atributes as needed

    def calculate_inventory_size(self):
        length = len(self.inventory)
        print(length)

    def add_item(self, item_instance):
        if self.calculate_inventory_size() > self.inventory_max_weight:
            self.inventory.append(item_instance)
        else:
            print("Your inventory is full...")

    def use_item(self, item_instance):
        if item_instance.type == "food":
            self.energy += 50
        elif item_instance.type == "medicine":
            self.health += 50
        elif item_instance.type == "STR Potion":
            self.strength += 25
        elif item_instance.type == "book":
            self.intelligence += 25
        # add more code here

    # add more methods as needed
    def train(self):
        self.dexterity += 10
        self.strength += 15
    
    def attack(self, monster):
        pass # figure out how to do this