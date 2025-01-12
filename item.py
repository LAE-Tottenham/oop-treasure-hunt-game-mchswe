class Item():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.type = category
    
    def __str__(self):
        return self.name