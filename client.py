import socket
import sys
import json
import tictactoe2
from timeit import default_timer


def ip_address():  
    ip_hardcoded = True  # hardcoded to avoid timewasting while testing
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
    if DEBUG_PRINT is True:
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
    s.connect((host, port))
    print("Server is started on", host, "port:", port)
    return s   


def exchange_names(s, player_name):
    player_name = player_name.encode('utf-8')
    s.send(player_name)    


def send_data_to_server(s, net_board, net_reserve_list):
    json_obj = {'board': net_board, 'reserve': net_reserve_list}
    data_dict = json.dumps(json_obj)
    encoded_data = data_dict.encode('utf-8')
    s.sendall(encoded_data)


def get_list(s):    
    net_dic_data = s.recv(4096)
    debug_print('net dictest', net_dic_data)  # debugprint 

    if len(net_dic_data) == 0:
        print("RECIEVED 0") 
        net_dic_data = s.recv(4096)

    net_decoded = net_dic_data.decode('utf-8')
    debug_print('net decoded: ', '"{}"'.format(net_decoded))  # debugprint
    net = json.loads(net_decoded)
    debug_print('net', net)  # debugprint
    local_net = net['board']
    debug_print('local net to return', local_net)  # debugprint
    net_reserve_list = net['reserve'] 
    debug_print('reserve list: ', net_reserve_list)  # debugprint
    net_other_player_name = net['name']
    net_other_mark = net['mark']
    round_number = net['round']
    return local_net, net_reserve_list, net_other_player_name, net_other_mark, round_number

DEBUG_PRINT = False

new_game = True
computer_plays = False
while new_game:   
    start = default_timer()
    who_is_second_player = tictactoe2.choose_enemy()    
    player_one_mark, player_two_mark = tictactoe2.player_generator()

    board = list("123456789")
    reserve_list = []
    net_board = []
    net_reserve_list = []

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
        # tictactoe2.print_best_score()        
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
        # tictactoe2.print_best_score()         
        new_game = tictactoe2.start_new_game()
    elif who_is_second_player == 2:
        s = socket_scaffold()
        player_one_name = tictactoe2.player_names()
        exchange_names(s, player_one_name) 
        net_board, net_reserve_list, player_two_name, player_one_mark, round_numb = get_list(s)
        print("\nPlayer one is: ", player_one_name)
        print("Player's mark is:", player_one_mark)
        player_two_mark = ''
        if player_one_mark == '\033[1;31mX\033[0;0m':
            player_two_mark = '\033[1;32mo\033[0;0m'
        else:
            player_two_mark = '\033[1;31mX\033[0;0m'
   
        print("\nPlayer two is: ", player_two_name)
        print("Player's mark is:", player_two_mark)

        # while round_numb <= 9:
            # debug_print("netboard in main", net_board)  #debugprint
        tictactoe2.print_board(net_board)  
        tictactoe2.game_body_case_net(player_one_name, player_two_name,
                                    net_reserve_list, net_board, player_one_mark,
                                    player_two_mark)
        send_data_to_server(s, net_board, net_reserve_list)

        # print('net board after step', net_board)
        # print('round number', round_numb)                                 
        # print(' net reserve list after move', net_reserve_list)

