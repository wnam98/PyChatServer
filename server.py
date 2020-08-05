import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

#socket is bound to a port number so that the TCP can identify the app data

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    pass

def start():
    server.listen()
    connected = True
    while connected:
        conn, addr = server.accept()

print("[STARTING] server is starting ...")
start()