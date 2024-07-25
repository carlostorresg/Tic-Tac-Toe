import random 
import time 
import os 
from functions import displayboard, player_input_marker, flip_coin, clear_screen, timer, empty_check, position_pick 


print("---------------Welcome to tic tac toe------------------")

board = [" "] * 10

player1,player2 = player_input_marker()

print("\n")

player = flip_coin(player1,player2)

timer()

clear_screen()

displayboard(board)

#choose position 
position_pick(board,player)

displayboard(board)

