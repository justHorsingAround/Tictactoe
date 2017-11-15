import socket
import sys
import csv
import tictactoe2
from random import randint
from timeit import default_timer


def ip_address():  
    ip_hardcoded = False   #hardcoded to avoid timewasting while testing
    if ip_hardcoded is not True: 
        while True:
            ip_input = input("Please enter the server ip: ")
            if ip_input == '\x1b':
                sys.exit(0)
            try:            
                socket.inet_aton(ip_input)
                return ip_input
            except:
                print("Error, not a valid ip address, "
                      "please try again or press 'esc' to exit!")
    else:
        return " . . . ."   
    


def server_echo():
    s.sendall('echo')
    date = s.recv(1024) 

def socket_scaffold():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ip_address()
    port = 2100
    s.connect((host,port))
    s.close()


new_game = True
computer_plays = False
while new_game:
   
    start = default_timer()
    tictactoe2.who_is_second_player = tictactoe2.choose_enemy()
    player_one_name, player_two_name = tictactoe2.player_names()
    player_one_mark, player_two_mark = tictactoe2.player_generator()
    board = list("123456789")
    reserve_list = []
    
    

    if tictactoe2.who_is_second_player == 0:
        print("\nPlayer one is: ", player_one_name)
        print("Player two is: ", player_two_name)     
        tictactoe2.print_board(board)
        tictactoe2.game_body_case_players(player_one_name, player_two_name,
                                          reserve_list, board, player_one_mark,
                                          player_two_mark)
        duration = default_timer() - start
        duration = int(duration)
        
        print('You played' ,duration, 'sec','\n')
        print('×××××××××××××××××××××××')
        print('××××× \033[1;31mTOP PLAYERS\033[0;0m ×××××')
        print('×××××××××××××××××××××××')  
        '''with open ('tictactoe_scores.txt', 'r') as f:
            player_scores = f.readlines()
            print(player_scores)'''
        new_game = tictactoe2.start_new_game()

    elif tictactoe2.who_is_second_player == 1:        
        print("\nPlayer one is: ", player_one_name)
        print("\nComputer is: ", player_two_name)
        tictactoe2.print_board(board)
        tictactoe2.game_body_case_comp(player_one_name, player_two_name,
                                       reserve_list, board, player_one_mark,
                                       player_two_mark)
        duration = default_timer() - start
        duration = int(duration)
        
        print('You played' ,duration, 'sec','\n')
        print('×××××××××××××××××××××××')
        print('××××× \033[1;31mTOP PLAYERS\033[0;0m ×××××')
        print('×××××××××××××××××××××××') 
        '''with open ('tictactoe_scores.csv', 'r') as rf:
            score_name = csv.reader(rf)
            temp_list = list(score_name)
            for item in range(len(temp_list[0])):
                print(temp_list[0][item])'''
        new_game = tictactoe2.start_new_game()
            
