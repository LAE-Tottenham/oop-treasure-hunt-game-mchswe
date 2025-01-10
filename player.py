class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.energy = 100
        self.inventory_max_weight = 50
        self.inventory = []
        self.intelligence = 10
        self.dexterity = 15
        self.strength = 10
        self.location = None
        # add more atributes as needed

    def calculate_inventory_size(self):
        amount = len(self.inventory)
        we = sum(item.weight for item in self.inventory)
        print(f"There are {amount} items in your Inventory.")
        print(f"The weight of your inventory is {we}.")

    def add_item(self, item_instance):
        if self.calculate_inventory_size() > self.inventory_max_weight:
            self.inventory.append(item_instance)
            print(f"You picked up {item_instance}!")
        else:
            print("Your inventory is full...")

    def use_item(self, item_instance):
        if item_instance.type == "food":
            self.energy += 50
        elif item_instance.type == "medicine":
            self.health += 50
        elif item_instance.type == "str potion":
            self.strength += 15
        elif item_instance.type == "book":
            self.intelligence += 25
        elif item_instance.type == "axe":
            self.strength *= 1.2
        elif item_instance.type == "sword":
            self.strength *= 1.6
        elif item_instance.type == "dagger":
            self.strength *= 1.1
        elif item_instance.type == "elixir":
            self.strength += 10
            self.intelligence += 10
            self.energy += 20
            self.dexterity += 10
            self.health += 75
        
        # add more code here

    # add more methods as needed
    def train(self):
        self.dexterity += 5
        self.strength += 5
    
    def attack(self, monster):
        if monster.health > 0:
            monster.health -= self.strength
            print(f"You attacked {monster.name}! {monster.name} now has {monster.health} HP.")
            if monster.health <= 0:
                print(f"{monster.name} has been defeated!")
        else:
            print(f"{monster.name} has already been defeated.")
    
    def guard(self, monster):
        monster.attackPower *= 0.2
        print(f"You have guarded against {monster.name}!")

    
    def move_to(self, place):
        if place in self.location.next_places:
            self.location = place
            self.location.description()
        else:
            print(f"You can't go there from here.")