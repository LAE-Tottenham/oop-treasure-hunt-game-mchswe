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
            if item_instance.type == "winning_item":
                print("Congratulations on defeating Gesshin. The Land of Ruliar is now safe. You have won.")
                exit()
            if item_instance.type == "secret_item":
                print("Use this item to unock the Secret Ending.")
            else:
                pass
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
            self.strength += 30
            self.intelligence += 10
            self.energy += 20
            self.dexterity += 10
            self.health += 125
        elif item_instance.type == "secret_win":
            print("Congratulations on getting the Secret Ending!")
            exit()
        else:
            pass

    def train(self):
        self.health += 10
        self.dexterity += 2
        self.strength += 5
        print(f"{self.name} has trained! Your Health is now {self.health} Your Strength is now {self.strength}. \n Your Dexterity is now {self.dexterity}.")
    
    def attack(self, monster):
        if monster.health > 0:
            monster.health -= self.strength
            print(f"You attacked {monster.name}! {monster.name} now has {monster.health} HP.")
            if monster.health <= 0:
                print(f"{monster.name} has been defeated!")
                monster_loot = monster.drop_loot()
                if monster_loot is not None:
                    for item in monster_loot:
                        self.add_item(item)
                else:
                    print("No loot was dropped.")
        else:
            print(f"{monster.name} has already been defeated.")
    
    def guard(self, monster):
        damage = monster.random_damage()
        damage *= 0.15
        print(f"You have guarded against {monster.name}!")

    
    def move_to(self, place):
        if place in self.location.next_places:
            self.location = place
            self.location.description()
        else:
            print(f"You can't go there from here.")
    
    def display_stats(self):
        print(f"Player: {self.name} \nHealth: {self.health} \nStrength: {self.strength} \nIntelligence: {self.intelligence} \nDexterity: {self.dexterity}")
        print("Inventory: ")
        for item in self.inventory:
            print(item.name)

    def combat_take_turn(self, monster_instance):
        print(f"Your Turn to Attack! \n What will you do? Enter 1-4 ")
        action = input(f" 1. Attack \n 2. Guard \n 3. Use Item \n 4. View Health \n ")
        if action == "1":
            self.attack(monster_instance)
        elif action == "2":
            self.guard(monster_instance)
        elif action == "3":
            print("Here are the items in your inventory: ")
            for item in self.inventory:
                print(item.name)
            item_name = input("Which item would you like to use?")
            for item in self.inventory:
                if item.name == item_name:
                    self.use_item(item)
                    break
                else:
                    print("Invalid Item or Item not in Inventory.")   
        elif action == "4":
            print(f"{self.name} has {self.health} HP.")         
        else:
            print("Invalid Action. Try Again.")