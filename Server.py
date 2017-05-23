import socket
import sys
import threading
import time
# encode what youre sending and decode what youre recv

THREAD_MAX = 5
connections_list = []
address_list = []
TICK = 0


# create a new server socket
def new_socket():

    try:
        global s
        global host
        global port
        host = '127.0.0.1'
        port = 4445
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # using TCP
        print('Running up the Server...')
    except socket.error as error:
        print("Unable to create socket: " + str(error))

    try:
        print('Binding to Port: ' + str(port))
        s.bind((host, port))
        s.listen(THREAD_MAX)
    except socket.error as error:
        print("Unable to bind to socket: " + str(error))
        sys.exit()


# creates and handles incoming connections
def connection_handler():

        while True:

            try:
                connection, address = s.accept()
                print('Connection Established : ' + 'IP ' + address[0] + ' Port ' + str(address[1]))
                #connection.setblocking(0)  # threading NEEDED?
                connections_list.append(connection)
                address_list.append(address)
                # print('Connection Established : ' + 'IP ' + address[0] + ' Port ' + str(address[1]))
                command_handler(connection)
            except socket.error as error:
                print("Error Connecting: " + str(error))

        s.close()
        sys.exit()


# parses user input into commands
def command_handler(connection):

    while True:

        client_input = connection.recv(1024)
        commands = client_input.split(' ')

        if len(commands) == 0:
            continue

        elif commands[0] == 'quit':
            print('quiting connection :' + connection)
            connections_list.remove(connection)
            connection.close()

        elif commands[0] == 'list':
            list_users()

        elif commands[0] == 'msg':
            pass

        elif commands[0] == 'msg':
            pass

        else:
            connection.send(commands[0])  # convert bytes to string
            temp = ''
            for c in commands:
                temp += c
                #print(temp)


def list_users():
    results = ''
    for i, connection in enumerate(connections_list):
        try:
            # see if user is still active
            connection.send(' ')
            connection.recv(1024)
        except:
            del connections_list[i]
            del address_list[i]
            continue
        # print out the individual IP & port number -- convert to usernames later
        results += str(i) + ' :: ' + str(address_list[i][0]) + ' ' + str(address_list[i][1]) + '\n'
        print('Active Users:')
        print(results)


# clears out stale connections on the server with a quick PING
def clear_past_connections():
    for n in connections_list:
        n.close()  # sanitize old connections & delete global lists
        del connections_list[:]
        del address_list[:]
        # del user_list[:] -- need to implement the change from IP to username


# create individual threads per client connection
def create_threads():

    for i in range(THREAD_MAX):
        t = threading.Thread(target=connection_handler())  # change this
        t.daemon = True # close threads
        t.start()
    s.close()


def main():

    new_socket()
    clear_past_connections()
    connection_handler()
    # create_threads() # or do I call connection handler?


main()

# def run_server():
#     while True:
#         client_connection, address = s.accept()
#         threading.Thread(target=client_handler, args=(client_connection, address)).start()
#