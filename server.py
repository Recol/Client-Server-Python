import socket
import sys

import os

import client
from client import type_selection, SERVER_PORT, SERVER_HOST, client_storage
t
# import the declared parameters to avoid duplicate information

BUFFER_SIZE = 4096
client_file_storage = ""

SEPARATOR = "<SEPARATOR>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("", int(sys.argv[1])))  # force argument 1 and 2 as host, avoides string to int issues
s.listen(5)

print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

client_socket, address = s.accept()
print(f"[+] {address} is connected.")

received = client_socket.recv(
    BUFFER_SIZE).decode()  # implement static buffer size so it will transmute across multiple iterations
filename, filesize = received.split(SEPARATOR)
# split the received file into the filename and filesize
filename = os.path.basename(filename)

filesize = int(filesize)

server_file_storage = 'server_data/'

if type_selection == "get":  # handle server type selection imported from the client
    server_file_storage += filename
    serverData = client.read_file(server_file_storage)

elif type_selection == "put":
    client_file_storage += filename
    data = client.read_file(client_file_storage)

if type_selection == "list":
    client.list_dir()

elif type_selection != "get" or "put" or "list":
    print('This is an invalid parameter option, please select a valid one.')

with open(filename, "wb") as f:
    while True:

        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break

    f.write(bytes_read)

    client_socket.close()
    s.close()
