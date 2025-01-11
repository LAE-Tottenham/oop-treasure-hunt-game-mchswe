class Place():
    def __init__(self, given_name, given_size, locked=False):
        # locked=False means that the locked parameter will be False by default if not provided.
        self.name = given_name
        self.size = given_size
        self.locked = locked
        self.next_places = []
        self.items = []
        self.monsters = []
        self.npcs = []

    def __str__(self):
        return self.name

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)

    def add_item(self, item_instance):
        self.items.append(item_instance)
    
    def remove_item(self, item_instance):
        self.items.remove(item_instance)
    
    def add_monster(self, monster_instance):
        self.monsters.append(monster_instance)

    def add_npc(self, npc_instance):
        self.npcs.append(npc_instance)

    def show_next_places(self):
        print("The possible places you can go to are: ")
        for place in self.next_places:
            # remember that next_places is a list of Place instances hence why we can use place.name
            print(str(place.name))
    
    def show_items(self):
        print("The items in this location are: ")
        for item in self.items:
            print(str(item.name))
    
    def check_lock(self):
        return self.locked

    def unlock(self, key_item):
        if key_item.type == "key":
            self.locked = False
            print(f"{self.name} has been unlocked!")
        else:
            print("You need a key to access this place.")
    
    def description(self):
        print(f"You are at {str(self.name)}.")
        self.show_items()
        self.show_next_places()