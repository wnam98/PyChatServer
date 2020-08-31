# Created by: Walter Nam 8/31/20
import socket
import threading


class Server:

    port = 5050
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (server, port)
    encoding = 'utf-8'
    disconnect = 'quit()'

    def __init__(self):
        self.server.bind(self.address)
        self.server.listen(1)

    def run(self):
        c, addr = self.server.accept()
        print("Connection from: " + str(addr))
        while True:
            data = c.recv(1024).decode(self.encoding)
            if not data:
                break
            print("Recieved from client: " + data)
            data = data.upper()
            print("Sending: " + data)
            c.send(data.encode(self.encoding))
        c.close()

'''
    def handle_connection(self, conn, ack):
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
            conn, ack = self.server.accept()
            connThread = threading.Thread(target=self.handle_connection, args=(conn, ack))
            connThread.daemon = True
            connThread.start()
            self.connections.append(conn)
            print(str(ack[0]) + ':' + str(ack[1], "connected"))
'''