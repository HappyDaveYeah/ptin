__author__ = 'dmicomrt'

import socket

HOST = '192.168.60.18'  # The remote host
PORT = 8088  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

for i in range(10):

    a = raw_input('input: ')
    print a
    s.send('hello')

s.close()
