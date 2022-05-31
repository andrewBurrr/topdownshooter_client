from socket import socket, AF_INET, SOCK_STREAM
import errno
from threading import Thread

import pickle

HEADER_SIZE = 10


class Client:
    def __init__(self, config):
        self.my_username = "test_client"
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((config["Address", config["Port"]]))
        self.client.setblocking(False)
        self.out_buffer = []
        username = self.my_username.encode('utf-8')
        username_header = f"{len(username):<{HEADER_SIZE}}".encode('utf-8')
        self.client.send(username_header + username)

    def run(self):
        while True:
            # construct packet
            message = input(f"{self.my_username} > ")

            if message:
                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_SIZE}}".encode('utf-8')
                self.client.send(message_header + message)

            try:
                while True:
                    username_header = self.client.recv(HEADER_SIZE)
                    if not len(username_header):
                        print("Connection closed by server")
                        exit(-1)

                    username_length = int(username_header.decode('utf-8').strip())
                    username = self.client.recv(username_length).decode('utf-8')

                    message_header = self.client.recv(HEADER_SIZE)
                    message_length = int(message_header.decode('utf-8').strip())
                    message = self.client.recv(message_length).decode('utf-8')

                    print(f"{username} > {message}")
            except IOError as err:
                if err.errno != errno.EAGAIN and err.errno != errno.EWOULDBLOCK:
                    print(f"Reading Error: {str(err)}")
                continue
            except Exception as err:
                print(f"Reading Error: {str(err)}")
                exit(-1)

# class Client:
#     def __init__(self, config):
#         self.client = socket(AF_INET, SOCK_STREAM)
#         self.client.connect((config["Address"], config["Port"]))
#
#     def run(self):
#         read_thread = Thread(target=self.read)
#         read_thread.start()
#
#         write_thread = Thread(target=self.write)
#         write_thread.start()
#
#     def read(self):
#         while True:
#             try:
#                 full_msg = b''
#                 new_msg = True
#                 while True:
#                     msg = self.client.recv(16)
#                     if new_msg:
#                         print(f"New message length: {msg[:HEADER_SIZE]}")
#                         msg_len = int(msg[:HEADER_SIZE])
#                         new_msg = False
#
#                     print(f"Full message length: {msg_len}")
#
#                     full_msg += msg
#
#                     print(len(full_msg))
#
#                     if len(full_msg) - HEADER_SIZE == msg_len:
#                         print("Full message received")
#                         print(full_msg[HEADER_SIZE:])
#                         print(pickle.loads(full_msg[HEADER_SIZE:]))
#                         new_msg = True
#                         full_msg = b''
#             except error:
#                 print("error")
#                 self.client.close()
#                 break
#
#     def write(self):
#         while True:
#             message = f'{input()}'
#             self.client.send(message.encode('ascii'))
