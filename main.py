import random 
import time 
import os 
from functions import display_board, choose_marker, flip_coin, clear_screen, timer, is_position_empty, choose_position, win_check, tie_check


print("---------------Welcome to tic tac toe------------------")

board = [" "] * 10



game_on = input("Do you want to start the game yes or no\n")
yeschoice = ("y","Y")

if game_on.startswith(yeschoice):
    game_on = True
else:
    game_on = False
clear_screen()
    
player1marker,player2marker = choose_marker()

turn = flip_coin()
#game stars
while game_on:

        if turn  == "p1":

    
            display_board(board)

            position = choose_position(board)
    
            board[position] = player1marker

            clear_screen()
            
            if win_check(board,player1marker):
                break

            elif tie_check(board):
                break

            else: turn = "p2"


        else:
        
            display_board(board)

            position = choose_position(board)

            board[position] = player2marker

            clear_screen() 

            if win_check(board,player2marker):
                 break

            elif tie_check(board):
                 break

            else : turn = "p1"

        


game_on = False

    
    
    




