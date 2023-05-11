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
        by Michael Scott, the manager. He didn't give you much direction
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

        current_time = current_time + timedelta(minutes=randint(5,25))
        if current_time >= end_time:
            print("\nIt's 5 PM! Great job today, time to go home!\n")
            print("~~~~~END OF GAME~~~~~\n")
            current_action = 'quit'
        else:
            formattedTime = current_time.strftime("%I:%M %p")
            print(f"\nThe current time is {formattedTime}.\n")

# Game functions
def create_rooms():
    global rooms
    bullpen = Room("bullpen", "\nYou walk into a bustling open-plan office space where employees work at\ntheir desks, cluttered with office supplies such as pens and DVDs. Pam, Angela,\nStanley, and Creed are crowded around reception")
    bullpen.add_item("dvd", "THREAT LEVEL MIDNIGHT: BY MICHAEL SCOTT")
    bullpen.add_item("pen", "a blue pen")
    bullpen.add_item_to_use("pen", "You fill out Stanley's crossword.")
    bullpen.add_item_to_use("stapler in jello", 'Dwight: "Dang it! Jim Put my stuff in jello again!\nThis is a gross misuse of company property. I am going to tell michael!')
    bullpen.add_person("pam", "Please don't throw trash at me.")
    bullpen.add_person("angela", "Poop is raining from the ceilings. POOP!")
    bullpen.add_person("stanley", "You are a professional idiot.")
    bullpen.add_person("creed", "I've never owned a refrigerator before.")
    bullpen.add_available_room("michael office")
    bullpen.add_available_room("Conference room")
    bullpen.add_available_room("Kitchen")

    rooms[bullpen.name] = bullpen

    conference_room = Room("conference room", "\nYou walk into a dark room, 5 rows of chairs face the front,\nwhere a small TV is propped up on a table. Kelly is\nsitting in the third row, next to Ryan, prattling about the Kardashians")
    conference_room.add_item("coin", "a small silver dime")
    conference_room.add_item("chair", "a generic grey and black office chair")
    conference_room.add_item_to_use("dvd", "You slide the dvd into the slot below the T.V.\nand michael Scarn comes onto the screen, dodging bullets coming\nfrom the evil delivery dude.Dramatically, Scarn says,'clean up on aisle five'")
    conference_room.add_item_to_use("chair", 'You throw the chair at a window and it breaks,\nCreed walks up behind you and yells "HEY THAT WAS MY CHAIR, NOT COOL DUDE!"\nthen he stomps out of the room.')
    conference_room.add_person("kelly", "Yeah, I have a lot of questions. Number one: How dare you?")
    conference_room.add_person("ryan", "Stanley yelled at me today. That was one of the most frightening experiences of my life.")
    conference_room.add_available_room("Bullpen")
   

    rooms[conference_room.name] = conference_room

    break_room = Room("break room", "\nYou walk into the break room, there are 3 large circle tables. On one of the tables sits a stapler in yellow jello.\nAlong the back wall, there is a line of vending machines. Sitting at the table closest to you, Jim, Phyllis,\nand Oscar are eating chips")
    break_room.add_item("stapler in jello", "a black stapler in yellow jello")
    break_room.add_item("chips", "a large bag of potato chips")
    break_room.add_item_to_use("coin", "You slide the silver dime into the slot in the vending machine, you select A4, a grape soda, you take it out and\ntake a sip!")
    break_room.add_item_to_use("chips", 'You take the bag of potato chips from Jim, Phyllis, and Oscar, and eat some.')
    break_room.add_person("jim", "FACT: BEARS EAT BEETS. BEARS. BEETS. BATTLESTAR GALACTICA")
    break_room.add_person("oscar", "I just want you to know you can't just say the word bankruptcy and expect anything to happen.")
    break_room.add_person("phyllis", "Close your mouth sweetie, you look like a trout.")
    break_room.add_available_room("Kitchen")


    rooms[break_room.name] = break_room

    kitchen = Room("kitchen", "\nYou walk into the kitchen, to your left, you see Meredith shaving her\nhead to get rid of lice. Sitting at the table, Kevin is eating\none of his many boxes of girl scout cookies. On the fridge, you\nsee Pam's drawing of a Sabre printer with captions written on it")
    kitchen.add_item("chili", "a large pan half filled with Kevin's famous chili")
    kitchen.add_item("mug", "Michael's white mug with black letters that says 'WORLDS BEST BOSS'")
    kitchen.add_item("drawing", "Pam's drawing of a Sabre printer")
    kitchen.add_item_to_use("cheese balls", "You slowly unscrew the lid off of the bright orange cheese balls,\nthe smell of greasy orange cheese powder overwhelms you. You pick up a\ncheese ball and throw it at Ryan as he is walking past, he\ncatches it in his mouth and walks back towards the conference room.")
    kitchen.add_item_to_use("chili", 'You take the lid off of the large metal pan on the counter, inside is\na bright and orange chili mixture, but it is only half filled and has\na few papers in it.')
    kitchen.add_item_to_use("drawing", "You walk up to Pam's drawing of a Sabre printer and write a caption on it.")
    kitchen.add_person("meredith", "Yeah, I have this thing about men cutting or threatening to cut my throat. Don't try to cut my throat!")
    kitchen.add_person("kevin", "The trick is to under cook the onions. Everybody is going to get to know each other in the pot.")
    kitchen.add_available_room("Bullpen")
    kitchen.add_available_room("Break Room")

    rooms[kitchen.name] = kitchen

    michael_office = Room("michael office", "\nYou walk into Michael's office which is cluttered with eccentric\ndecorations, including a coveted Dundie award, a chattering teeth toy,\nand a container of cheese balls. Michael Scott and Dwight Schrute\nare talking at the desk")
    michael_office.add_item("cheese balls", "a large container filled with bright orange cheese balls")
    michael_office.add_item("teeth", "chattering teeth toy")
    michael_office.add_item("dundie", "Michael's worlds best boss dundie")
    michael_office.add_item_to_use("teeth", "You twist the gear on the side of the teeth and they begin to chatter.")
    michael_office.add_item_to_use("dundie","Michael turns his dundie towards you, just like in the intro.")
    michael_office.add_item_to_use("mug", 'Dwight takes the WORLDS BEST BOSS mug and sets it on the floor to putt a golf ball into it')
    michael_office.add_person("michael", "I have flaws. What are they? I sing in the shower. Occasionally I'll hit somebody with my car. So sue me.")
    michael_office.add_person("dwight", "I am fast. To give you a reference point, I'm somewhere between a snake and a mongoose… and a panther.")
    michael_office.add_available_room("Bullpen")

    rooms[michael_office.name] = michael_office

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