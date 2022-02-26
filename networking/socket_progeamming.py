"""
connecting client an server is a socket..
"""
import socket

# import sys

# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("socker created successfully")
# except socket.error as err:
#     print(f"socker created failed with error {err}")

# port = 80

# try:
#     ip = socket.gethostbyname("youngstorage.myddns.me")
# except socket.gaierror:
#     print(f"there was a error resolving host")
#     sys.exit(1)

# s.connect((ip, port))

# print("the socket was successfully connectde to the youngstorage")

# print(ip)
s = socket.socket()
print("socket successfully created")
port = 12345
s.bind(("", port))
print(f"socket binded to {port}")
s.listen(5)
while True:
    c, addr = s.accept()
    print(f"got connection from {addr}")
    c.send(b'thank u for connecting to the socket\n')
    c.close()
