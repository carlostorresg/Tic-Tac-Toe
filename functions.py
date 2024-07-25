import random #imports random for the flip function
import os #imports the os to clear the screen
import time #imports time for the timer 


def displayboard(board):
    '''
    prints the board
    '''
    print("          " + board[1] + "|" + board[2] + "|" + board[3])
    print("       -----------       ")
    print("          " + board[4] + "|" + board[5] + "|" + board[6])
    print("       -----------       ")
    print("          " + board[7] + "|" + board[8] + "|" + board[9])


def player_input_marker():
    '''
    getting the marker from the player
    '''
    player1 = " "
     
    while player1 not in ["X", "O"]:
        player1 = input("Choose between X or O \n").upper()

        player2 = "O" if player1 == "X" else "X" 
         
    return player1,player2


def flip_coin(player1,player2):
    '''
    picks a random number between 1 and 2
    '''
    flip = random.randint(1,2)

    if flip == 1:
        
        print(" " + player1 + " goes first ") 
        player = player1 
        return player 
    else:
        print(" " + player2 + " goes first ")
        player = player2 
        return player 

def clear_screen():
    '''
    es like putting the command clear in the termianl
    '''
    os.system('clear')

def timer():
    '''
    makes a timer for 3 seconds
    '''
    print("game starting in 5 seconds")
    time.sleep(3)

def empty_check(board,position):
    '''
    checking if the position is available or not 
    '''
    if position > len(board):
        return False

    return board[position] == " "
    

def position_pick(board,player):
    '''
    taking the input and puting it on the new board 
    '''
    position = 11
    
   
    while position not in range(1,10) and not empty_check(board,position): 
        position  = int(input("Choose your position from 1-9 "))

        board[position] = player
         
    return board
#function to check if someone won 
def win_check(board,player):
    
    combinations = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,4,7],
        [2,5,8],
        [3,6,9],
        [1,5,9],
        [3,5,7]
    ]

    for combination in combinations:
        if board[combination[0]] == player and board[combination[1]] == player and board[combination[2]] == player:
            print(f"player {player} has won the game !!")
            return True
        
    return False
