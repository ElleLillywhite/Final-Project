import pickle

# Room class
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

# Item class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    
