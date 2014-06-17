from turtle import *
import socket


speed(0)
pensize(10)

def makeSquare(size):
    for i in range(4):
        forward(size)
        left(90)

def makeSpiral(size):
    for i in range (18):
        makeSquare(size)
        left(20)

HOST = ''                 # Symbolic name meaning the local host
PORT = 8088              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

coloring = -1

for i in range(10):
    conn, addr = s.accept()
    print 'Connected by', addr
    data = conn.recv(1024)
    if coloring == 1: color("red")
    else: color("green")
    makeSpiral(75)
    coloring *= -1
    conn.send(data)
    conn.close()

exitonclick()

