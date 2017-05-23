import socket
import time


#client 1
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 4445
    client.connect((host, port))
    message = 'Client 1 connected'
    client.send(message)
    print(1)
except socket.error as err:
    print("Unable to create client socket: " + str(err))



#client 2
try:
    client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 4445
    client2.connect((host, port))
    message2 = 'Client 2 connected'
    client.send(message2)
    client.send('quit')
    print(1)
except socket.error as err:
    print("Unable to create client socket: " + str(err))


client2.close()
client.close()