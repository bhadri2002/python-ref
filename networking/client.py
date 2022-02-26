import socket


def Main():
    host = "127.0.0.1"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = b"welcome to the hacker world"
    while True:
        s.send(message)
        data = s.recv(1024)
        print(f"receive from the server:>{data.decode()}")
        ans = input("\ndo u want to continue(y/n)")
        if ans == "y" or ans == "Y":
            continue
        else:
            break
    s.close()

if __name__ == "__main__":
    Main()