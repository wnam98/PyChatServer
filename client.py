# Created by: Walter Nam 8/31/20

import socket
import threading
import sys

class Client:
    def run(self):
        message = input("Write your message:")
        while message != self.disconnect:
            self.server.send(message.encode(self.encoding))
            data = self.server.recv(1024).decode(self.encoding)
            print("Recieved from server: " + data)
            message = input(" ->: ")
        self.server.close()

'''
class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_msg(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))

    def __init__(self, address):
        self.sock.connect((address, 10000))

        inThread = threading.Thread(target = self.send_msg)
        inThread.daemon = True
        inThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))
'''