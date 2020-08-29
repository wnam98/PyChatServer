import socket
import threading as thd


class Client:

    def __init__(self, header, port, server, address, encoding):
        self.header = header
        self.port = port
        self.server = server
        self.address = address
        self.encoding = encoding

    def send(self, msg, encoding):
        message = msg.encode(encoding)
        msg_length = len(msg)
        send_length = str(msg_length).encode(encoding)


    def create_msg(self):
        pass

    def disconnect(self):
        pass

'''
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "Client has disconnected"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT) #endpoint

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

message = input(str(">>"))
send(message)
print("Message sent \n")
send(DISCONNECT_MSG)
'''