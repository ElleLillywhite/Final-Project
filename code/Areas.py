import pickle

# this class loads the rooms
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = {}
        self.itemsToUse = {}
        self.people = {}
        self.availableRooms = []

    def add_item(self, item, description):
        self.items[item.lower()] = description

    def add_item_to_use(self, item, description):
        self.itemsToUse[item.lower()] = description

    def add_person(self, name, phrase):
        self.people[name] = phrase
    
    def add_available_room(self, name):
        self.availableRooms.append(name.lower())
# this look function outputs a description of the room and available actions
    def look(self):
        print(f'You are in the{self.name}. {self.description}.\n')
        if self.people:
            #displays what people are in the room
            print('You look around and see some people:')
            for tempName in self.people.keys():
                print(f'    ~ {tempName}')
        if self.items:
            #displays items in the room
            print('Items in the room are:')
            for tempItem in self.items.keys():
                print(f'    ~ {tempItem}: {self.items[tempItem]}')
        if self.itemsToUse:
            #displays what items can be used in this room
            print('You can use these items in this room:')
            for tempItem in self.itemsToUse.keys():
                print(f'    ~ {tempItem}')
        if self.availableRooms:
            #displays available rooms from this destination.
            print('You can go to these rooms:')
            for tempRoom in self.availableRooms:
                print(f'    ~ {tempRoom}')
# get item function allows the player to get items and it adds it to the inventory
    def get_item(self, person):
        if self.items:
            itemToGet = input("What do you want to pick up?\n").lower()
            if itemToGet in self.items:
                person.add_item(itemToGet)
                del self.items[itemToGet]
            else:
                print(f"There isn't a {itemToGet} in {self.name}.")
        else:
            print(f"{self.name} doesn't have any stuff to get.")
#use item function allows the player to 
    def use_item(self, person):
        if self.itemsToUse:
            itemToUse = input("What do you want to use?\n").lower()
            if itemToUse in self.itemsToUse:
                if person.has_item(itemToUse):
                    person.use_item(itemToUse)
                    print(self.itemsToUse[itemToUse.lower()])
                else:
                    #catches if item isnt in inventory
                    print(f"You don't have a {itemToUse}")
            #catches if player tries to use an item in the wrong room
            else:
                print(f"You can't use a {itemToUse} in {self.name}.")
        else:
            print(f"{self.name} doesn't have any stuff you can use.")
#talk function prints out who you can talk to
    def talk(self):
        if self.people:
            print("You can talk to these people:")
            for tempPerson in self.people:
                print(f" {tempPerson}")
            name = input("Who would you like to talk to?\n").lower()
            if name in self.people:
                print(f'{name}: "{self.people[name]}"')
            else:
                #this sends error if the name is not in the room/spelled wrong.
                print(f"{name} is spelled wrong or not in this room.")
     #move room function which allows movement between rooms   
    def move_to_room(self):
        if self.availableRooms:
            print("You can go to these rooms:")
            for tempRoom in self.availableRooms:
                print(f" {tempRoom}")
            #roomChoice keeps track of which room player is in
            roomChoice = input("Which room do you want to go to?\n").lower()            
            if roomChoice in self.availableRooms:
                return roomChoice
            else:
                print(f"Sorry, you can't get to {roomChoice} from here!")
                return None

    
# Player class creates player, tells when player picks up an item
class Player:
    def __init__(self, name):
        print(f'Creating a new player named {name}')
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f'\n{self.name} picked up {item}.')

    def has_item(self, item):
        return item in self.inventory
#remove item from inventory when used
    def use_item(self, item):
        self.inventory.remove(item)
        print(f'{self.name} used the {item}.')
#prints out inventory
    def get_inventory(self):
        if self.inventory:
            #prints inventory
            print("You have this stuff in your inventory:")
            for tempItem in self.inventory:
                print(f" {tempItem}")
            print("")
        else:
            #displays if inventory is empty
            print("You don't have anything!")