import random #imports random for the flip function
import os #imports the os to clear the screen
import time #imports time for the timer 


def display_board(board):
    '''
    prints the board
    '''
    print("          " + board[1] + "|" + board[2] + "|" + board[3])
    print("       -----------       ")
    print("          " + board[4] + "|" + board[5] + "|" + board[6])
    print("       -----------       ")
    print("          " + board[7] + "|" + board[8] + "|" + board[9])


def choose_marker():
    '''
    getting the marker from the player
    '''
    marker1 = " "
     
    while marker1 not in ["X", "O"]:

        try:  
      
            marker1 = input("Player 1 choose between X or O \n").upper()

            marker2 = "O" if marker1 == "X" else "X" 
        except: 
            print("enter a valid input")
         
    return marker1,marker2


def flip_coin():
    '''
    picks a random number between 1 and 2
    '''
    flip = random.randint(1,2)

    if flip == 1:
        
        print(" player 1 goes first ") 
         
    else:
        print("player 2 goes first ")
        
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

def is_position_empty(board,position):
    '''
    checking if the position is available or not 
    '''
    
    return board[position] == " "
    

def choose_position(board):
    '''
    taking the input and puting it on the new board 
    '''
    position = 0
    
   
    while position not in range(1,10) and not is_position_empty(board,position): 
        position  = int(input("Choose your position from 1-9 "))

        return position 
         
    
#function to check if someone won 
def win_check(board,marker):
    
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
        if board[combination[0]] == marker and board[combination[1]] == marker and board[combination[2]] == marker:
            print(f"player {player2} has won the game !!")
            return True
        
    return False

    #'''full_board():

    #turn = player 2'''


