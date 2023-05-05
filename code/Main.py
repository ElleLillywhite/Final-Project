import pickle
import datetime
from datetime import timedelta
from Areas import Room, Player
from random import randint

# Game variables

current_room = "bullpen"
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
    print("""
                            ~|   THE OFFICE GAME   |~
                           Created by: Elle Lillywhite
        
        Welcome to "The Office Game" you've just been hired to be a temp
        by Micheal Scott, the manager. He didn't give you much direction
        on what you are supposed to do so take your time exploring. You
        will be realeased from work at 5PM. Good Luck :)


    """)
    player = Player(input('What is your name?\n'))
    create_rooms()
    current_room = "bullpen"
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
                print("Loading game from file...\n")
                load_game()
            case "save": #save the game from a file
                print("Current room before saving is " + current_room)
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
                print("~~~EXITING GAME~~~")

        current_time = current_time + timedelta(minutes=randint(5,60))
        if current_time >= end_time:
            print("It's 5 PM! Great job today, time to go home!\n")
            current_action = 'quit'
        else:
            formattedTime = current_time.strftime("%I:%M %p")
            print(f"The current time is {formattedTime}.\n")

# Game functions
def create_rooms():
    global rooms
    bullpen = Room("bullpen", "the main office area of Dunder Mifflin")
    bullpen.add_item("dvd", "THREAT LEVEL MIDNIGHT: BY MICHEAL SCOTT")
    bullpen.add_item("pen", "a blue pen.")
    bullpen.add_item_to_use("pen", "You fill out Stanley's crossword.")
    bullpen.add_item_to_use("stapler in jello", 'Dwight: "Dang it! Jim Put my stuff in jello again!\nThis is a gross misuse of company property. I am going to tell Micheal!')
    bullpen.add_person("Pam", "Please don't throw trash at me.")
    bullpen.add_person("Angela", "Poop is raining from the ceilings. POOP!")
    bullpen.add_person("Stanley", "You are a professional idiot.")
    bullpen.add_person("Creed", "I've never owned a refrigerator before.")
    bullpen.add_available_room("Michael's office")
    bullpen.add_available_room("Conference room")
    bullpen.add_available_room("Kitchen")

    rooms[bullpen.name] = bullpen

    conference_room = Room("conference room", "\nYou walk into a dark room, 5 rows of chairs face the front, where a small TV is propped up on a table. Kelly is\nsitting in the third row, next to Ryan, prattling about the Kardashians")
    conference_room.add_item("coin", "a small silver dime")
    conference_room.add_item("chair", "a generic grey and black office chair")
    conference_room.add_item_to_use("dvd", "You slide the dvd into the slot below the T.V.\nand Micheal Scarn comes onto the screen, dodging bullets coming\nfrom the evil delivery dude.Dramatically, Scarn says,'clean up on aisle five'")
    conference_room.add_item_to_use("chair", 'You throw the chair at a window and it breaks,\nCreed walks up behind you and yells "HEY THAT WAS MY CHAIR, NOT COOL DUDE!"\nthen he stomps out of the room.')
    conference_room.add_person("Kelly", "Yeah, I have a lot of questions. Number one: How dare you?")
    conference_room.add_person("Ryan", "Stanley yelled at me today. That was one of the most frightening experiences of my life.")
    conference_room.add_available_room("Bullpen")
   

    rooms[conference_room.name] = conference_room

    break_room = Room("break room", "You walk into the break room, there are 3 large circle tables. On one of the tables sits a stapler in yellow jello.\nAlong the back wall, there is a line of vending machines. Sitting at the table closest to you, Jim, Phyllis,\nand Oscar are eating chips.")
    break_room.add_item("stapler in jello", "a black stapler in yellow jello")
    break_room.add_item("chips", "a large bag of potato chips")
    break_room.add_item_to_use("coin", "You slide the silver dime into the slot in the vending machine, you select A4, a grape soda, you take it out and\ntake a sip!")
    break_room.add_item_to_use("chips", 'You take the bag of potato chips from Jim, Phyllis, and Oscar, and eat some.')
    break_room.add_person("Jim", "FACT: BEARS EAT BEETS. BEARS. BEETS. BATTLESTAR GALACTICA")
    break_room.add_person("Oscar", "I just want you to know you can't just say the word bankruptcy and expect anything to happen.")
    break_room.add_available_room("Kitchen")


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