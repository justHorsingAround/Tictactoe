import socket
import time
import json
from random import randint


def debug_print(message):
    if DEBUG_PRINT is True:
        print(message)


def accept_connection(s):
    connection, address = s.accept()
    print("Received a connection from", address[0], ":", port)
    return connection, address


def send_list_to_first(s, board, reserve, name_two, mark_one, round_numb):    
    print("first send list", board)
    json_obj = {'board': board, 'reserve': reserve,
                'name': name_two, 'mark': mark_one,
                'round': round_numb}
    data_dict = json.dumps(json_obj)
    decoded_data = data_dict.encode('utf-8')
    first_connection.sendall(decoded_data) 
    print("decoded data from first send", decoded_data)   
   

def send_list_to_second(s, board, reserve, name_one, mark_two, round_numb):
    print("second send list", board)
    json_obj = {'board': board, 'reserve': reserve,
                'name': name_one, 'mark': mark_two,
                'round': round_numb}
    data_dict = json.dumps(json_obj)
    decoded_data = data_dict.encode('utf-8')
    sec_connection.sendall(decoded_data)
    print("decoded data from second send", decoded_data)   


def recieve_data(s):
    recv_dict_data = s.recv(4096)
    serv_decoded = recv_dict_data.decode('utf-8')
    loaded_data = json.loads(serv_decoded)
    player_board = loaded_data['board']
    print('board in recivedata()', player_board)
    reserve = loaded_data['reserve'] 
    game_ended = loaded_data['end']
    return player_board, reserve, game_ended


def player_generator():
    temp = randint(0, 1)
    if temp == 0:
        player_one = '\033[1;31mX\033[0;0m'
        player_two = '\033[1;32mo\033[0;0m'
    else:
        player_one = '\033[1;32mo\033[0;0m'
        player_two = '\033[1;31mX\033[0;0m'
    return player_one, player_two
    
print("Server is started")   
DEBUG_PRINT = False
turn_counter = 1
MAX_TURNS = 9
board = list("123456789")
reserve_list = [-1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 2100
s.bind((host, port))
s.listen(5)
first_connection, first_address = accept_connection(s)
sec_connection, sec_address = accept_connection(s)

name_one = first_connection.recv(1024)
name_one = name_one.decode('utf-8')
name_two = sec_connection.recv(1024)
name_two = name_two.decode('utf-8')
player_one_mark, player_two_mark = player_generator()

send_list_to_first(s, board, reserve_list, name_two, player_one_mark, turn_counter)
send_list_to_second(s, board, reserve_list, name_one, player_two_mark, turn_counter)

while turn_counter <= MAX_TURNS:
    print(board)
    if turn_counter % 2 == 1:
        send_list_to_first(s, board, reserve_list, name_two, player_one_mark, turn_counter)
        board, reserve_list, is_game_ended = recieve_data(first_connection)
        print('after recieve', board, reserve_list)
        if is_game_ended is True:
            break
    elif turn_counter % 2 == 0:
        print('board in else', board)        
        send_list_to_second(s, board, reserve_list, name_one, player_two_mark, turn_counter)
        board, reserve_list, is_game_ended = recieve_data(sec_connection)
        if is_game_ended is True:
            break
    print('after recieve', board, reserve_list)

    turn_counter += 1

print("Server is up to shotdown")
s.close()
