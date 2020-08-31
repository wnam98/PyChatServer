# Created by: Walter Nam 8/31/20

import socket
import threading

class Client:

    port = 5050
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (server, port)
    encoding = 'utf-8'
    disconnect = 'quit()'

    def __init__(self):
        sock = socket.socket()
        sock.connect(self.address)

    def run(self):
        message = input("Write your message:")
        while message != self.disconnect:
            self.sock.send(message.encode(self.encoding))
            data = self.sock.recv(1024).decode(self.encoding)
            print("Recieved from server: " + data)
            message = input(" ->: ")
        self.server.close()