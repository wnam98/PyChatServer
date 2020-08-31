# Created by: Walter Nam 8/31/20

import client
import server

server = server.Server()
client = client.Client()

server.run()
client.run()