import math
import random
import os

board_map= {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
#total places are nine so only nine attempts allowed total
state_number = 1
won_state = 0

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

def player_won(number_1,number_2,number_3):
	if board_map[number_1] == 'X' and board_map[number_2] == 'X' and board_map[number_3] == 'X':
		print("You won dickwad, go fuck yourself.")
		global won_state
		won_state +=1
		print("won state is {}".format(won_state))
	else:
		pass
def computer_won(number_1,number_2,number_3):
	if board_map[number_1] == '0' and board_map[number_2] == '0' and board_map[number_3] == '0':
		print("Your AI overlord won, go fuck yourself")
		global won_state
		won_state +=1
		print("won state is {}".format(won_state))


	else:
		pass
def move_logic(no_1,no_2,no_3):
	if board_map[no_1] == 'X' and board_map[no_2] == 'X' and is_available(no_3):
		computer_game_input(no_3)
		global state_variable
		state_variable +=1

#computer play
def computer_move():
	#total possible ways of winning include 3 vertical, 3 horizontal, 2 diagonal
	#the goal is to block each attempt
	# if state_number == 0:
	# 	move = random.randint(1,9)
	# 	computer_game_input(move)

	#shitty linear logic tyme
		#vertical all combos
	global state_variable
	state_variable = 0
	print("Now is the computer's turn douchebag")
	#horizontal 
	move_logic(1,4,7)
	move_logic(4,7,1)
	move_logic(2,5,8)
	move_logic(5,8,2)
	move_logic(3,6,9)
	move_logic(6,9,3)
	#vertical
	move_logic(1,2,3)
	move_logic(2,3,1)
	move_logic(4,5,6)
	move_logic(5,6,4)
	move_logic(7,8,9)
	move_logic(8,9,7)
	#diagonal
	move_logic(3,5,7)
	move_logic(7,5,3)
	move_logic(1,5,9)
	move_logic(5,9,1)
	# print(state_variable)

	if state_variable == 0:
	 	choose_random()

	make_board()
	
def who_won():

	player_won(1,4,7)
	player_won(2,5,8)
	player_won(3,6,9)
	player_won(1,2,3)
	player_won(4,5,6)
	player_won(7,8,9)
	player_won(1,5,9)
	player_won(3,5,7)

	computer_won(1,4,7)
	computer_won(2,5,8)
	computer_won(3,6,9)
	computer_won(1,2,3)
	computer_won(4,5,6)
	computer_won(7,8,9)
	computer_won(1,5,9)
	computer_won(3,5,7)



	
