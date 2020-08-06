import socket as sckt
import threading as thd


class Server:

    def __init__(self, header, port, server, address, encoding):
        self.header = header
        self.port = port
        self.server = server
        self.address = address
        self.encoding = encoding

    def create_server(self, address):
        self.server = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)
        self.server.bind(address)

    def accept_connection(self, conn, address, header, encoding):
        disconnected = "Disconnected"
        print(f"[CLIENT] {address} connected")
        connected = True
        while connected:
            msg_length = conn.recv(header).decode(format)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(format)
                if msg == disconnected:
                    connected = False
                print(f"[{address}] {msg}")
                conn.send("MSG Received".encode(encoding))
            conn.close()

'''
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT) #endpoint
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECTED"

#socket is bound to a port number so that the TCP can identify the app data

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("MSG Received".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    connected = True
    while connected:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting ...")
start()
'''