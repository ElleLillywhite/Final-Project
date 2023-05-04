import pickle

# Room class
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = {}
        self.itemsToUse = {}
        self.people = {}
        self.availableRooms = []
        print(f'Creating room {self.name}...')

    def add_item(self, item, description):
        self.items[item.lower()] = description

    def add_item_to_use(self, item, description):
        self.itemsToUse[item.lower()] = description

    def add_person(self, name, phrase):
        self.people[name] = phrase
    
    def add_available_room(self, name):
        self.availableRooms.append(name.lower())

    def look(self):
        print(f'You are in {self.name}. It is {self.description}.')
        if self.people:
            print('You look around and see some people:')
            for tempName in self.people.keys():
                print(f'    {tempName}')
        if self.items:
            print('Items in the room are:')
            for tempItem in self.items.keys():
                print(f'    {tempItem}: {self.items[tempItem]}')
        if self.itemsToUse:
            print('You can use these items in this room:')
            for tempItem in self.itemsToUse.keys():
                print(f'    {tempItem}')
        if self.availableRooms:
            print('You can go to these rooms:')
            for tempRoom in self.availableRooms:
                print(f'    {tempRoom}')

    def get_item(self, person):
        if self.items:
            itemToGet = input("What do you want to pick up? ").lower()
            if itemToGet in self.items:
                person.add_item(itemToGet)
                del self.items[itemToGet]
            else:
                print(f"There isn't a {itemToGet} in {self.name}.")
        else:
            print(f"{self.name} doesn't have any stuff to get.")

    def use_item(self, person):
        if self.itemsToUse:
            itemToUse = input("What do you want to use?\n").lower()
            if itemToUse in self.itemsToUse:
                if person.has_item(itemToUse):
                    person.use_item(itemToUse)
                    print(self.itemsToUse[itemToUse.lower()])
                else:
                    print(f"You don't have a {itemToUse}")
            else:
                print(f"You can't use a {itemToUse} in {self.name}.")
        else:
            print(f"{self.name} doesn't have any stuff you can use.")

    def talk(self):
        if self.people:
            print("You can talk to these people:")
            for tempPerson in self.people:
                print(f" {tempPerson}")
            name = input("Who would you like to talk to?\n")
            if name in self.people:
                print(f'{name}: "{self.people[name]}"')
        
    def move_to_room(self):
        if self.availableRooms:
            print("You can go to these rooms:")
            for tempRoom in self.availableRooms:
                print(f" {tempRoom}")
            roomChoice = input("Which room do you want to go to?").lower()            
            if roomChoice in self.availableRooms:
                return roomChoice
            else:
                print(f"Sorry, you can't get to {roomChoice} from here!")
                return None

    
# Player class
class Player:
    def __init__(self, name):
        print(f'Creating a new player named {name}')
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f'{self.name} picked up {item}.')

    def has_item(self, item):
        return item in self.inventory

    def use_item(self, item):
        self.inventory.remove(item)
        print(f'{self.name} used {item}.')
    
    def get_inventory(self):
        if self.inventory:
            print("You have this stuff in your inventory:")
            for tempItem in self.inventory:
                print(f" {tempItem}")
        else:
            print("You don't have anything!")



