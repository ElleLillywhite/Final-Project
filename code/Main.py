import pickle
import datetime
from datetime import timedelta
from Areas import Room, Player
from random import randint

# Game variables

current_room = "reception"
current_action = "begin"
player = None
rooms = {}
current_time = None

ACTION_LIST=("quit",
		 "save",
		 "load",
		 "get",
		 "use",
		 "move",
         "talk",
         "inventory")



def main():
    global player, current_room, current_time, current_action
    player = Player(input('What is your name there home stump?'))
    create_rooms()
    current_room = "reception"
    current_action = "begin"
    start_time = datetime.datetime(2007, 7, 16, 8, 0, 0)
    end_time = datetime.datetime(2007, 7, 16, 17, 0, 0)
    current_time = start_time
    rooms[current_room].look()

    while current_action != 'quit':
        
        print('What do you want to do?')
        current_action = input(f'{ACTION_LIST}\n')
        match current_action:
            case "load": #load the game from a file
                print("Loading game from file")
                load_game()
            case "save": #save the game from a file
                print("current room before saving is " + current_room)
                save_game()
            case "get": #get an item
                rooms[current_room].get_item(player)
            case "use": #use an item
                rooms[current_room].use_item(player)
            case "move": #move to another room
                nextRoom = rooms[current_room].move_to_room()
                if nextRoom in rooms.keys():
                    current_room = nextRoom
                    rooms[current_room].look()
            case "talk": #talk to someone
                rooms[current_room].talk()
            case "inventory":
                player.get_inventory()
            case "quit": #do nothing and we will automatically quit
                print("exiting game")

        current_time = current_time + timedelta(minutes=randint(5,60))
        if current_time >= end_time:
            print("It's 5 PM, time to go home!")
            current_action = 'quit'
        else:
            formattedTime = current_time.strftime("%I:%M %p")
            print(f"The current time is {formattedTime}.")

# Game functions
def create_rooms():
    global rooms
    reception = Room("reception", "the reception area of Dunder Mifflin.")
    reception.add_item("phone", "A phone with a notepad next to it.")
    reception.add_item("pen", "A blue pen.")
    reception.add_item_to_use("pen", "You write a note.")
    reception.add_person("Pam", "Please don't throw trash at me...")
    reception.add_person("Dwight", "Identity theft is not a joke!")
    reception.add_available_room("Michael's office")
    reception.add_available_room("Conference room")
    reception.add_available_room("Kitchen")

    rooms[reception.name] = reception

    conference_room = Room("conference room", "a regular old conference room.")
    conference_room.add_item("whiteboard marker", "A black whiteboard marker.")

    rooms[conference_room.name] = conference_room

    break_room = Room("break room", "stinky.")
    break_room.add_item("coffee mug", "A white coffee mug.")

    rooms[break_room.name] = break_room

    warehouse = Room("warehouse", "full of boxes.")
    warehouse.add_item("stapler", "A red stapler.")

    rooms[warehouse.name] = warehouse

def save_game():
    print("Saving game to file...")
    current_room, current_action, player, rooms, current_time
    with open("save_game.bin", "wb") as f:
        print("Current room is " + current_room)
        pickle.dump(current_room, f)
        pickle.dump(current_action, f)
        pickle.dump(player, f)
        pickle.dump(current_time, f)
    print("Game saved!")


def load_game():
    print("Loading game from file...")
    global current_room, current_action, player, rooms, current_time
    with open("save_game.bin", "rb") as f:
        print(current_room)
        current_room = pickle.load(f)
        print(current_room)
        current_action = pickle.load(f)
        player = pickle.load(f)
        current_time = pickle.load(f)
    print("Game loaded!")

if __name__ == "__main__":
	main()