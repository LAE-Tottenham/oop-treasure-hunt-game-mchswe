from place import Place
from player import Player
from item import Item
from monster import Monster
from npc import NPC

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
        
        home.add_next_place(garden)
        home.add_next_place(bedroom)
        bedroom.add_next_place(bathroom)
        garden.add_next_place(shed)
        shed.add_next_place(cave)
        home.add_next_place(pallon_village)
        pallon_village.add_next_place(pallon_vault)
        pallon_village.add_next_place(brick_crossroads)
        brick_crossroads.add_next_place(dunbar_quays)
        brick_crossroads.add_next_place(engardia_town)
        engardia_town.add_next_place(engardia_apoth)
        engardia_town.add_next_place(final_cross)
        final_cross.add_next_place(hrule)

        # items
        hammer = Item('Hammer', 5)
        pen = Item('Pen')
        # Keys
        bath_key = Item("Bathroom Key", 1, "key")
        vault_key = Item("Pallon Vault Key", 1, "key")
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
        cadenza = Item("Cadenza", 14, "sword")  # dunbar quay
        h_axe = Item("Heavy Axe", 15, "axe")    # pallon village
        ifrit_axe = Item("Ifrit", 16, "axe")    # engardia apothecary
        # Misc
        paper = Item("Piece of Paper", 0, "misc")
        mirror = Item("Mirror", 0, "misc")
        bottle = Item("Glass Bottle", 0, "misc")
        # 


        home.add_item(hammer)
        bedroom.add_item(pen)

        # home will be our starting place
        self.current_place = home
        
        # finish the setup function...

    def start(self):
        print("Welcome to my game...")
        print("Storyline...")
        name = input("Enter player name: ")
        player = Player(name)

        print("You are currently in " + self.current_place.name)
        self.current_place.show_next_places()
        opt = input("""
What would you like to do?
1. Go to a Place
2. Pickup Item
3. Check Inventory
4. Inspect Place
etc.   
""")
        if opt == "1":
            # add code
            pass
        elif opt == "2":
            # add code
            pass
        elif opt == "3":
            # add code
            pass
            
