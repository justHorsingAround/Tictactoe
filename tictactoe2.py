import sys
import csv
from random import randint
from timeit import default_timer


def player_names():
    return input('Enter the first players name: ')    


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


def write_score_file(player_name):
    with open("tictactoe_scores.csv", "a") as wf:        
        writer_obj = csv.writer(wf)
        writer_obj.writerow(player_name)


def chk_winning_conditions(player_one_name, player_two_name, reserve_list,
                           board, player_one_mark, player_two_mark):
    i = 0
    while i < 3:        
        if board[0+3*i] == board[1+3*i] and board[1+3*i] == board[2+3*i]:
            if board[1+3*i] == player_one_mark:
                print(player_one_name, "is the winner!")
                write_score_file(player_one_name)
            else:
                print(player_two_name, "is the winner! ")
                write_score_file(player_two_name)
            return True      
        i += 1 

    j = 0
    while j < 3:
        if board[0+j] == board[3+j] and board[3+j] == board[6+j]:
            if board[3+j] == player_one_mark:
                print(player_one_name, "is the winner!")
                write_score_file(player_one_name)
            else:
                print(player_two_name, "is the winner! ")
                write_score_file(player_two_name)
            return True
        j += 1  

    if board[0] == board[4] and board[4] == board[8]:
        if board[4] == player_one_mark:
            print(player_one_name, "is the winner!")
            write_score_file(player_one_name)
        else:
            print(player_two_name, "is the winner! ")
            write_score_file(player_two_name)
        return True

    elif board[2] == board[4] and board[4] == board[6]:
        if board[4] == player_one_mark:
            print(player_one_name, "is the winner!")
            write_score_file(player_one_name)
        else:
            print(player_two_name, "is the winner! ")
            write_score_file(player_two_name)
        return True

    elif len(reserve_list) == 9:
        print('This is a draw!')
        return True

    else:
        return False


def game_body_case_net(player_one_name, player_two_name, net_reserve_list, net_board, player_one_mark,
                       player_two_mark): 
    is_game_ended = False
    move = 0
    
    print(player_one_name, 's turn')
    move = cooridante_input()
    while move in net_reserve_list:
        print("\n\033[1;31mThis field is already taken!\033[0;0m")
        move = cooridante_input()
    net_board[move] = player_one_mark
    net_reserve_list.append(move)
    is_game_ended = chk_winning_conditions(player_one_name, player_two_name,
                                           net_reserve_list, net_board, player_one_mark,
                                           player_two_mark)
        
        
def game_body_case_players(player_one_name, player_two_name, 
                           reserve_list, board, player_one_mark,
                           player_two_mark):     
    i = 1
    is_game_ended = False
    move = 0
    while not is_game_ended:             
        if (i % 2) == 1:
            print(player_one_name, 's turn')
            move = cooridante_input()           
            while move in reserve_list:
                print("\n\033[1;31mThis field is already taken!\033[0;0m")
                move = cooridante_input()
            board[move] = player_one_mark
            reserve_list.append(move)          
        elif (i % 2) == 0:
            print(player_two_name, 's turn')
            move = cooridante_input()
            while move in reserve_list:
                print("\n\033[1;31mThis field is already taken!\033[0;0m")
                move = cooridante_input()
            board[move] = player_two_mark
            reserve_list.append(move)
        i += 1
        print_board(board)
        is_game_ended = chk_winning_conditions(player_one_name, player_two_name,
                                               reserve_list, board, player_one_mark,
                                               player_two_mark)


def ai_random_choose(reserve_list):
    running = True
    while running:
        temp = randint(0, 8)
        if temp not in reserve_list:
            print("The computer choosed: ", temp)
            running = False
            return temp


def game_body_case_comp(player_one_name, player_two_name,
                        reserve_list, board, player_one_mark,
                        player_two_mark):
    i = 1
    is_game_ended = False
    move = 0
    while not is_game_ended:
        if (i % 2) == 1:
            print(player_one_name, 's turn')
            move = cooridante_input()           
            while move in reserve_list:
                print("\n\033[1;31mThis field is already taken!\033[0;0m")
                move = cooridante_input()
            board[move] = player_one_mark
            reserve_list.append(move) 
            print("user reserve list", reserve_list)
        if (i % 2) == 0:
            print("Player computers turn")
            move = ai_random_choose(reserve_list)
            board[move] = player_two_mark
            reserve_list.append(move)
            print("comp reserve list", reserve_list)
        i += 1
        print_board(board)
        is_game_ended = chk_winning_conditions(player_one_name, player_two_name,
                                               reserve_list, board, player_one_mark,
                                               player_two_mark)


def choose_enemy():    
    while True:
        try:
            who_is_second_player = int(input("\n\033[1;33mPress 0 if you want to play with someone,"
                                             "or 1 if to choose the computer: \033[0;0m"))
            if who_is_second_player == 0 or who_is_second_player == 1 or who_is_second_player == 2:
               return who_is_second_player
            else:
                print("\033[1;31mWrong input, try again!\033[0;0m\n")
        except ValueError:
            print("\033[1;31mWrong input, try again!\033[0;0m\n")


def fancy_score():
    print('×××××××××××××××××××××××')
    print('××××× \033[1;31mTOP PLAYERS\033[0;0m ×××××')
    print('×××××××××××××××××××××××')  


def timer(start):
    duration = default_timer() - start
    duration = int(duration)    
    print('You played', duration, 'sec','\n')


def print_best_score():
    '''with open ('tictactoe_scores.txt', 'r') as f:
            player_scores = f.readlines()
            print(player_scores)'''
    pass

    
    
    




