import sys
from copy import deepcopy
from random import randint

def player_names():
    player_one = str(input('Enter the first players name: '))
    player_two = str(input('Enter the second players name: '))
    return player_one, player_two


def start_new_game():
    temp = input("Press 1 to play or anything else to exit: ")
    if temp == "1":
        return True
    else:
        print("Exit from the game...")
        return False

    
def print_board(board):
    i = 0
    while i < 3:
        print("\n", "_________________", "\n")
        print("|", end="")
        j = 0
        while j < 3:
            print(" ", board[3*i + j], "|".rjust(2), end="")
            j += 1 
        i += 1
    print("\n", "_________________", "\n")


def cooridante_input():
    in_list = False
    chk_list = list("123456789")
    while not in_list:
        coordinate = input("Please enter the coordinate you want to mark: ")   
        if coordinate in chk_list:
            in_list = True
        else:
            print("Wrong input, try again!")
    index = int(coordinate) - 1
    return index   
            

def player_generator():
    temp = randint(0, 1)
    if temp == 0:
        player_one = 'X'
        player_two = 'O'
    else:
        player_one = 'O'
        player_two = 'X'
    return player_one, player_two


def chk_winning_conditions(player_names):
    i = 0
    while i < 3:        
        if board[0+3*i] == board[1+3*i] and board[1+3*i] == board[2+3*i]:
            if board[1+3*i] == player_one_mark:
                print(player_one_name, " is the winner!")
            else:
                print(player_two_name, " is the winner! ")
            return True      
        i += 1
        
    j = 0
    while j < 3:
        if board[0+j] == board[3+j] and board[3+j] == board[6+j]:
            if board[3+j] == player_one_mark:
                print(player_one_name, " is the winner!")
            else:
                print(player_two_name, " is the winner! ")
            return True
        j += 1 
            
    if board[0] == board[4] and board[4] == board[8]:
        if board[4] == player_one_mark:
            print(player_one_name, " is the winner!")
        else:
            print(player_two_name, " is the winner! ")
        return True
        
    elif board[2] == board[4] and board[4] == board[6]:
        if board[4] == player_one_mark:
            print(player_one_name, " is the winner!")
        else:
            print(player_two_name, " is the winner! ")
        return True

    elif len(reserve_list) == 9:
        print('This is a draw!')
        return True

    else:
        return False


def game_body(player_generator, player_names):     # ask about reference and constants tomorrow
    i = 1
    is_game_ended = False
    move = 0
    while not is_game_ended:             
        if (i % 2) == 1:
            print(player_one_name, 's turn')
            move = cooridante_input()           
            while move in reserve_list:
                print("this field is already taken!")
                move = cooridante_input()
            board[move] = player_one_mark
            reserve_list.append(move)          
        elif (i % 2) == 0:
            print(player_two_name, 's turn')
            move = cooridante_input()
            while move in reserve_list:
                print("this field is already taken!")
                move = cooridante_input()
            board[move] = player_two_mark
            reserve_list.append(move)
        i += 1
        print_board(board)
        is_game_ended = chk_winning_conditions(player_names)


new_game = True
while new_game:
    player_one_name, player_two_name = player_names()
    print(player_one_name, player_two_name)
    player_one_mark, player_two_mark = player_generator()
    board = list("123456789")
    reserve_list = []
    print_board(board)
    game_body(player_generator, player_names) 
    new_game = start_new_game()     