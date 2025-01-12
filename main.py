from place import Place
from player import Player
from item import Item
from monster import Monster
from npc import NPC
import os

def clear_screen():     # makes the game more readable
    # windows
    if os.name == "nt":
        os.system("cls")
    else:
        #mac/linux
        os.system("clear")

class Game():
    def __init__(self):
        self.current_place = None
        # add more atributes as needed

    def setup(self):
        # here you will setup your Game
        # places
        home = Place('Home', 10)
        bedroom = Place('Bedroom', 5)
        bathroom = Place('Bathroom', 4, True) # bathroom is locked
        garden = Place('Garden', 15)
        shed = Place('Shed', 3)
        cave = Place('Cave', 50)
        pallon_village = Place("Pallon Village", 60)
        pallon_vault = Place("Vault of Pallon", 40, True)   # Vault Keys
        brick_crossroads = Place("Brick Crossroads", 20)
        dunbar_quays = Place("Dunbar Quay", 40, True)   # Quay Keys
        engardia_town = Place("Engardia Town", 70)
        engardia_apoth = Place("Engardia Apothecary",10)
        final_cross = Place("Longa Via", 15)
        hrule = Place("Hrule", 30)
        secret_winspot = Place("Cave Corner", 10, True) # secret win spot
        
        # connecting places
        cave.add_next_place(secret_winspot) # cave -> secret win spot # will be stuck in here if 
        home.add_next_place(garden)    # home -> garden
        home.add_next_place(bedroom)    # home -> bedroom
        bedroom.add_next_place(home)    # bedroom -> home
        bedroom.add_next_place(bathroom)    #bedroom -> bathroom
        bathroom.add_next_place(bedroom)    # bathroom -> bedroom
        garden.add_next_place(shed)    # garden -> shed
        garden.add_next_place(home) # garden -> home
        shed.add_next_place(cave)   # shed -> cave
        cave.add_next_place(shed)   # cave -> shed
        shed.add_next_place(garden) # shed -> garden
        home.add_next_place(pallon_village) # home -> pallon village    
        pallon_village.add_next_place(home) # pallon village -> home
        pallon_village.add_next_place(pallon_vault) # pallon village -> pallon vault
        pallon_village.add_next_place(brick_crossroads) # pallon village -> brick crossroads
        pallon_vault.add_next_place(pallon_village) # pallon vault -> pallon village
        brick_crossroads.add_next_place(dunbar_quays)   # brick crossroads -> dunbar quays
        dunbar_quays.add_next_place(brick_crossroads)   # dunbar quays -> brick crossroads
        brick_crossroads.add_next_place(pallon_village) # brick crossroads -> pallon village
        brick_crossroads.add_next_place(engardia_town)  # brick crossroads -> engardia town
        engardia_town.add_next_place(brick_crossroads)  # engardia town -> brick crossroads
        engardia_town.add_next_place(engardia_apoth)    # engardia town -> engardia apothecary
        engardia_apoth.add_next_place(engardia_town)    # engardia apothecary -> engardia town
        engardia_town.add_next_place(final_cross)    # engardia town -> final cross
        final_cross.add_next_place(engardia_town)   # final cross -> engardia town
        final_cross.add_next_place(hrule)   # final cross -> hrule
        hrule.add_next_place(final_cross)   # hrule -> final cross

        # items

        # winning item
        win_heart = Item("Heart of Gesshin", 0, "winning_item")
        secret_note = Item("Secret Note", 0, "secret_win")
        # misc
        hammer = Item('Hammer', 5, "misc")
        pen = Item('Pen', 0, "misc")
        # Keys
        bath_key = Item("Bathroom Key", 1, "key")
        vault_key = Item("Vault of Pallon Key", 1, "key")
        dunbar_key = Item("Dunbar Quay Key", 1, "key")
        # Consumables
        medicine = Item("Medicine", 2, "medicine")
        str_potion = Item("Strength Potion", 4, "str potion")
        scroll = Item("Ancient Scroll", 1, "book")
        elixir = Item("Ominous Elixir", 4, "elixir")
        # Weapons
        book = Item("Book", 5, "book")
        b_sword = Item("Bastard Sword", 10, "sword") # shed
        dagger = Item("Dagger", 8, "dagger") #  shed
        t_dagger = Item("Thief's Dagger", 6, "dagger")  # engardia apothecary
        excalibur = Item("Excalibur", 15, "weapon") # pallon vault
        cadenza = Item("Cadenza", 14, "h_sword")  # dunbar quay
        h_axe = Item("Heavy Axe", 15, "axe")    # pallon village
        ifrit_axe = Item("Ifrit", 16, "axe")    # engardia apothecary
        caladbolg = Item("Caladbolg", 22, "h_sword")  # hrule
        # Misc
        paper = Item("Piece of Paper", 0, "misc")
        mirror = Item("Mirror", 0, "misc")
        bottle = Item("Glass Bottle", 0, "misc")
        
        # adding items to locations
        home.add_item(hammer)
        bedroom.add_item(pen)
        bedroom.add_item(bath_key)
        # keys added
        pallon_village.add_item(vault_key)
        # add_item(dunbar_key) -- Dropped by Hobgoblin
        # consumables/misc added
        engardia_apoth.add_item(medicine)
        engardia_apoth.add_item(str_potion)
        engardia_apoth.add_item(scroll)
        bedroom.add_item(medicine)
        bedroom.add_item(medicine)
        bedroom.add_item(bottle)
        shed.add_item(book)
        shed.add_item(paper)
        shed.add_item(mirror)
        engardia_town.add_item(pen)
        engardia_town.add_item(medicine)
        engardia_town.add_item(str_potion)
        dunbar_quays.add_item(elixir)        
        # weapons added
        engardia_apoth.add_item(t_dagger)
        engardia_apoth.add_item(ifrit_axe)
        dunbar_quays.add_item(cadenza)
        shed.add_item(b_sword)
        shed.add_item(dagger)
        pallon_vault.add_item(excalibur)
        pallon_village.add_item(h_axe)
        hrule.add_item(caladbolg)

        # monsters
        goblin = Monster("Goblin", 40, 4, 7, False)   # cave, pallon village
        sec_goblin = Monster("Minion Goblin", 40, 2, 6, False)   # cave, pallon village
        hobgoblin = Monster("Hobgoblin", 80, 7, 12, False) # pallon village, pallon vault, brick crossroads
        brick_hobgoblin = Monster("Weak Hobgoblin", 70, 4, 11, False)
        bandit = Monster("Bandit", 60, 4, 7, False)    # brick crossroads, dunbar quay, engardia town
        sec_bandit = Monster("Malnourished Bandit", 50, 2, 6, False)    # brick crossroads, dunbar quay, engardia town
        bandit_leader = Monster("Bandit Leader", 120, 13, 19, False)    # engardia town, brick crossroads
        vandal = Monster("Vandal", 100, 10, 15, False)  # engardia town, final cross
        gesshin = Monster("Gesshin", 380, 26, 36, True) # hrule boss
        hyur = Monster("Hyur", 140, 19, 23, True) # pallon_vault boss
        aggelos = Monster("Aggelos", 200, 21, 29, True) # dunbar quay boss

        #adding loot to monsters
        gesshin.add_loot(win_heart)
        brick_hobgoblin.add_loot(dunbar_key)

        # adding monsters to locations

        # goblin spawns
        cave.add_monster(goblin)
        cave.add_monster(sec_goblin)
        pallon_village.add_monster(goblin)        
        pallon_village.add_monster(sec_goblin)        
        # hobgoblin spawns
        pallon_village.add_monster(hobgoblin)
        pallon_vault.add_monster(hobgoblin)
        brick_crossroads.add_monster(brick_hobgoblin)
        # bandit spawns
        brick_crossroads.add_monster(bandit)
        brick_crossroads.add_monster(sec_bandit)
        dunbar_quays.add_monster(sec_bandit)
        dunbar_quays.add_monster(bandit)
        engardia_town.add_monster(bandit)
        engardia_town.add_monster(bandit_leader)
        # vandal spawns
        engardia_town.add_monster(vandal)
        engardia_town.add_monster(vandal)
        final_cross.add_monster(vandal)
        # boss spawns
        hrule.add_monster(gesshin)
        pallon_vault.add_monster(hyur)
        dunbar_quays.add_monster(aggelos)

        # NPCs
        apothecary = NPC("Apothecary", [medicine, str_potion, scroll]) # engardia apothecary
        traveller = NPC("Travelling Wanderer", [])  # last cross

        # adding NPCs to locations
        engardia_apoth.add_npc(apothecary)
        final_cross.add_npc(traveller)
                
        # home will be our starting place
        self.current_place = home
        
        # finish the setup function...

    # combat logic

    def combat(self, player, monster):
        print(f"{player.name} is now fighting {monster.name}! ")
        while player.health > 0 and monster.health > 0:
            player.combat_take_turn(monster)
            if monster.health <= 0:
                monster.is_defeated()
                break
            monster.combat_take_turn(player)
            if player.health <= 0:
                print(f"{player.name} has been defeated. \n Game Over.")
                input("Press Enter to continue...")
                break
        print("Combat has ended.")
        input("Press Enter to continue...")


    def start(self):
        print("Welcome to my game...")
        print("Storyline...")
        name = input("Enter player name: ")
        player = Player(name)
        play = True
        while play:
            clear_screen()
            print("You are currently in " + str(self.current_place.name))
            self.current_place.show_next_places()
            opt = input(f"""
   \n What would you like to do? Enter 1-9
    1. Go to a Place
    2. Pickup Item
    3. Check Inventory
    4. Attack Enemy
    5. Use Item
    6. Inspect Place
    7. Train
    8. Display Stats
    9. Quit \n   
    """)
            if opt == "1":
                print("Where would you like to go?")
                self.current_place.show_next_places()
                place_name = input("Enter where you would like to go next: ")
                for place in self.current_place.next_places:
                    if place.name == place_name:
                        if place.locked:
                            key_name = f"{place.name} Key"
                            has_key = any(item.name == key_name and item.type == "key" for item in player.inventory)
                            if has_key:
                                place.unlock()
                                self.current_place = place
                                print(f"You are now at {place.name}.")
                                self.current_place.description()
                                print(" ")
                            else:
                                print(f"{place.name} is locked. You need a key to enter.")
                                print(" ")
                            input("Press Enter to continue...")
                            break
                        else:
                            self.current_place = place
                            print(f"You are now at {place.name}.")
                            self.current_place.description()
                            print(" ")
                            break 
                else:
                    print("This place does not exist. Please select from one of the options.")
            elif opt == "2":
                print("Here are the items in this area: ")
                for item in self.current_place.items:
                    print(str(item.name))
                item_name = input("What would you like to pick up? ")
                for item in self.current_place.items:
                    if item.name == item_name:
                        player.add_item(item)
                        self.current_place.remove_item(item)
                        print(f"{str(item.name)} has been picked up.")
                        break
                    else:
                        print("This item does not exist in this location.")
            elif opt == "3":
                print(f"Here is your invetory: ")
                for item in player.inventory:
                    print(str(item.name))
                player.calculate_inventory_size()
                input("Press Enter to continue...")
            elif opt == "4":
                if not self.current_place.monsters:
                    print("No monsters in this location.")
                else:
                    print("Enemies in this location: ")
                    for monster in self.current_place.monsters:
                        print(str(monster.name))
                    monster_name = input("Which enemy would you like to attack?:  ")
                    for monster in self.current_place.monsters:
                        if monster.name == monster_name:
                            self.combat(player, monster)
                            if monster.health <= 0:
                                self.current_place.monsters.remove(monster)
                            break
                        elif player.health <= 0:
                            print(f"{player.name} has been defeated. \n Game Over. Please try again.")
                            play = False
                    else:
                        print("Invalid Monster Name. Please select from the list.")
            elif opt == "5":
                print(f"Here are the items in your inventory: ")
                for item in player.inventory:
                    print(f"{item.name} - Weight: {item.weight} - Type: {item.type}")
                item_name = input("Which item would you like to use? ")
                for item in player.inventory:
                    if item.name == item_name:
                        player.use_item(item)
                        break
                else:
                    print("Invalid Item Name or Item Not in Inventory.")
            elif opt == "6":
                str(self.current_place.description())
                print(f"The monsters here are: ")
                for monster in self.current_place.monsters:
                    print(str(monster.name))
                input("Press Enter to continue...")
                
            elif opt == "7":
                player.train()
                input("Press Enter to continue...")
            elif opt == "8":
                player.display_stats()
                input("Press Enter to continue...")
            elif opt == "9":
                print("Thank you for Playing.")
                play = False
            else:
                print("Invalid Option. Please select one of the options above.")

game = Game()
game.setup()
game.start()
