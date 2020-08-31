# Created by: Walter Nam 8/31/20

import client
import server
import sys

if(len(sys.argv) > 1):
    client = client.Client(sys.argv[1])
else:
    server = server.Server()
    server.run()