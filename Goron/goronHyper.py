__author__ = 'dmicomrt'
import socket
import sys

HOST = 'localhost'  # HOST
PORT = 50007  # PORT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


for i in range(0, 10):
    data = []
    data.append(raw_input('Command desired :'))
    if data[0] == 'close': break
    data.append(raw_input('App to apply: '))
    s.send(data[0])
    s.recv(0)
    s.send(data[1])

    if data[0] == 'ADD':
        s.recv(0)
        f=open (data[1], "rb")
        l = f.read(1024)
        while (l):
            s.send(l)
            l = f.read(1024)
        f.close()

    data = s.recv(1024)
    print(data)

s.close()