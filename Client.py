import socket


def new_client():

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 4447
        client.connect((host, port))
    except socket.error as err:
        print("Unable to create client socket: " + str(err))

    while True:
        client_message = input('Enter command: ') # do I need to encode before sending?
        client.send(client_message)
        if 'quit' in client_message:
            client.close()
            break;
        # reply from the server
        data = client.recv(1024)
        print('Received: ' + data.decode('utf-8'))


def main():
    new_client()

main()
















# hostname = ''
# port = 0
# recv_buffer = 1024
# user_list = []
#
# if len(sys.argv) < 3:
#     sys.stderr.write("Usage: ")
#
#
# def command_handler(command, parameter):
#     global user_list
#     global username
#
#     #create username
#     if command == "nick":
#         if parameter[0] == '' or '\n':
#             print('Invalid Username. No spaces allowed.')
#             return
#         elif:
#             parameter not in user_list
