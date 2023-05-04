#Example of the final project - text adventure program
from numpy import array
import pickle
from Rooms import rooms, MOVEMENT

ACTIONS=("quit",#quit game
		 "save",#save game
		 "load",#load previous save
		 "get",#add item to inventory
		 "use",#use item in inventory
		 "move")#display movement options

class Player():
	'''Player Object'''
	def __init__(self):
						#x, y, z
		self.__position = (0, 0, 0)
		self.inventory = []
		self.name = input("What is your name? ").title()
		print(f"{self.name} begins an epic quest...")

	@property
	def position(self):
		return tuple(self.__position)
	@position.setter
	def position(self, new):
		self.__position += new

def valid_input(prompt = "What would you like to do? "):
	'''force the player to select a valid action'''
	print("\t--COMMANDS--")
	response = None
	while response not in ACTIONS:
		print(f"Actions:\n{ACTIONS}")
		response = input(prompt).lower()
	return response

def save():
	'''save the player object and rooms dictionary to a file'''
	with open('game.dat','wb') as f:
		pickle.dump(player,f)
		pickle.dump(rooms,f)
	print("Game saved!")

def load():
	'''load the player object and rooms dictionary from a file'''
	#using global variables to reduce size
	global player
	global rooms
	try:
		with open("game.dat",'rb') as f:
			player = pickle.load(f)
			rooms = pickle.load(f)
		print("Game loaded!")
	except FileNotFoundError:
		print("Game file not found!")

player = Player()
def main(player):
	choice = None
	while choice != "quit":
		#unpack current room variables
		room = rooms.get(player.position, "Invalid room setting - something broke")
		print(room.description())
		choice = valid_input()
		if choice == "quit":
			print("Thanks for playing!")
		elif choice == "save":
			save()
		elif choice == "load":
			load()
		elif choice == "get":
			room.get_item(player)
		elif choice == "use":
			room.use_item(player)
		elif choice == "move":
			room.move(player)

if __name__ == "__main__":
	main(player)