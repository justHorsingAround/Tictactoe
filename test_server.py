import socket
import time

def debug_print(message):
    if DEBUG_PRINT == True:
        print(message)

def accept_connection():
    connection, address = sockt.accept()
    print("Received a connection from", address[0], ":", port)
    return connection, address
    
DEBUG_PRINT=True

sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 2100
sockt.bind((host,port))
sockt.listen(5)
first_connection, first_address = accept_connection()
sec_connection, sec_address = accept_connection()
name_one = first_connection.recv(1024)
name_two = sec_connection.recv(1024)
first_connection.sendall(name_two)
sec_connection.sendall(name_one)

sockt.close()
