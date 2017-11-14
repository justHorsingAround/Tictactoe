import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 2100
s.bind((host,port))
s.listen(5)

s.close()
