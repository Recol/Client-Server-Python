import socket
import sys

import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # traffic buffer size
SERVER_HOST = sys.argv[1]  # assign the server host as the first argument
SERVER_PORT = sys.argv[2]  # assign the port as the second argument
type_selection = sys.argv[3].lower()  # assign the "put", "get", etc as the third option and force to lowercase
client_storage = 'client_data/'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

filename = ""
type = sys.argv[3]

# create TCP socket connection
print(f"[+] Connecting to {SERVER_HOST}:{SERVER_PORT}")
s.connect((sys.argv[1], int(sys.argv[2])))  # force argument 1 and 2 as host, avoides string to int issues
print("[+] Connected.")
print("Server up and running")

try:
    if type_selection == "put" or "get":
        s.sendall(type_selection.encode() + b' ' + sys.argv[4].encode())
    else:
        s.sendall(type_selection.encode() + b' ')


except ConnectionRefusedError:
    print('The server has rejected the connection request by the client.')
except ConnectionAbortedError:
    print('The server has aborted the connection to the client.')
except ConnectionError:
    print('An external connection error has taken place with the client')

tb = sys.exc_info()[2]  # detect executable environment to get detailed error information

s.send(f"{filename}{SEPARATOR}{filesize}".encode())  # encode string to UTF-8


def send_file():
    with open(filename, 'rb') as f:


        try:  # begin stream to handle opening the file
            while True:
                if filesize == 0:
                    print("This file contains no bytes, and cannot be sent.")
                    break
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:  # if the files cannot open, terminate the stream early
                    break
            s.sendall(bytes_read)
        except IOError:
            print('There has been an error with the I/O stream.')

        except ConnectionError:
            print('Fatal error occurred')  # if exception occurs, fail safely


s.close()


def read_file(requestfilepath):  # read the file, try and find it, if none are handled, then return an exception
    try:  #
        requestFile = open(file=requestfilepath, mode='rb')
        request = requestFile.readlines()
        return request
    except FileExistsError:
        print('The file already exists and cannot be overridden')
    except FileNotFoundError:
        print('The file has not been located.')
    finally:
        print('The file has been read successfully.')


def list_dir():  # loop file contents using listdirectory
    print('Listing directory contents')
    for contents in os.listdir():
        print(contents)
    print('Completed listing the content directories')


raise Exception().with_traceback(tb)
