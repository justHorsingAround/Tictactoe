import socket
import tictactoe2

def ip_address():
    while True
    try:
        ip_input = int(input("Please enter the server ip: "))
        return ip_input
    except:
        print("Error wrong input!")

#todo: reorganise main to the client    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ip_address()
port = 2100
s.connect((host,port))
s.close()