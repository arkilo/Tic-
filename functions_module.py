import math
import random
import os

board_map= {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
#total places are nine so only nine attempts allowed total
state_number = 0

#make a board
def make_board():
	r1 = " 			 {}  |  {}  | {} "
	print(r1.format(board_map[1],board_map[2],board_map[3]))
	print("			--------------")
	r2 = "			 {}  |  {}  | {} "
	print(r2.format(board_map[4],board_map[5],board_map[6]))
	print("			--------------")
	r3 = " 			 {}  |  {}  | {} "
	print(r3.format(board_map[7],board_map[8],board_map[9]))
	# global board_map
	# board_map[1]=3
	# print(board_map)

#take the player input
def player_input():
	user_var = input("Please type the coordinate for your move ")
	global board_map
	board_map[int(user_var)] = "X"
	# print(board_map)
	make_board()
	global state_number
	state_number += 1


def computer_game_input(moves):
	global board_map
	board_map[int(moves)] = "0"
	# print(board_map)

def choose_random():
	if state_number!=0:
		global board_map
		temp = list(board_map)
		# print("WJIOWNDIAN")
		# print("THIS IS TEMP {}".format(temp))
		temp_1 = []
		for i in range(1,9):
			if type(temp[i]) == int:
				temp_1.append(i) 
		# print(temp_1)
		computer_game_input(random.choice(temp_1))

def is_available(number):
	if board_map[number] == '0':
		return False
	else:
		return True
#computer play
def computer_move():
	#total possible ways of winning include 3 vertical, 3 horizontal, 2 diagonal
	#the goal is to block each attempt
	# if state_number == 0:
	# 	move = random.randint(1,9)
	# 	computer_game_input(move)

	#shitty linear logic tyme
		#vertical all combos
	print("Now is the computer's turn douchebag")
	if board_map[1] == 'X' and board_map[4] == 'X' and is_available(7):
		computer_game_input(7)

	elif board_map[4] == 'X' and board_map[7] == 'X' and is_available(1):
		computer_game_input(1)

	elif board_map[2] == 'X' and board_map[5] == 'X' and is_available(8):
		computer_game_input(8)

	elif board_map[5] == 'X' and board_map[8] == 'X' and is_available(2):
		computer_game_input(2)

	elif board_map[3] == 'X' and board_map[6] == 'X' and is_available(9):
		computer_game_input(9)

		#horizontal all combos

	elif board_map[1] == 'X' and board_map[2] == 'X' and is_available(3):
		computer_game_input(3)

	elif board_map[2] == 'X' and board_map[3] == 'X' and is_available(1):
		computer_game_input(1)

	elif board_map[4] == 'X' and board_map[5] == 'X' and is_available(6):
		computer_game_input(6)

	elif board_map[5] == 'X' and board_map[6] == 'X' and is_available(4):
		computer_game_input(4)

	elif board_map[7] == 'X' and board_map[8] == 'X' and is_available(9):
		computer_game_input(9)

	elif board_map[8] == 'X' and board_map[9] == 'X' and is_available(7):
		computer_game_input(7)

		#diagonal all combos

	elif board_map[3] == 'X' and board_map[5] == 'X' and is_available(7):
		computer_game_input(7)

	elif board_map[7] == 'X' and board_map[5] == 'X' and is_available(3):
		computer_game_input(3)

	elif board_map[1] == 'X' and board_map[5] == 'X' and is_available(9):
		computer_game_input(9)

	elif board_map[5] == 'X' and board_map[9] == 'X' and is_available(1):
		computer_game_input(1)

	else:
		choose_random()

	make_board()
	