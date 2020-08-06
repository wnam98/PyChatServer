import socket
import threading as thd


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