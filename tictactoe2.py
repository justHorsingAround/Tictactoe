import sys
import test_client
from random import randint
from timeit import default_timer


def player_names():
    player_one = str(input('Enter the first players name: '))
    player_two = str(input('Enter the second players name: '))
    return player_one, player_two


def start_new_game():
    temp = input("\n\033[1;33mPress 1 to play or anything else to exit: \033[0;0m")
    if temp == "1":
        return True
    else:
        print("\033[1;31mThe game has been terminated by the user!\033[0;0m")

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
            print("\033[1;31mWrong input, try again!\033[0;0m")
    index = int(coordinate) - 1
    return index   
            

def player_generator():
    temp = randint(0, 1)
    if temp == 0:
        player_one = '\033[1;31mX\033[0;0m'
        player_two = '\033[1;32mo\033[0;0m'
    else:
        player_one = '\033[1;32mo\033[0;0m'
        player_two = '\033[1;31mX\033[0;0m'
    return player_one, player_two


def chk_winning_conditions(player_one_name, player_two_name):
    i = 0
    while i < 3:        
        if board[0+3*i] == board[1+3*i] and board[1+3*i] == board[2+3*i]:
            if board[1+3*i] == player_one_mark:
                print(player_one_name, "is the winner!")
                with open ('tictactoe_scores.txt', 'a') as f:
                    f.write(player_one_name + '\n')
            else:
                print(player_two_name, "is the winner! ")
                with open ('tictactoe_scores.txt', 'a') as f:
                    f.write(player_two_name + '\n')
            return True      
        i += 1        
    j = 0
    while j < 3:
        if board[0+j] == board[3+j] and board[3+j] == board[6+j]:
            if board[3+j] == player_one_mark:
                print(player_one_name, "is the winner!")
                with open ('tictactoe_scores.txt', 'a') as f:
                    f.write(player_one_name + '\n')
            else:
                print(player_two_name, "is the winner! ")
                with open ('tictactoe_scores.txt', 'a') as f:
                    f.write(player_two_name + '\n')
            return True
        j += 1            
    if board[0] == board[4] and board[4] == board[8]:
        if board[4] == player_one_mark:
            print(player_one_name, "is the winner!")
            with open ('tictactoe_scores.txt', 'a') as f:
                f.write(player_one_name + '\n')
        else:
            print(player_two_name, "is the winner! ")
            with open ('tictactoe_scores.txt', 'a') as f:
                f.write(player_two_name + '\n')
        return True        
    elif board[2] == board[4] and board[4] == board[6]:
        if board[4] == player_one_mark:
            print(player_one_name, "is the winner!")
            with open ('tictactoe_scores.txt', 'a') as f:
                f.write(player_one_name + '\n')
        else:
            print(player_two_name, "is the winner! ")
            with open ('tictactoe_scores.txt', 'a') as f:
                f.write(player_two_name + '\n')
        return True
    elif len(reserve_list) == 9:
        print('This is a draw!')
        return True    
    else:
        return False


def game_body_case_players(player_names):     
    i = 1
    is_game_ended = False
    move = 0
    while not is_game_ended:             
        if (i % 2) == 1:
            print(player_one_name,'s turn')
            move = cooridante_input()           
            while move in reserve_list:
                print("\n\033[1;31mThis field is already taken!\033[0;0m")
                move = cooridante_input()
            board[move] = player_one_mark
            reserve_list.append(move)          
        elif (i % 2) == 0:
            print(player_two_name,'s turn')
            move = cooridante_input()
            while move in reserve_list:
                print("\n\033[1;31mThis field is already taken!\033[0;0m")
                move = cooridante_input()
            board[move] = player_two_mark
            reserve_list.append(move)
        i += 1
        print_board(board)
        is_game_ended = chk_winning_conditions(player_one_name, player_two_name)


def ai_random_choose():
    running = True
    while running:
        temp = randint(0, 8)
        if temp not in reserve_list:
            print("The computer choosed: ", temp)
            running = False
            return temp


def game_body_case_comp(player_names):
    i = 1
    is_game_ended = False
    move = 0
    while not is_game_ended:
        if (i % 2) == 1:
            print(player_one_name,'s turn')
            move = cooridante_input()           
            while move in reserve_list:
                print("\n\033[1;31mThis field is already taken!\033[0;0m")
                move = cooridante_input()
            board[move] = player_one_mark
            reserve_list.append(move) 
            print("user reserve list", reserve_list)
        if (i % 2) == 0:
            print("Player computers turn")
            move = ai_random_choose()
            board[move] = player_two_mark
            reserve_list.append(move)
            print("comp reserve list", reserve_list)
        i += 1
        print_board(board)
        is_game_ended = chk_winning_conditions(player_one_name, player_two_name)


def choose_enemy():    
    while True:
        try:
            who_is_second_player = int(input("\n\033[1;33mPress 0 if you want to play with someone, or 1 if to choose the computer: \033[0;0m"))
            if who_is_second_player == 0 or who_is_second_player == 1:
               return who_is_second_player
            else:
                print("\033[1;31mWrong input, try again!\033[0;0m\n")
        except ValueError:
            print("\033[1;31mWrong input, try again!\033[0;0m\n")




new_game = True
computer_plays = False
while new_game:
    
    start = default_timer()
    who_is_second_player = choose_enemy()
    player_one_name, player_two_name = player_names()
    player_one_mark, player_two_mark = player_generator()
    board = list("123456789")
    reserve_list = []

    if who_is_second_player == 0:
        print("\nPlayer one is: ", player_one_name)
        print("Player two is: ", player_two_name)     
        print_board(board)
        game_body_case_players(player_names)
        duration = default_timer() - start
        duration = int(duration)
        print('You played' ,duration, 'sec') 
        with open ('tictactoe_scores.txt', 'r') as f:
            player_scores = f.readlines()
            print(player_scores)
        new_game = start_new_game()

    elif who_is_second_player == 1:        
        print("\nPlayer one is: ", player_one_name)
        print("\nComputer is: ", player_two_name)
        print_board(board)
        game_body_case_comp(player_names)
        duration = default_timer() - start
        duration = int(duration)
        print('You played' ,duration, 'sec')
        with open ('tictactoe_scores.txt', 'r') as f:
            player_scores = f.readlines()
            print(player_scores)
        new_game = start_new_game()
        