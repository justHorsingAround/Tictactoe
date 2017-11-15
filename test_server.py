import socket
import time

sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 2100
sockt.bind((host,port))
sockt.listen(5)
connection, address = sockt.accept()
print("Connected by", address)
while True:
    data = connection.recv(1024)
    if not data:
        break
    connection.sendall(data)

sockt.close()
