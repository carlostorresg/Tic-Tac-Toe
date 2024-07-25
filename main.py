import random 
import time 
import os 
from functions import display_board, choose_marker, flip_coin, clear_screen, timer, is_position_empty, choose_position


print("---------------Welcome to tic tac toe------------------")

board = [" "] * 10



game_on = input("Do you want to start the game yes or no\n")
prefix = ("y","Y")

if game_on.startswith(prefix):
    game_on = True
else:
    game_on = False
    
while game_on:
    player1marker,player2marker = choose_marker()

    flip_coin()
    break




