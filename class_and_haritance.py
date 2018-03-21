import random as Ran
global game_counter
global com_total_moving
global user_total_moving

class ClassMain(object):
	def __init__(self, name, turns):
		self.__name = name
		self.__turns = turns
	def print_counter(self, count):
		for i in range(1,count):
			print (" ", end="")
	def get_name(self):
		return self.__name
	def get_turns(self):
		return self.__turns

class ClassSon(ClassMain):
	# def __init__(self, name, turns):
	# 	super(ClassMain, self).__init__()
	# 	self.name = name
	# 	self.turns = turns
	def making_rand(self):
		Ran_num = Ran.randrange(1, 7) # 1이상 7미만 정수형
		return Ran_num
	def end_winner(self, first, second, user1, user2):
		if first > second:
			print()
			print(" >> The Winner Is : "+ user1)
		elif first < second:
			print()
			print(" >> The Winner Is : "+ user2)
		else :
			print()
			print(" >> The Winner Is : No one! ")
			print(" >> Draw the game :) >> ")

user_name = input(" >> What is ur name : ")
user_turns = input(" >> How many time do y wanna play game : ")
game = ClassSon(user_name, user_turns)

# global value init
game_counter = 0
com_total_moving = 0
user_total_moving = 0
#

in_char = None
while in_char != "q" and game_counter < int(user_turns):
	in_char = input(" >> Press any button to contiue game! >> ")
	com_rand = game.making_rand()
	user_rand = game.making_rand()
	move_counter = com_rand - user_rand
	#
	if move_counter >= 0: #computer win
		game_counter += 1
		print("──────────────────────────────────")
		print()
		com_total_moving += move_counter
		game.print_counter(com_total_moving)
		print("[ COM ] ")
		print()
		print("──────────────────────────────────")
	else : #user win
		game_counter += 1
		print("──────────────────────────────────")
		print()
		user_total_moving += abs(move_counter) #절대값
		game.print_counter(user_total_moving)
		print("[ "+game.get_name()+" ] ")
		print()
		print("──────────────────────────────────")
	#

game.end_winner(com_total_moving, user_total_moving, "COM", game.get_name())