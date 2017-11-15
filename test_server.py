import socket
import time
import json
from random import randint

def debug_print(message):
    if DEBUG_PRINT == True:
        print(message)

def accept_connection(s):
    connection, address = s.accept()
    print("Received a connection from", address[0], ":", port)
    return connection, address


    
    

    
DEBUG_PRINT=True

debug_print("Server is running.")

board = list("123456789")
reserve_list = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 2100
s.bind((host,port))
s.listen(5)
first_connection, first_address = accept_connection(s)
sec_connection, sec_address = accept_connection(s)
name_one = first_connection.recv(1024)
name_two = sec_connection.recv(1024)
first_connection.sendall(name_two)
sec_connection.sendall(name_one)

json_obj = {'board': board}


b_board = json.dumps(json_obj)
dec_board = b_board.encode('utf-8')
first_connection.sendall(dec_board)
sec_connection.sendall(dec_board)



debug_print("Server is up to shotdown")
s.close()
