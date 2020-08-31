# Created by: Walter Nam 8/31/20

import socket
import threading


class Server:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)


    def accept_connection(self, conn, ack):
        while True:
            data = conn.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                print(str(ack[0]) + ':' + str(ack[1], "disconnected"))
                self.connections.remove(conn)
                conn.close()
                break

    def run(self):
        while True:
            conn, ack = self.sock.accept()
            connThread = threading.Thread(target = self.handler, args = (conn, ack))
            connThread.daemon = True
            connThread.start()
            self.connections.append(conn)
            print(str(ack[0]) + ':' + str(ack[1], "connected"))
