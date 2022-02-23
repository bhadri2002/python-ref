import socket   #import socket from the lib

s=socket.socket() # init socker
host = socket.gethostname() #get localhost
port = 8888 # asign port for the connection
s.bind((host,port)) #bind the connection using host and port

s.listen(5) #listening for the connection

while True:
    c,addr = s.accept() # if the client connect to the server it works
    print("got connection from",addr)
    c.send(b"thank u for connection our service")