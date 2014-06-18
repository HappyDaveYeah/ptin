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

HOST = '192.168.60.18'               
PORT = 8088
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

coloring = -1

for i in range(10):

    data = s.recv(1024)
    if not data: break
    print 'rebo alguna cosa'
    if coloring == 1: color("red")
    else: color("green")
    makeSpiral(200)
    coloring *= -1

s.close()
