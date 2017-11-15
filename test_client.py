import socket
import sys
import tictactoe2
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
        return ". . ."  


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
    who_is_second_player = tictactoe2.choose_enemy()    
    player_one_mark, player_two_mark = tictactoe2.player_generator()
    board = list("123456789")
    reserve_list = []

    if who_is_second_player == 0:
        player_one_name = tictactoe2.player_names()
        player_two_name = tictactoe2.player_names()
        print("\nPlayer one is: ", player_one_name)        
        print("Player two is: ", player_two_name)
        tictactoe2.print_board(board)
        tictactoe2.game_body_case_players(player_one_name, player_two_name,
                                          reserve_list, board, player_one_mark,
                                          player_two_mark)
        tictactoe2.timer(start)
        tictactoe2.fancy_score()
        #tictactoe2.print_best_score()        
        new_game = tictactoe2.start_new_game()

    elif who_is_second_player == 1:
        player_one_name = tictactoe2.player_names()        
        print("\nPlayer one is: ", player_one_name)
        player_two_name = "Computer"
        print("\nPlayer two is: ", player_two_name)
        tictactoe2.print_board(board)
        tictactoe2.game_body_case_comp(player_one_name, player_two_name,
                                       reserve_list, board, player_one_mark,
                                       player_two_mark)
        tictactoe2.timer(start)
        tictactoe2.fancy_score()
        #tictactoe2.print_best_score()         
        new_game = tictactoe2.start_new_game()

    elif who_is_second_player == 2:
        player_one_name = tictactoe2.player_names() 
        
        pass
            
