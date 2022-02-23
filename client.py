import socket

s = socket.socket()
host = socket.gethostname()
port = 8888

while True:
    s.connect((host,port))
    rev = s.recv(1024)
    print(rev.decode())