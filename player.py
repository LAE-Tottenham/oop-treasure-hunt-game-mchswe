class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.inventory_max_weight = 100
        self.inventory = []
        self.intelligence = 10
        self.dexterity = 15
        self.strength = 10
        # add more atributes as needed

    def calculate_inventory_size(self):
        amount = len(self.inventory)
        we = sum(item.weight for item in self.inventory)
        print(f"There are {amount} items in your Inventory.")
        print(f"The weight of your inventory is {we}.")
        return we

    def add_item(self, item_instance):
        if self.calculate_inventory_size() + item_instance.weight <= self.inventory_max_weight:
            self.inventory.append(item_instance)
            print(f"You picked up {item_instance.name}!")
        else:
            print("Your inventory is full...")
    
    def remove_item(self, item_instance):
        self.inventory.remove(item_instance)
        print(f"{item_instance.name} has been removed from your inventory.")

    def use_item(self, item_instance):
        if item_instance.type == "food":
            self.energy += 50
        elif item_instance.type == "medicine":
            self.health += 50
        elif item_instance.type == "str potion":
            self.strength += 15
            self.health *= 1.1
        elif item_instance.type == "book":
            self.intelligence += 25
        elif item_instance.type == "axe":
            self.strength *= 1.2
        elif item_instance.type == "sword":
            self.strength *= 1.6
        elif item_instance.type == "h_sword":
            self.strength *= 2.2
        elif item_instance.type == "dagger":
            self.strength *= 1.1
        elif item_instance.type == "elixir":
            self.strength += 10
            self.intelligence += 10
            self.energy += 20
            self.dexterity += 10
            self.health += 75
        else:
            pass

    def train(self):
        self.dexterity += 5
        self.strength += 5
        print(f"{self.name} has trained! Your Strength is now {self.strength}. \n Your Dexterity is now {self.dexterity}.")
    
    def attack(self, monster):
        if monster.health > 0:
            monster.health -= self.strength
            print(f"You attacked {monster.name}! {monster.name} now has {monster.health} HP.")
            if monster.health <= 0:
                print(f"{monster.name} has been defeated!")
                monster_loot = monster.drop_loot()
                for item in monster_loot:
                    self.add_item(item)
        else:
            print(f"{monster.name} has already been defeated.")
    
    def guard(self, monster):
        monster.attackPower *= 0.15
        print(f"You have guarded against {monster.name}!")

    
    def move_to(self, place):
        if place in self.location.next_places:
            self.location = place
            self.location.description()
        else:
            print(f"You can't go there from here.")
    
    def display_stats(self):
        print(f"Player: {self.name} \n Health: {self.health} \n Strength: {self.strength} \n Intelligence: {self.intelligence} \n Dexterity: {self.dexterity} \n Inventory: {self.inventory}")

    def combat_take_turn(self, monster_instance):
        print(f"Your Turn to Attack! \n What will you do?")
        action = input(f" 1. Attack \n 2. Guard \n 3. Use Item")
        if action == "1":
            self.attack(monster_instance)
        elif action == "2":
            self.guard(monster_instance)
        elif action == "3":
            item = input("Which item would you like to use?")
            print(f"{self.inventory}")
            for item in self.inventory:
                if item.name == item:
                    self.use_item(item)
                    break
            else:
                print("Invalid Item or Item not in Inventory.")
        else:
            print("Invalid Action. Try Again.")