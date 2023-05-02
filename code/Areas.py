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

    
# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

# Game variables
current_room = None
player = None

# Game functions
def create_rooms():
    reception = Room("Reception", "You are in the reception area of Dunder Mifflin.")
    reception.add_item(Item("Phone", "A phone with a notepad next to it."))
    reception.add_item(Item("Pen", "A blue pen."))

    conference_room = Room("Conference Room", "You are in the conference room.")
    conference_room.add_item(Item("Whiteboard Marker", "A black whiteboard marker."))

    break_room = Room("Break Room", "You are in the break room.")
    break_room.add_item(Item("Coffee Mug", "A white coffee mug."))

    warehouse = Room("Warehouse", "You are in the warehouse.")
    warehouse.add_item(Item("Stapler", "A red stapler."))

    return [reception, conference_room, break_room, warehouse]

def create_player(name):
    return Player(name)


def save_game():
    with open("save_game.bin", "wb") as f:
        pickle.dump((current_room, player), f)


def load_game():
    global current_room, player
    with open("save_game.bin", "rb") as f:
        current_room, player = pickle.load(f)

def print_current_room():
    print(current_room.name)
    print(current_room.description)
    if len(current_room.items) > 0:
        print("Items in room:")
        for item in current_room.items:
            print("- " + item.name)

def print_player_inventory():
    print("Inventory:")
    if len(player.inventory) > 0:
        for item in player.inventory:
            print("- " + item.name)
    else:
        print("Your inventory is empty.")

def move_to_room(room_name):
    global current_room
    for room in rooms:
        if room.name.lower() == room_name.lower():
            current_room = room
            print_current_room()
            return
    print("Sorry, that room does not exist.")