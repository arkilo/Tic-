from functions_module import *
from functions_module import won_state
make_board()

for i in range(8):
	while won_state == 0:
		player_input()
		computer_move()
		who_won()
		print(won_state)
		if won_state == 1:
			break


rint("GAME OVER FUCKFACE")
