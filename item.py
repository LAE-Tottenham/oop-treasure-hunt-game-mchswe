class Item():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.type = category
    
    def __str__(self):
        return self.name
    
    # def __repr__(self):
    #     return f"Item(name={self.name}, weight={self.weight}, type={self.type})"