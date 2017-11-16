import socket
import sys
import json
import tictactoe2
from timeit import default_timer


def ip_address():  
    ip_hardcoded = True   #hardcoded to avoid timewasting while testing
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
        return "localhost"  


def debug_print(message, data):
    if DEBUG_PRINT == True:
        print(message, data)


def server_echo(s):
    s.sendall(b'echo')
    date = s.recv(1024) 
    if repr(date) == "b'echo'":
        print("the server responded")


def socket_scaffold():    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ip_address()
    port = 2100
    s.connect((host,port))
    print("Server is started on", host, "port:", port)
    return s    

def exchange_names(s, player_name):
    player_name = player_name.encode('utf-8')
    s.send(player_name)
    second_player_name = s.recv(1024)
    return second_player_name.decode('utf-8')
    #print(repr(date.decode('utf-8')))

def get_mark(s):
    player_mark = s.recv(1024)
    return player_mark.decode('utf-8')



def get_list(s):    
    net_dic_data = s.recv(4096)
    debug_print('net dictest', net_dic_data)  #debugprint 

    if len(net_dic_data) == 0: 
        net_dic_data = s.recv(4096)

    net_decoded = net_dic_data.decode('utf-8')
    debug_print('net decoded: ', '"{}"'.format(net_decoded))  #debugprint

    net = json.loads(net_decoded)
    debug_print('net', net)  #debugprint

    local_net = net['datalist']
    debug_print('local net to return', local_net)  #debugprint

    return local_net

DEBUG_PRINT = True

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
        player_two_name = "Computer"        
        print("\nPlayer one is: ", player_one_name)        
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
        s = socket_scaffold()
        player_one_name = tictactoe2.player_names()        
        player_two_name = exchange_names(s, player_one_name)
        player_mark = get_mark(s)
        print("playermark", player_mark)
       

        print("\nPlayer one is: ", player_one_name)        
        print("\nPlayer two is: ", player_two_name)

        net_board = get_list(s)
        #debug_print("netboard in main", net_board)  #debugprint
        tictactoe2.print_board(net_board)  #inital board from client file
        net_reserv_list = get_list(s)  
        print(net_reserv_list)
        
        pass
            
